from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from generator.novel import (
    CHAPTER_COUNT,
    CHAPTER_WORD_COUNT,
    GENRES,
    generate_chapter,
    generate_novel,
)


ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
TEMPLATE_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"

DEFAULT_NOVEL_COUNT = 4

PARODY_GENRE_POOL = [
    "Isekai",
    "Cultivation Parody",
    "Academy Parody",
    "System Parody",
    "Fantasy Parody",
    "Villain Parody",
    "Hero Parody",
    "Chaotic Comedy",
]


def env_int(name: str, default: int) -> int:
    try:
        return max(1, int(os.getenv(name, str(default))))
    except ValueError:
        return default


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


def build_novel(environment: Environment, number: int, genre: str) -> dict:
    novel = generate_novel(genre=genre, parody=True)

    folder = SITE / f"novel-{number:03d}"
    chapters_dir = folder / "chapters"
    folder.mkdir(parents=True, exist_ok=True)
    chapters_dir.mkdir(parents=True, exist_ok=True)

    # Keep the complete blueprint available to the static reader.
    write_json(folder / "novel.json", novel)

    print(
        f"[{number}] {novel['title']} | {genre} | "
        f"{CHAPTER_COUNT} chapters x {CHAPTER_WORD_COUNT} words"
    )

    for chapter_number in range(1, CHAPTER_COUNT + 1):
        chapter = generate_chapter(novel["seed"], chapter_number)
        expected = CHAPTER_WORD_COUNT

        if chapter["word_count"] != expected:
            raise RuntimeError(
                f"Chapter {chapter_number} generated "
                f"{chapter['word_count']} words; expected {expected}"
            )

        write_json(
            chapters_dir / f"{chapter_number:03d}.json",
            chapter,
        )

        if chapter_number % 50 == 0 or chapter_number == CHAPTER_COUNT:
            print(f"    generated {chapter_number}/{CHAPTER_COUNT}")

    # The existing Jinja page is retained, but its chapter loader is
    # switched to local JSON by the build-time template configuration.
    html = environment.get_template("novel.html").render(
        novel=novel,
        genres=GENRES,
        static_site=True,
        static_chapter_path="chapters",
    )
    (folder / "index.html").write_text(html, encoding="utf-8")

    return {
        "id": f"novel-{number:03d}",
        "path": f"novel-{number:03d}/index.html",
        "title": novel["title"],
        "author": novel["author"],
        "genre": novel["genre"],
        "secondary_genre": novel["secondary_genre"],
        "tone": novel["tone"],
        "synopsis": novel["synopsis"],
        "seed": novel["seed"],
        "chapter_count": novel["chapter_count"],
        "parody_mode": True,
    }


def build_catalog(catalog: list[dict]) -> None:
    cards = []
    for item in catalog:
        cards.append(
            f"""
            <article class="card">
              <div class="tag">{item['genre']}</div>
              <h2>{item['title']}</h2>
              <p>{item['synopsis']}</p>
              <div class="meta">
                {item['chapter_count']} chapters · {item['tone']} · PARODY
              </div>
              <a class="button" href="{item['path']}">Read Novel →</a>
            </article>
            """
        )

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Light Novel World — Parody Library</title>
<meta name="description" content="A Python-generated static library of absurd parody light novels.">
<style>
:root {{
  color-scheme: dark;
  --bg:#090b12; --surface:#111522; --border:#293044;
  --text:#f4f6fb; --muted:#aab2c5; --accent:#9b7cff;
}}
* {{ box-sizing:border-box; }}
body {{
  margin:0; min-height:100vh; font-family:Inter,system-ui,sans-serif;
  background:radial-gradient(circle at top,#1a1530 0,#090b12 45%);
  color:var(--text);
}}
main {{ width:min(1180px,calc(100% - 32px)); margin:auto; padding:72px 0; }}
.hero {{ text-align:center; margin-bottom:48px; }}
.badge {{ display:inline-block; padding:7px 12px; border:1px solid var(--border);
  border-radius:999px; color:#cfc5ff; font-size:12px; letter-spacing:.12em; }}
h1 {{ font-size:clamp(42px,8vw,84px); line-height:.95; margin:18px 0; }}
.hero p {{ max-width:720px; margin:auto; color:var(--muted); font-size:18px; line-height:1.7; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:18px; }}
.card {{ background:rgba(17,21,34,.88); border:1px solid var(--border);
  border-radius:20px; padding:24px; box-shadow:0 18px 50px rgba(0,0,0,.22); }}
.tag {{ color:#bcaaff; font-size:12px; text-transform:uppercase; letter-spacing:.12em; }}
.card h2 {{ font-size:26px; margin:12px 0; }}
.card p {{ color:var(--muted); line-height:1.65; min-height:110px; }}
.meta {{ color:#7f89a0; font-size:13px; margin:16px 0; }}
.button {{ display:inline-block; padding:12px 16px; border-radius:12px;
  background:var(--accent); color:white; text-decoration:none; font-weight:700; }}
footer {{ text-align:center; color:var(--muted); margin-top:42px; }}
</style>
</head>
<body>
<main>
<section class="hero">
  <span class="badge">PYTHON · STATIC · PARODY</span>
  <h1>Light Novel World</h1>
  <p>
    No server-side chapter generation. No database. No API.
    Python generates the novels at build time, then the browser simply reads
    the finished story files.
  </p>
</section>
<section class="grid">
{''.join(cards)}
</section>
<footer>{len(catalog)} pre-generated parody novels · {CHAPTER_COUNT} chapters each</footer>
</main>
</body>
</html>
"""
    (SITE / "index.html").write_text(html, encoding="utf-8")
    write_json(SITE / "catalog.json", catalog)


def main() -> None:
    count = env_int("NOVEL_COUNT", DEFAULT_NOVEL_COUNT)

    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)

    environment = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )

    catalog = []
    for number in range(1, count + 1):
        genre = PARODY_GENRE_POOL[(number - 1) % len(PARODY_GENRE_POOL)]
        catalog.append(build_novel(environment, number, genre))

    build_catalog(catalog)

    # Copy the site's stylesheet for any pages that reference it.
    source_css = STATIC_DIR / "css" / "style.css"
    if source_css.exists():
        (SITE / "static" / "css").mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_css, SITE / "static" / "css" / "style.css")

    print("")
    print(f"BUILD COMPLETE: {count} parody novels")
    print(f"OUTPUT: {SITE}")
    print("No Flask server is required to serve the generated site.")


if __name__ == "__main__":
    main()
