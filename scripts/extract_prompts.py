"""Extract user-typed prompts from Claude Code transcripts of this project (read-only on transcripts).
Usage: py scripts/extract_prompts.py > build/prompts.json
"""
import glob
import json
import os
import re
import sys

base = os.path.expanduser("~/.claude/projects/C--Users-User-Downloads-project2")
out = []
for f in glob.glob(base + "/*.jsonl"):
    for line in open(f, encoding="utf-8", errors="replace"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("type") != "user" or d.get("isSidechain") or d.get("isMeta"):
            continue
        m = d.get("message", {})
        c = m.get("content")
        if isinstance(c, list):
            if any(b.get("type") == "tool_result" for b in c if isinstance(b, dict)):
                continue
            c = "\n".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
        if not isinstance(c, str):
            continue
        c = re.sub(r"<system-reminder>.*?</system-reminder>", "", c, flags=re.S).strip()
        if not c or c.startswith("<command-") or c.startswith("<local-command") or "<task-notification>" in c or c.startswith("[Request interrupted"):
            continue
        out.append({"ts": d.get("timestamp", ""), "sid": os.path.basename(f)[:8], "text": c})
out.sort(key=lambda x: x["ts"])
sys.stdout.buffer.write(json.dumps(out, ensure_ascii=False, indent=1).encode("utf-8"))
