#!/usr/bin/env python3
"""将 SRT/VTT 字幕清洗为纯文本 transcript。"""
import re
import sys
from pathlib import Path

def clean_srt(text: str) -> str:
    # 去掉时间戳行、序号行、HTML 标签
    lines = text.splitlines()
    out = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if re.match(r'^\d+$', line):
            continue
        if re.match(r'\d{1,2}:\d{2}:\d{2}', line):
            continue
        line = re.sub(r'<[^>]+>', '', line)
        line = re.sub(r'\{\\an\d\}', '', line)
        out.append(line)
    # 去连续重复行
    deduped = []
    prev = None
    for line in out:
        if line != prev:
            deduped.append(line)
        prev = line
    return '\n'.join(deduped)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python3 srt_to_transcript.py <input.srt> [output.txt]")
        sys.exit(1)
    inp = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else inp.with_suffix('.txt')
    text = clean_srt(inp.read_text(encoding='utf-8', errors='ignore'))
    out.write_text(text, encoding='utf-8')
    print(f"已写入 {out}")
