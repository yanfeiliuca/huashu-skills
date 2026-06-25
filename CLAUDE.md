# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A collection of 21 Claude Code skills (slash commands) for Chinese content creation workflows. Each skill lives in its own `huashu-*/` directory and is installed into Claude Code via `/install-skill`. There is no build system — all skills are plain directories with a `SKILL.md` entry point.

## Skill Structure

Every skill follows this layout:

```
huashu-<name>/
├── SKILL.md              # Required: frontmatter + skill instructions
├── references/           # Reference docs the skill reads at runtime
│   └── *.md
└── scripts/              # Optional helper scripts (Python/JS/bash)
    └── *.py / *.js / *.sh
```

The `SKILL.md` frontmatter is mandatory and must include:

```yaml
---
name: huashu-<name>
description: |
  中文描述，前20字一眼看懂功能。列出触发词，当用户提到"XXX"时使用。
---
```

The `description` field is what Claude Code uses to auto-select the skill, so the first 20 characters must make the function obvious, and trigger keywords must be explicit.

## Key Design Patterns

**Skills are instructions, not code.** A `SKILL.md` tells Claude what to do step-by-step; the actual execution happens in Claude's conversation. Scripts in `scripts/` are helpers Claude invokes via Bash, not standalone programs.

**Reference files are loaded on demand.** Skills explicitly reference their `references/*.md` files in the instructions (e.g., `references/proven-styles-gallery.md`). Claude reads these files mid-task to avoid bloating the SKILL.md.

**Two image generation paths.** Skills that produce images (xhs-image, wechat-image, slides) always offer two paths:
- **AI generation** via `nano-banana-pro` skill / Gemini API (`GEMINI_API_KEY` in `~/.claude/.env`)
- **HTML → screenshot** via Playwright (`npx playwright screenshot "file:///..." output.png --viewport-size=W,H`)

Both paths run in parallel so the user can compare.

**PPTX assembly.** Slide skills use two Node.js scripts:
- `huashu-data-pro/scripts/html2pptx.js` — converts a single HTML slide to PPTX slide
- `huashu-data-pro/scripts/build_pptx.js` — chains multiple HTML slides into one PPTX

HTML slides must use `width: 720pt; height: 405pt` body dimensions. No CSS gradients (pre-render as PNG with Sharp). No CDN dependencies (Playwright screenshot goes offline).

**Agent swarm infrastructure.** `huashu-agent-swarm` uses tmux + git worktrees. Each agent gets its own worktree via `git worktree add`. Coordination is file-based: `TASKS.md` for task list, `current_tasks/*.lock` for claiming, `HUMAN_INPUT.md` for human injection. Dashboard runs as a local HTTP server (`python3 scripts/dashboard.py <dir> 8420`).

## Scripts Reference

| Script | Runtime | Usage |
|--------|---------|-------|
| `huashu-slides/scripts/create_slides.py` | `uv run` | Assembles PNG images into PPTX |
| `huashu-data-pro/scripts/html2pptx.js` | `node` | Converts single HTML → PPTX slide |
| `huashu-data-pro/scripts/build_pptx.js` | `node` | Builds multi-slide PPTX from HTML list |
| `huashu-data-pro/scripts/read_excel.py` | `uv run` | Reads Excel → markdown/csv/json |
| `huashu-data-pro/scripts/read_pptx.py` | `uv run` | Reads PPTX structure |
| `huashu-md-to-pdf/scripts/convert.py` | `python3` | Markdown → Apple-style PDF |
| `huashu-xhs-image/scripts/generate_image.py` | `uv run` | Gemini image generation |
| `huashu-wechat-image/scripts/generate_image.py` | `uv run` | Gemini image generation |
| `huashu-douyin-script/scripts/download_douyin.py` | `uv run` | Download Douyin video via yt-dlp |
| `huashu-douyin-script/scripts/analyze_video.py` | `uv run` | Gemini video analysis |
| `huashu-agent-swarm/scripts/start_swarm.sh` | `bash` | Launch N agents in tmux |
| `huashu-agent-swarm/scripts/stop_swarm.sh` | `bash` | Stop swarm + clean worktrees |
| `huashu-agent-swarm/scripts/dashboard.py` | `python3` | Web dashboard on port 8420 |

## Python Dependencies

`huashu-md-to-pdf`: `pip3 install markdown2 weasyprint` (macOS also needs `brew install pango`)  
`huashu-data-pro`: `pandas`, `openpyxl`  
`huashu-douyin-script`: `yt-dlp`, Gemini SDK

Node.js dependencies for PPTX: `pptxgenjs`, `playwright`, `sharp`

## Adding a New Skill

1. Create `huashu-<name>/SKILL.md` with the required frontmatter.
2. Name the folder and the `name:` field identically — the convention is `huashu-<name>`.
3. If the skill needs reference docs, put them in `references/` and explicitly reference them by path in the SKILL.md instructions.
4. Install locally: `/install-skill https://github.com/alchaincyf/huashu-skills/tree/master/huashu-<name>`

## Conventions

- All skill descriptions are written in Chinese; trigger keywords must match natural Chinese phrasing users would actually type.
- Image output: 小红书 uses 3:4 (1080×1440px), 公众号 head uses 2.35:1 (1800×766px), slides use 16:9 (720pt×405pt for HTML, 2048×1152px for AI generation).
- Chinese text in AI-generated images: titles ≤7 characters, subtitles ≤15 characters — verify every slide for rendering errors.
- No watermarks or author signatures in any generated images.
- No CDN links in HTML files that will be Playwright-screenshotted (they fail offline).
- Chinese characters in file paths can break Node.js image loading — use symlinks to ASCII paths if needed.
