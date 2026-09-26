from flask import Flask, render_template, jsonify, abort
from generator.novel import (
    CHAPTER_COUNT,
    generate_novel,
    generate_chapter,
)

app = Flask(__name__)


@app.get("/")
def home():
    """
    Every request generates a completely new novel seed.

    No database.
    No localStorage.
    No sessionStorage.
    No cookies are used for novel generation.
    """
    novel = generate_novel()
    return render_template("novel.html", novel=novel)


@app.get("/api/novel")
def api_novel():
    """
    Generate a completely new novel.
    """
    novel = generate_novel()
    return jsonify(novel)


@app.get("/api/chapter/<seed>/<int:chapter_number>")
def api_chapter(seed: str, chapter_number: int):
    """
    Generate one deterministic chapter belonging to the supplied novel seed.
    """
    if not seed:
        abort(404)

    if chapter_number < 1 or chapter_number > CHAPTER_COUNT:
        abort(404)

    chapter = generate_chapter(seed, chapter_number)
    return jsonify(chapter)


@app.get("/health")
def health():
    return jsonify(
        {
            "status": "ok",
            "service": "light-novel-world",
            "chapters_per_novel": CHAPTER_COUNT,
            "storage": "none",
            "novel_on_refresh": True,
            "responsive": True,
        }
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
