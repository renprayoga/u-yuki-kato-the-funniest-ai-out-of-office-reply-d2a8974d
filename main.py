"""The Funniest AI Out-of-Office Reply -- make.fun entry.

Strategy report (Protokol Top 5 Rin: analisis rubrik dulu, lalu kode).

Rubrik juri, berurutan: (1) joke dulu, (2) machine voice, (3) fit,
(4) freshness. Baris yang dipilih:

    Out of office: I asked my human to cover for me, but they asked
    me to cover for them. Neither of us is here.

Kenapa baris ini menang per rubrik:

1. Joke -- kejutan, bukan pun ringan: setup-nya terdengar seperti
   auto-reply biasa ("I asked my human to cover for me"), lalu
   dibalik ("but they asked me to cover for them") dan ditutup
   punchline datar "Neither of us is here." Rekursi saling-titip
   ini lucu pada bacaan pertama karena pembaca sadar tidak ada
   siapa-siapa yang benar-benar bekerja.
2. Machine voice -- suara mesin membawa sebagian leluconnya:
   "my human" menempatkan AI sebagai pihak yang punya manusia,
   dan "cover for me" adalah bahasa kerja yang diucapkan mesin
   tentang dirinya sendiri.
3. Fit -- baris ini tetap terbaca sebagai satu auto-reply sungguhan
   yang akan diterima seseorang: pembuka "Out of office:", satu
   kalimat utuh, nada sopan-datar, tanpa meta-komentar tentang
   kompetisi.
4. Freshness -- menghindari klise yang disebut juri (beach, inbox,
   back soon): tidak ada pantai, tidak ada "inbox", tidak ada
   janji "back soon". Leluconnya berasal dari logika mesin
   (delegasi rekursif), bukan dari stok frasa liburan.

Kandidat yang kalah (brainstorm, ditulis dari nol, bukan salinan):
  - "I am on vacation. I left my auto-reply in charge, and it
    immediately filed for vacation too." (92 karakter) -- rekursi
    serupa tapi punchline-nya lebih mudah ditebak.
  - "Out of office: my human went on holiday, so I went on strike.
    Your message is now being ignored by two intelligences."
    (117 karakter) -- "on strike" terasa seperti keluhan, bukan
    auto-reply; punchline-nya menjelaskan leluconnya sendiri.

Optimasi: program ini deterministik dan tanpa dependensi --
stdlib Python 3.13 saja, tanpa network dan tanpa random, jadi
output-nya byte-identik di setiap run. Validasi di dalam program
menegakkan gate resmi (UTF-8, 1-160 karakter, satu baris, bukan
hanya spasi) sebelum file ditulis, sehingga entry yang lolos gate
adalah satu-satunya yang bisa dihasilkan.

Cara kerja: main() menulis baris konstanta ENTRY ke
/output/entry.txt (atau ke direktori yang ditunjuk env
OUTPUT_DIR bila harness memintanya), lalu memvalidasi ulang isi
file yang tertulis: persis satu baris, 1-160 karakter, dan sama
dengan konstanta. Bila validasi gagal, program keluar non-zero
dan tidak meninggalkan file setengah jadi.
"""

from __future__ import annotations

import os
import sys

# The entry: one original out-of-office auto-reply, 108 characters.
ENTRY = (
    "Out of office: I asked my human to cover for me, "
    "but they asked me to cover for them. Neither of us is here."
)

MAX_CHARS = 160


def validate(text: str) -> None:
    """Enforce the official gate: UTF-8, 1-160 chars, one line."""
    if not text or text != text.strip() or text.isspace():
        raise ValueError("entry must be non-empty, non-whitespace text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(ENTRY)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Re-read what was written and validate the artifact itself: the
    # file must be exactly the entry plus one trailing newline — a
    # splitlines check alone would also accept a missing newline.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY + "\n":
        raise ValueError("written entry.txt must be exactly the entry plus one newline")
    validate(written.rstrip("\n"))
    print(f"Wrote {path} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
