#!/bin/bash
# 下载 YouTube 字幕
# 用法: bash download_subtitles.sh <YouTube_URL> [输出目录]

URL="$1"
OUT_DIR="${2:-../references/sources/transcripts}"

if [ -z "$URL" ]; then
    echo "用法: bash download_subtitles.sh <YouTube_URL> [输出目录]"
    exit 1
fi

mkdir -p "$OUT_DIR"

yt-dlp --list-subs "$URL" 2>/dev/null

yt-dlp --write-sub --write-auto-sub --sub-langs "zh-CN,zh-TW,zh-Hans,zh-Hant,en" \
    --skip-download --sub-format srt \
    -o "$OUT_DIR/%(title)s.%(ext)s" "$URL"
