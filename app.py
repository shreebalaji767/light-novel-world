from flask import Flask, render_template, jsonify, request, abort
from generator.novel import generate_novel, generate_chapter

app = Flask(__name__)


@app.get("/")
def home():
    novel = generate_novel()
    return render_template("novel.html", novel=novel)


@app.get("/api/novel")
def api_novel():
    novel = generate_novel()
    return jsonify(novel)


@app.get("/api/chapter/<seed>/<int:chapter_number>")
def api_chapter(seed: str, chapter_number: int):
    if chapter_number < 1 or chapter_number > 600:
        abort(404)

    chapter = generate_chapter(seed, chapter_number)
    return jsonify(chapter)


@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "light-novel-world",
        "chapters_per_novel": 600,
        "storage": "none"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
