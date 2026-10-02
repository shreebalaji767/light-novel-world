import re

from app import app
from generator.novel import CHAPTER_COUNT, CHAPTER_WORD_COUNT, generate_chapter, generate_novel


def test_novel_has_expected_structure():
    novel = generate_novel()

    assert novel["seed"]
    assert re.fullmatch(r"[0-9a-f]{64}", novel["seed"])
    assert novel["chapter_count"] == CHAPTER_COUNT
    assert len(novel["arcs"]) == 15
    assert len(novel["blueprint"]["chapter_roadmap"]) == CHAPTER_COUNT


def test_chapter_is_deterministic_and_exact_length():
    seed = "a" * 64

    first = generate_chapter(seed, 1)
    second = generate_chapter(seed, 1)

    assert first == second
    assert first["number"] == 1
    assert first["word_count"] == CHAPTER_WORD_COUNT


def test_last_chapter_is_valid():
    chapter = generate_chapter("b" * 64, CHAPTER_COUNT)

    assert chapter["number"] == CHAPTER_COUNT
    assert chapter["word_count"] == CHAPTER_WORD_COUNT


def test_api_rejects_invalid_seed_and_chapter():
    client = app.test_client()

    assert client.get("/api/chapter/not-a-seed/1").status_code == 404
    assert client.get(f"/api/chapter/{'a' * 64}/0").status_code == 404
    assert client.get(f"/api/chapter/{'a' * 64}/{CHAPTER_COUNT + 1}").status_code == 404


def test_api_chapter_is_cacheable():
    client = app.test_client()

    response = client.get(f"/api/chapter/{'a' * 64}/1")

    assert response.status_code == 200
    assert response.headers["Cache-Control"] == "public, max-age=3600"
