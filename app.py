import os
import re

from flask import Flask, abort, jsonify, render_template, request

from generator.novel import (
    CHAPTER_COUNT,
    GENRES,
    generate_chapter,
    generate_novel,
)

app = Flask(__name__)

# Seeds are generated with secrets.token_hex(32), so valid seeds are
# exactly 64 hexadecimal characters. Reject malformed values before they
# reach the generator.
SEED_PATTERN = re.compile(r"^[0-9a-fA-F]{64}$")


def is_valid_seed(seed: str) -> bool:
    return bool(SEED_PATTERN.fullmatch(seed))


def selected_genre(value: str | None) -> str | None:
    if not value:
        return None
    normalized = value.strip().casefold()
    return next((genre for genre in GENRES if genre.casefold() == normalized), None)


def selected_parody(value: str | None) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


@app.get("/")
def home():
    """Render a new novel using optional genre/parody selections."""
    genre = selected_genre(request.args.get("genre"))
    parody = selected_parody(request.args.get("parody"))
    return render_template(
        "novel.html",
        novel=generate_novel(genre=genre, parody=parody),
        genres=GENRES,
    )


@app.get("/api/novel")
def api_novel():
    """Generate a new novel using optional genre/parody selections."""
    genre = selected_genre(request.args.get("genre"))
    parody = selected_parody(request.args.get("parody"))
    response = jsonify(generate_novel(genre=genre, parody=parody))
    response.headers["Cache-Control"] = "no-store"
    return response


@app.get("/api/chapter/<seed>/<int:chapter_number>")
def api_chapter(seed: str, chapter_number: int):
    """Return one deterministic chapter for a valid novel seed."""
    if not is_valid_seed(seed):
        abort(404)

    if not 1 <= chapter_number <= CHAPTER_COUNT:
        abort(404)

    chapter = generate_chapter(seed, chapter_number)
    response = jsonify(chapter)

    # The chapter is deterministic for this seed + number, so it is safe
    # for browsers/proxies to cache it for a short period.
    response.headers["Cache-Control"] = "public, max-age=3600"

    return response


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
    debug = os.getenv("FLASK_DEBUG", "0").lower() in {
        "1",
        "true",
        "yes",
        "on",
    }

    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=debug,
    )
