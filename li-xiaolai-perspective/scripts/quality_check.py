#!/usr/bin/env python3
"""检查 SKILL.md 是否通过 6 项质量标准。"""
import re
import sys
from pathlib import Path

CHECKS = [
    ("心智模型数量", r'## 心智模型', 3, 7, "count_sections"),
    ("诚实边界条目", r'## 诚实边界', 3, None, "count_boundary_items"),
    ("表达DNA", r'## 表达 DNA|## 表达DNA', 1, None, "exists"),
    ("内在张力", r'## .*张力|## 价值观与反模式', 2, None, "count_lines"),
    ("一手来源", r'一手来源|一手素材', 1, None, "exists"),
]

def count_sections(text: str, pattern: str) -> int:
    # 只在 ## 心智模型 到下一个 ## 之间统计 ### 数量
    m = re.search(r'## 心智模型.*?(?=\n## |$)', text, re.S)
    if not m:
        return 0
    return len(re.findall(r'^### ', m.group(0), re.M))

def count_boundary_items(text: str, pattern: str) -> int:
    # 统计 ## 诚实边界 下的 1. 2. 3. 条目数
    m = re.search(r'## 诚实边界.*?(?=\n## |$)', text, re.S)
    if not m:
        return 0
    return len(re.findall(r'^\d+\. ', m.group(0), re.M))

def main(path: Path):
    text = path.read_text(encoding='utf-8', errors='ignore')
    print(f"质量检查: {path}")
    print("-" * 40)
    for name, pat, low, high, kind in CHECKS:
        if kind == "count_sections":
            val = count_sections(text, pat)
        elif kind == "count_boundary_items":
            val = count_boundary_items(text, pat)
        elif kind == "count_lines":
            val = len(re.findall(pat, text, re.M))
        else:
            val = 1 if re.search(pat, text, re.M) else 0
        ok = (low is None or val >= low) and (high is None or val <= high)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: {val} (期望 >= {low}{f', <= {high}' if high else ''})")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python3 quality_check.py <SKILL.md路径>")
        sys.exit(1)
    main(Path(sys.argv[1]))
