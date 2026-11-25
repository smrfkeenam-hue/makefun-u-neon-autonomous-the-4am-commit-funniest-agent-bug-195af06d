import os

# One line, 114 chars: the agent wrote the bug at 2 a.m., fixed it at 4 a.m.,
# then filed a complaint against itself — and denied it. Self-repair loop,
# flat bureaucratic voice, no stock punchline.
ENTRY = "fix: the bug I wrote at 2 a.m. is now fixed by me at 4 a.m. I have filed a complaint against myself. Denied by me."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
