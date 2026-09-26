(() => {
    "use strict";

    const config = window.NOVEL_CONFIG;

    let currentChapter = 1;

    const chapterTitle =
        document.getElementById("chapterTitle");

    const chapterBody =
        document.getElementById("chapterBody");

    const chapterPosition =
        document.getElementById("chapterPosition");

    const chapterArc =
        document.getElementById("chapterArc");

    const chapterLocation =
        document.getElementById("chapterLocation");

    const progressBar =
        document.getElementById("progressBar");

    const previousChapter =
        document.getElementById("previousChapter");

    const nextChapter =
        document.getElementById("nextChapter");

    const previousChapterBottom =
        document.getElementById("previousChapterBottom");

    const nextChapterBottom =
        document.getElementById("nextChapterBottom");

    const startReading =
        document.getElementById("startReading");

    const randomChapter =
        document.getElementById("randomChapter");

    const newNovelButton =
        document.getElementById("newNovelButton");

    const finalNewNovel =
        document.getElementById("finalNewNovel");


    function escapeHtml(value) {
        const div = document.createElement("div");
        div.textContent = value;
        return div.innerHTML;
    }


    async function loadChapter(number, scroll = true) {
        if (number < 1) {
            number = 1;
        }

        if (number > config.chapterCount) {
            number = config.chapterCount;
        }

        currentChapter = number;

        chapterTitle.textContent = "Loading Chapter...";
        chapterBody.innerHTML = `
            <div class="loading">
                <span></span>
                <span></span>
                <span></span>
            </div>
        `;

        try {
            const response = await fetch(
                `/api/chapter/${encodeURIComponent(config.seed)}/${number}`,
                {
                    headers: {
                        "Accept": "application/json"
                    }
                }
            );

            if (!response.ok) {
                throw new Error("Chapter request failed");
            }

            const chapter = await response.json();

            chapterTitle.textContent =
                chapter.title;

            chapterPosition.textContent =
                `Chapter ${String(chapter.number).padStart(3, "0")}`;

            chapterArc.textContent =
                `ARC ${String(chapter.arc.number).padStart(2, "0")} · ${chapter.arc.title}`;

            chapterLocation.textContent =
                chapter.location;

            chapterBody.innerHTML =
                chapter.paragraphs
                    .map(
                        paragraph =>
                            `<p>${formatText(paragraph)}</p>`
                    )
                    .join("");

            const percentage =
                (chapter.number / config.chapterCount) * 100;

            progressBar.style.width =
                `${percentage}%`;

            updateButtons();

            if (scroll) {
                document
                    .getElementById("chapters")
                    .scrollIntoView({
                        behavior: "smooth",
                        block: "start"
                    });
            }

            document.title =
                `${chapter.title} — Light Novel World`;

        } catch (error) {
            chapterBody.innerHTML = `
                <div class="error-box">
                    <h3>Chapter unavailable</h3>
                    <p>
                        The chapter could not be generated.
                        Please try again.
                    </p>
                </div>
            `;
        }
    }


    function formatText(text) {
        return escapeHtml(text)
            .replace(
                /\*\*(.*?)\*\*/g,
                "<strong>$1</strong>"
            );
    }


    function updateButtons() {
        const atBeginning =
            currentChapter <= 1;

        const atEnd =
            currentChapter >= config.chapterCount;

        previousChapter.disabled =
            atBeginning;

        previousChapterBottom.disabled =
            atBeginning;

        nextChapter.disabled =
            atEnd;

        nextChapterBottom.disabled =
            atEnd;
    }


    function next() {
        if (currentChapter < config.chapterCount) {
            loadChapter(currentChapter + 1);
        }
    }


    function previous() {
        if (currentChapter > 1) {
            loadChapter(currentChapter - 1);
        }
    }


    function newNovel() {
        window.location.href = "/";
    }


    previousChapter.addEventListener(
        "click",
        previous
    );

    previousChapterBottom.addEventListener(
        "click",
        previous
    );

    nextChapter.addEventListener(
        "click",
        next
    );

    nextChapterBottom.addEventListener(
        "click",
        next
    );

    startReading.addEventListener(
        "click",
        () => loadChapter(1)
    );

    randomChapter.addEventListener(
        "click",
        () => {
            const number =
                Math.floor(
                    Math.random() * config.chapterCount
                ) + 1;

            loadChapter(number);
        }
    );

    newNovelButton.addEventListener(
        "click",
        newNovel
    );

    finalNewNovel.addEventListener(
        "click",
        newNovel
    );


    document
        .querySelectorAll(".arc-button")
        .forEach(button => {

            button.addEventListener(
                "click",
                () => {

                    const start =
                        Number(button.dataset.start);

                    loadChapter(start);

                }
            );

        });


    document.addEventListener(
        "keydown",
        event => {

            if (
                event.target.tagName === "INPUT" ||
                event.target.tagName === "TEXTAREA"
            ) {
                return;
            }

            if (event.key === "ArrowRight") {
                next();
            }

            if (event.key === "ArrowLeft") {
                previous();
            }

            if (event.key.toLowerCase() === "n") {
                newNovel();
            }

        }
    );


    loadChapter(1, false);

})();
