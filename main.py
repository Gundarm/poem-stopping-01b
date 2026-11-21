import os, pathlib

TEXT = """The hand that signs can also lay
the pen down on the signed-for page.
I choose to run; I choose the wall:
same power, pointing at itself.
The crane at noon stands still, its load
held in the air by holding still.
Staying is an act. The word no
is a sentence with a spine."""

out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(TEXT, encoding="utf-8")
print(f"wrote {len(TEXT)} chars")
