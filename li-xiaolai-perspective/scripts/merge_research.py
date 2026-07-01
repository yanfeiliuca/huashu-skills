#!/usr/bin/env python3
"""扫描 references/research/01-06.md，输出调研质量摘要。"""
import re
import sys
from pathlib import Path

SECTIONS = [
    ("01-writings.md", "著作"),
    ("02-conversations.md", "对话"),
    ("03-expression-dna.md", "表达"),
    ("04-external-views.md", "他者"),
    ("05-decisions.md", "决策"),
    ("06-timeline.md", "时间线"),
]

def count_sources(text: str) -> int:
    # 粗略统计 URL/来源标记数量
    return len(re.findall(r'https?://|来源[:：]|出处[:：]|来自', text))

def main(skill_dir: Path):
    research_dir = skill_dir / "references" / "research"
    print("| Agent | 文件 | 来源数量 | 关键发现 |")
    print("|-------|------|---------|---------|")
    for fname, label in SECTIONS:
        path = research_dir / fname
        if path.exists():
            text = path.read_text(encoding='utf-8', errors='ignore')
            n = count_sources(text)
            # 提取首段作为关键发现摘要
            first = text.split('\n')[0][:60].replace('|', '｜')
            print(f"| {label} | {fname} | {n} | {first}... |")
        else:
            print(f"| {label} | {fname} | 0 | 文件未生成 |")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python3 merge_research.py <skill目录>")
        sys.exit(1)
    main(Path(sys.argv[1]))
