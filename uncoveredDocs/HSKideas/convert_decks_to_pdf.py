#!/usr/bin/env python3
"""Convert HTML lesson decks to A4 PDFs using Playwright."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

DECKS = [
    Path("/Users/pedro/Documents/GitHub/Xinhan/uncoveredDocs/HSKideas/11 friends/gong-zuo-lesson-deck.html"),
    Path("/Users/pedro/Documents/GitHub/Xinhan/uncoveredDocs/HSKideas/12 Coffee luckyinCoffee/rui-xing-ka-pei-lesson-deck.html"),
    Path("/Users/pedro/Documents/GitHub/Xinhan/uncoveredDocs/HSKideas/13 banjia/ban-jia-lesson-deck.html"),
    Path("/Users/pedro/Documents/GitHub/Xinhan/uncoveredDocs/HSKideas/14 mood and weather/xin-qing-tian-qi-lesson-deck.html"),
    Path("/Users/pedro/Documents/GitHub/Xinhan/uncoveredDocs/HSKideas/16 Mood and Weather/xin-qing-he-tian-qi-lesson-deck.html"),
    Path("/Users/pedro/Documents/GitHub/Xinhan/uncoveredDocs/HSKideas/15 Many Ways to Say It/many-ways-to-say-it-hsk3-lesson-deck.html"),
]


async def html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f"file://{html_path.resolve()}", wait_until="networkidle")
        # Give fonts a moment to settle.
        await page.wait_for_timeout(500)
        await page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        await browser.close()


async def main() -> None:
    for html_path in DECKS:
        if not html_path.exists():
            print(f"Skipping missing file: {html_path}")
            continue
        pdf_path = html_path.with_suffix(".pdf")
        print(f"Converting {html_path.name} → {pdf_path.name}")
        await html_to_pdf(html_path, pdf_path)
        print(f"  Saved {pdf_path}")


if __name__ == "__main__":
    asyncio.run(main())
