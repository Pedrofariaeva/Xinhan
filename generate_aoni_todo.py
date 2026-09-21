#!/usr/bin/env python3
"""Build the bilingual Meeting Report (Aoni Zhang & Pedro Faria, September 2026) from the editable txt.

Usage:
    python3 generate_meetingreport_202609.py

Reads:  uncoveredDocs/V20260920/meetingReport_2026-09_content_v3.txt
Writes: uncoveredDocs/V20260920/meetingReport_2026-09_Aoni_Pedro_Bilingual_v3.docx
        uncoveredDocs/V20260920/meetingReport_2026-09_Aoni_Pedro_Bilingual_v3.pdf

Same tags and same look as the week report: the builder in generate_weekreport_20260915.py is
reused as it is, only the paths change. To make a v3, copy the content file to _v3 and change VERSION below.
"""

from pathlib import Path

import generate_weekreport_20260915 as g

DIR = Path(__file__).parent / "uncoveredDocs" / "V20260920"

g.DIR = DIR
g.PHOTOS = DIR / "photos"
VERSION = "v3"   # v1 files stay untouched; change this to make v3
g.SRC = DIR / "aoniTodo_2026-09_content.txt"
g.DOCX_OUT = DIR / "aoniTodo_2026-09_Aoni.docx"
g.PDF_OUT = DIR / "aoniTodo_2026-09_Aoni.pdf"

if __name__ == "__main__":
    g.build_docx()
    g.build_pdf()
