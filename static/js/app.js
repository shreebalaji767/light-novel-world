(function () {
    "use strict";

    const config = window.NOVEL_CONFIG || {};

    const seed = String(config.seed || "");
    const chapterCount = Number(config.chapterCount || 600);

    let currentChapter = 1;
    let loading = false;


    const elements = {
        chapterPosition: document.getElementById("chapterPosition"),
        chapterArc: document.getElementById("chapterArc"),
        chapterLocation: document.getElementById("chapterLocation"),
        chapterTitle: document.getElementById("chapterTitle"),
        chapterBody: document.getElementById("chapterBody"),
        progressBar: document.getElementById("progressBar"),

        previousChapter: document.getElementById("previousChapter"),
        nextChapter: document.getElementById("nextChapter"),

        previousChapterBottom:
            document.getElementById("previousChapterBottom"),

        nextChapterBottom:
            document.getElementById("nextChapterBottom"),

        startReading:
            document.getElementById("startReading"),

        randomChapter:
            document.getElementById("randomChapter"),

        newNovelButton:
            document.getElementById("newNovelButton"),

        finalNewNovel:
            document.getElementById("finalNewNovel"),

        chapterList:
            document.getElementById("chapterList"),
    };


    function setButtonState(button, disabled) {
        if (!button) {
            return;
        }

        button.disabled = disabled;
    }


    function updateNavigation() {
        const atBeginning = currentChapter <= 1;
        const atEnd = currentChapter >= chapterCount;

        setButtonState(
            elements.previousChapter,
            atBeginning || loading
        );

        setButtonState(
            elements.previousChapterBottom,
            atBeginning || loading
        );

        setButtonState(
            elements.nextChapter,
            atEnd || loading
        );

        setButtonState(
            elements.nextChapterBottom,
            atEnd || loading
        );
    }


    function updateProgress() {
        const percentage =
            (currentChapter / chapterCount) * 100;

        if (elements.progressBar) {
            elements.progressBar.style.width =
                `${Math.min(100, percentage)}%`;
        }
    }


    function clearChapter() {
        if (elements.chapterBody) {
            elements.chapterBody.innerHTML = "";
        }

        if (elements.chapterTitle) {
            elements.chapterTitle.textContent =
                "Loading Chapter...";
        }
    }


    function renderChapter(chapter) {
        if (!chapter) {
            return;
        }

        currentChapter = Number(chapter.number) || 1;

        if (elements.chapterPosition) {
            elements.chapterPosition.textContent =
                `Chapter ${String(currentChapter).padStart(3, "0")}`;
        }

        if (elements.chapterArc) {
            elements.chapterArc.textContent =
                chapter.arc?.title || "STORY";
        }

        if (elements.chapterLocation) {
            elements.chapterLocation.textContent =
                chapter.location || "UNKNOWN";
        }

        if (elements.chapterTitle) {
            elements.chapterTitle.textContent =
                chapter.title || `Chapter ${currentChapter}`;
        }

        if (elements.chapterBody) {
            elements.chapterBody.innerHTML = "";

            const paragraphs =
                Array.isArray(chapter.paragraphs)
                    ? chapter.paragraphs
                    : [];

            paragraphs.forEach(function (paragraph) {
                const p = document.createElement("p");

                p.textContent = paragraph;

                elements.chapterBody.appendChild(p);
            });
        }

        updateProgress();
        updateNavigation();

        if (elements.chapterPosition) {
            elements.chapterPosition.scrollIntoView({
                behavior: "smooth",
                block: "nearest"
            });
        }
    }


    async function loadChapter(number) {
        if (loading) {
            return;
        }

        if (number < 1 || number > chapterCount) {
            return;
        }

        if (!seed) {
            return;
        }

        loading = true;

        updateNavigation();

        clearChapter();

        try {
            const response = await fetch(
                `/api/chapter/${encodeURIComponent(seed)}/${number}`,
                {
                    method: "GET",
                    headers: {
                        "Accept": "application/json"
                    },
                    cache: "no-store"
                }
            );

            if (!response.ok) {
                throw new Error(
                    `Chapter request failed: ${response.status}`
                );
            }

            const chapter = await response.json();

            renderChapter(chapter);

        } catch (error) {
            console.error(error);

            if (elements.chapterTitle) {
                elements.chapterTitle.textContent =
                    "Unable to load chapter";
            }

            if (elements.chapterBody) {
                elements.chapterBody.innerHTML = "";

                const message =
                    document.createElement("p");

                message.textContent =
                    "Something went wrong while loading this chapter. Please try again.";

                elements.chapterBody.appendChild(message);
            }

        } finally {
            loading = false;

            updateNavigation();
        }
    }


    function goToChapter(number) {
        loadChapter(number);

        const reader =
            document.getElementById("chapters");

        if (reader) {
            reader.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }
    }


    function newNovel() {
        /*
         * Do not store anything locally.
         *
         * A normal navigation request reaches Flask /,
         * which creates a new cryptographically random seed.
         */
        window.location.href = "/";
    }


    function randomChapter() {
        const number =
            Math.floor(Math.random() * chapterCount) + 1;

        goToChapter(number);
    }


    if (elements.previousChapter) {
        elements.previousChapter.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter - 1);
            }
        );
    }


    if (elements.nextChapter) {
        elements.nextChapter.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter + 1);
            }
        );
    }


    if (elements.previousChapterBottom) {
        elements.previousChapterBottom.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter - 1);
            }
        );
    }


    if (elements.nextChapterBottom) {
        elements.nextChapterBottom.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter + 1);
            }
        );
    }


    if (elements.startReading) {
        elements.startReading.addEventListener(
            "click",
            function () {
                goToChapter(1);
            }
        );
    }


    if (elements.randomChapter) {
        elements.randomChapter.addEventListener(
            "click",
            function () {
                randomChapter();
            }
        );
    }


    if (elements.newNovelButton) {
        elements.newNovelButton.addEventListener(
            "click",
            newNovel
        );
    }


    if (elements.finalNewNovel) {
        elements.finalNewNovel.addEventListener(
            "click",
            newNovel
        );
    }


    if (elements.chapterList) {
        const arcButtons =
            elements.chapterList.querySelectorAll(
                ".arc-button"
            );

        arcButtons.forEach(function (button) {
            button.addEventListener(
                "click",
                function () {
                    const start =
                        Number(button.dataset.start);

                    if (Number.isInteger(start)) {
                        goToChapter(start);
                    }
                }
            );
        });
    }


    /*
     * Keyboard navigation.
     */
    document.addEventListener(
        "keydown",
        function (event) {

            const tag =
                document.activeElement?.tagName;

            if (
                tag === "INPUT" ||
                tag === "TEXTAREA" ||
                tag === "SELECT"
            ) {
                return;
            }

            if (event.key === "ArrowLeft") {
                goToChapter(currentChapter - 1);
            }

            if (event.key === "ArrowRight") {
                goToChapter(currentChapter + 1);
            }
        }
    );


    /*
     * Load Chapter 1 automatically.
     */
    loadChapter(1);

})();(function () {
    "use strict";

    const config = window.NOVEL_CONFIG || {};

    const seed = String(config.seed || "");
    const chapterCount = Number(config.chapterCount || 600);

    let currentChapter = 1;
    let loading = false;


    const elements = {
        chapterPosition: document.getElementById("chapterPosition"),
        chapterArc: document.getElementById("chapterArc"),
        chapterLocation: document.getElementById("chapterLocation"),
        chapterTitle: document.getElementById("chapterTitle"),
        chapterBody: document.getElementById("chapterBody"),
        progressBar: document.getElementById("progressBar"),

        previousChapter: document.getElementById("previousChapter"),
        nextChapter: document.getElementById("nextChapter"),

        previousChapterBottom:
            document.getElementById("previousChapterBottom"),

        nextChapterBottom:
            document.getElementById("nextChapterBottom"),

        startReading:
            document.getElementById("startReading"),

        randomChapter:
            document.getElementById("randomChapter"),

        newNovelButton:
            document.getElementById("newNovelButton"),

        finalNewNovel:
            document.getElementById("finalNewNovel"),

        chapterList:
            document.getElementById("chapterList"),
    };


    function setButtonState(button, disabled) {
        if (!button) {
            return;
        }

        button.disabled = disabled;
    }


    function updateNavigation() {
        const atBeginning = currentChapter <= 1;
        const atEnd = currentChapter >= chapterCount;

        setButtonState(
            elements.previousChapter,
            atBeginning || loading
        );

        setButtonState(
            elements.previousChapterBottom,
            atBeginning || loading
        );

        setButtonState(
            elements.nextChapter,
            atEnd || loading
        );

        setButtonState(
            elements.nextChapterBottom,
            atEnd || loading
        );
    }


    function updateProgress() {
        const percentage =
            (currentChapter / chapterCount) * 100;

        if (elements.progressBar) {
            elements.progressBar.style.width =
                `${Math.min(100, percentage)}%`;
        }
    }


    function clearChapter() {
        if (elements.chapterBody) {
            elements.chapterBody.innerHTML = "";
        }

        if (elements.chapterTitle) {
            elements.chapterTitle.textContent =
                "Loading Chapter...";
        }
    }


    function renderChapter(chapter) {
        if (!chapter) {
            return;
        }

        currentChapter = Number(chapter.number) || 1;

        if (elements.chapterPosition) {
            elements.chapterPosition.textContent =
                `Chapter ${String(currentChapter).padStart(3, "0")}`;
        }

        if (elements.chapterArc) {
            elements.chapterArc.textContent =
                chapter.arc?.title || "STORY";
        }

        if (elements.chapterLocation) {
            elements.chapterLocation.textContent =
                chapter.location || "UNKNOWN";
        }

        if (elements.chapterTitle) {
            elements.chapterTitle.textContent =
                chapter.title || `Chapter ${currentChapter}`;
        }

        if (elements.chapterBody) {
            elements.chapterBody.innerHTML = "";

            const paragraphs =
                Array.isArray(chapter.paragraphs)
                    ? chapter.paragraphs
                    : [];

            paragraphs.forEach(function (paragraph) {
                const p = document.createElement("p");

                p.textContent = paragraph;

                elements.chapterBody.appendChild(p);
            });
        }

        updateProgress();
        updateNavigation();

        if (elements.chapterPosition) {
            elements.chapterPosition.scrollIntoView({
                behavior: "smooth",
                block: "nearest"
            });
        }
    }


    async function loadChapter(number) {
        if (loading) {
            return;
        }

        if (number < 1 || number > chapterCount) {
            return;
        }

        if (!seed) {
            return;
        }

        loading = true;

        updateNavigation();

        clearChapter();

        try {
            const response = await fetch(
                `/api/chapter/${encodeURIComponent(seed)}/${number}`,
                {
                    method: "GET",
                    headers: {
                        "Accept": "application/json"
                    },
                    cache: "no-store"
                }
            );

            if (!response.ok) {
                throw new Error(
                    `Chapter request failed: ${response.status}`
                );
            }

            const chapter = await response.json();

            renderChapter(chapter);

        } catch (error) {
            console.error(error);

            if (elements.chapterTitle) {
                elements.chapterTitle.textContent =
                    "Unable to load chapter";
            }

            if (elements.chapterBody) {
                elements.chapterBody.innerHTML = "";

                const message =
                    document.createElement("p");

                message.textContent =
                    "Something went wrong while loading this chapter. Please try again.";

                elements.chapterBody.appendChild(message);
            }

        } finally {
            loading = false;

            updateNavigation();
        }
    }


    function goToChapter(number) {
        loadChapter(number);

        const reader =
            document.getElementById("chapters");

        if (reader) {
            reader.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }
    }


    function newNovel() {
        /*
         * Do not store anything locally.
         *
         * A normal navigation request reaches Flask /,
         * which creates a new cryptographically random seed.
         */
        window.location.href = "/";
    }


    function randomChapter() {
        const number =
            Math.floor(Math.random() * chapterCount) + 1;

        goToChapter(number);
    }


    if (elements.previousChapter) {
        elements.previousChapter.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter - 1);
            }
        );
    }


    if (elements.nextChapter) {
        elements.nextChapter.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter + 1);
            }
        );
    }


    if (elements.previousChapterBottom) {
        elements.previousChapterBottom.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter - 1);
            }
        );
    }


    if (elements.nextChapterBottom) {
        elements.nextChapterBottom.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter + 1);
            }
        );
    }


    if (elements.startReading) {
        elements.startReading.addEventListener(
            "click",
            function () {
                goToChapter(1);
            }
        );
    }


    if (elements.randomChapter) {
        elements.randomChapter.addEventListener(
            "click",
            function () {
                randomChapter();
            }
        );
    }


    if (elements.newNovelButton) {
        elements.newNovelButton.addEventListener(
            "click",
            newNovel
        );
    }


    if (elements.finalNewNovel) {
        elements.finalNewNovel.addEventListener(
            "click",
            newNovel
        );
    }


    if (elements.chapterList) {
        const arcButtons =
            elements.chapterList.querySelectorAll(
                ".arc-button"
            );

        arcButtons.forEach(function (button) {
            button.addEventListener(
                "click",
                function () {
                    const start =
                        Number(button.dataset.start);

                    if (Number.isInteger(start)) {
                        goToChapter(start);
                    }
                }
            );
        });
    }


    /*
     * Keyboard navigation.
     */
    document.addEventListener(
        "keydown",
        function (event) {

            const tag =
                document.activeElement?.tagName;

            if (
                tag === "INPUT" ||
                tag === "TEXTAREA" ||
                tag === "SELECT"
            ) {
                return;
            }

            if (event.key === "ArrowLeft") {
                goToChapter(currentChapter - 1);
            }

            if (event.key === "ArrowRight") {
                goToChapter(currentChapter + 1);
            }
        }
    );


    /*
     * Load Chapter 1 automatically.
     */
    loadChapter(1);

})();(function () {
    "use strict";

    const config = window.NOVEL_CONFIG || {};

    const seed = String(config.seed || "");
    const chapterCount = Number(config.chapterCount || 600);

    let currentChapter = 1;
    let loading = false;


    const elements = {
        chapterPosition: document.getElementById("chapterPosition"),
        chapterArc: document.getElementById("chapterArc"),
        chapterLocation: document.getElementById("chapterLocation"),
        chapterTitle: document.getElementById("chapterTitle"),
        chapterBody: document.getElementById("chapterBody"),
        progressBar: document.getElementById("progressBar"),

        previousChapter: document.getElementById("previousChapter"),
        nextChapter: document.getElementById("nextChapter"),

        previousChapterBottom:
            document.getElementById("previousChapterBottom"),

        nextChapterBottom:
            document.getElementById("nextChapterBottom"),

        startReading:
            document.getElementById("startReading"),

        randomChapter:
            document.getElementById("randomChapter"),

        newNovelButton:
            document.getElementById("newNovelButton"),

        finalNewNovel:
            document.getElementById("finalNewNovel"),

        chapterList:
            document.getElementById("chapterList"),
    };


    function setButtonState(button, disabled) {
        if (!button) {
            return;
        }

        button.disabled = disabled;
    }


    function updateNavigation() {
        const atBeginning = currentChapter <= 1;
        const atEnd = currentChapter >= chapterCount;

        setButtonState(
            elements.previousChapter,
            atBeginning || loading
        );

        setButtonState(
            elements.previousChapterBottom,
            atBeginning || loading
        );

        setButtonState(
            elements.nextChapter,
            atEnd || loading
        );

        setButtonState(
            elements.nextChapterBottom,
            atEnd || loading
        );
    }


    function updateProgress() {
        const percentage =
            (currentChapter / chapterCount) * 100;

        if (elements.progressBar) {
            elements.progressBar.style.width =
                `${Math.min(100, percentage)}%`;
        }
    }


    function clearChapter() {
        if (elements.chapterBody) {
            elements.chapterBody.innerHTML = "";
        }

        if (elements.chapterTitle) {
            elements.chapterTitle.textContent =
                "Loading Chapter...";
        }
    }


    function renderChapter(chapter) {
        if (!chapter) {
            return;
        }

        currentChapter = Number(chapter.number) || 1;

        if (elements.chapterPosition) {
            elements.chapterPosition.textContent =
                `Chapter ${String(currentChapter).padStart(3, "0")}`;
        }

        if (elements.chapterArc) {
            elements.chapterArc.textContent =
                chapter.arc?.title || "STORY";
        }

        if (elements.chapterLocation) {
            elements.chapterLocation.textContent =
                chapter.location || "UNKNOWN";
        }

        if (elements.chapterTitle) {
            elements.chapterTitle.textContent =
                chapter.title || `Chapter ${currentChapter}`;
        }

        if (elements.chapterBody) {
            elements.chapterBody.innerHTML = "";

            const paragraphs =
                Array.isArray(chapter.paragraphs)
                    ? chapter.paragraphs
                    : [];

            paragraphs.forEach(function (paragraph) {
                const p = document.createElement("p");

                p.textContent = paragraph;

                elements.chapterBody.appendChild(p);
            });
        }

        updateProgress();
        updateNavigation();

        if (elements.chapterPosition) {
            elements.chapterPosition.scrollIntoView({
                behavior: "smooth",
                block: "nearest"
            });
        }
    }


    async function loadChapter(number) {
        if (loading) {
            return;
        }

        if (number < 1 || number > chapterCount) {
            return;
        }

        if (!seed) {
            return;
        }

        loading = true;

        updateNavigation();

        clearChapter();

        try {
            const response = await fetch(
                `/api/chapter/${encodeURIComponent(seed)}/${number}`,
                {
                    method: "GET",
                    headers: {
                        "Accept": "application/json"
                    },
                    cache: "no-store"
                }
            );

            if (!response.ok) {
                throw new Error(
                    `Chapter request failed: ${response.status}`
                );
            }

            const chapter = await response.json();

            renderChapter(chapter);

        } catch (error) {
            console.error(error);

            if (elements.chapterTitle) {
                elements.chapterTitle.textContent =
                    "Unable to load chapter";
            }

            if (elements.chapterBody) {
                elements.chapterBody.innerHTML = "";

                const message =
                    document.createElement("p");

                message.textContent =
                    "Something went wrong while loading this chapter. Please try again.";

                elements.chapterBody.appendChild(message);
            }

        } finally {
            loading = false;

            updateNavigation();
        }
    }


    function goToChapter(number) {
        loadChapter(number);

        const reader =
            document.getElementById("chapters");

        if (reader) {
            reader.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }
    }


    function newNovel() {
        /*
         * Do not store anything locally.
         *
         * A normal navigation request reaches Flask /,
         * which creates a new cryptographically random seed.
         */
        window.location.href = "/";
    }


    function randomChapter() {
        const number =
            Math.floor(Math.random() * chapterCount) + 1;

        goToChapter(number);
    }


    if (elements.previousChapter) {
        elements.previousChapter.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter - 1);
            }
        );
    }


    if (elements.nextChapter) {
        elements.nextChapter.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter + 1);
            }
        );
    }


    if (elements.previousChapterBottom) {
        elements.previousChapterBottom.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter - 1);
            }
        );
    }


    if (elements.nextChapterBottom) {
        elements.nextChapterBottom.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter + 1);
            }
        );
    }


    if (elements.startReading) {
        elements.startReading.addEventListener(
            "click",
            function () {
                goToChapter(1);
            }
        );
    }


    if (elements.randomChapter) {
        elements.randomChapter.addEventListener(
            "click",
            function () {
                randomChapter();
            }
        );
    }


    if (elements.newNovelButton) {
        elements.newNovelButton.addEventListener(
            "click",
            newNovel
        );
    }


    if (elements.finalNewNovel) {
        elements.finalNewNovel.addEventListener(
            "click",
            newNovel
        );
    }


    if (elements.chapterList) {
        const arcButtons =
            elements.chapterList.querySelectorAll(
                ".arc-button"
            );

        arcButtons.forEach(function (button) {
            button.addEventListener(
                "click",
                function () {
                    const start =
                        Number(button.dataset.start);

                    if (Number.isInteger(start)) {
                        goToChapter(start);
                    }
                }
            );
        });
    }


    /*
     * Keyboard navigation.
     */
    document.addEventListener(
        "keydown",
        function (event) {

            const tag =
                document.activeElement?.tagName;

            if (
                tag === "INPUT" ||
                tag === "TEXTAREA" ||
                tag === "SELECT"
            ) {
                return;
            }

            if (event.key === "ArrowLeft") {
                goToChapter(currentChapter - 1);
            }

            if (event.key === "ArrowRight") {
                goToChapter(currentChapter + 1);
            }
        }
    );


    /*
     * Load Chapter 1 automatically.
     */
    loadChapter(1);

})();(function () {
    "use strict";

    const config = window.NOVEL_CONFIG || {};

    const seed = String(config.seed || "");
    const chapterCount = Number(config.chapterCount || 600);

    let currentChapter = 1;
    let loading = false;


    const elements = {
        chapterPosition: document.getElementById("chapterPosition"),
        chapterArc: document.getElementById("chapterArc"),
        chapterLocation: document.getElementById("chapterLocation"),
        chapterTitle: document.getElementById("chapterTitle"),
        chapterBody: document.getElementById("chapterBody"),
        progressBar: document.getElementById("progressBar"),

        previousChapter: document.getElementById("previousChapter"),
        nextChapter: document.getElementById("nextChapter"),

        previousChapterBottom:
            document.getElementById("previousChapterBottom"),

        nextChapterBottom:
            document.getElementById("nextChapterBottom"),

        startReading:
            document.getElementById("startReading"),

        randomChapter:
            document.getElementById("randomChapter"),

        newNovelButton:
            document.getElementById("newNovelButton"),

        finalNewNovel:
            document.getElementById("finalNewNovel"),

        chapterList:
            document.getElementById("chapterList"),
    };


    function setButtonState(button, disabled) {
        if (!button) {
            return;
        }

        button.disabled = disabled;
    }


    function updateNavigation() {
        const atBeginning = currentChapter <= 1;
        const atEnd = currentChapter >= chapterCount;

        setButtonState(
            elements.previousChapter,
            atBeginning || loading
        );

        setButtonState(
            elements.previousChapterBottom,
            atBeginning || loading
        );

        setButtonState(
            elements.nextChapter,
            atEnd || loading
        );

        setButtonState(
            elements.nextChapterBottom,
            atEnd || loading
        );
    }


    function updateProgress() {
        const percentage =
            (currentChapter / chapterCount) * 100;

        if (elements.progressBar) {
            elements.progressBar.style.width =
                `${Math.min(100, percentage)}%`;
        }
    }


    function clearChapter() {
        if (elements.chapterBody) {
            elements.chapterBody.innerHTML = "";
        }

        if (elements.chapterTitle) {
            elements.chapterTitle.textContent =
                "Loading Chapter...";
        }
    }


    function renderChapter(chapter) {
        if (!chapter) {
            return;
        }

        currentChapter = Number(chapter.number) || 1;

        if (elements.chapterPosition) {
            elements.chapterPosition.textContent =
                `Chapter ${String(currentChapter).padStart(3, "0")}`;
        }

        if (elements.chapterArc) {
            elements.chapterArc.textContent =
                chapter.arc?.title || "STORY";
        }

        if (elements.chapterLocation) {
            elements.chapterLocation.textContent =
                chapter.location || "UNKNOWN";
        }

        if (elements.chapterTitle) {
            elements.chapterTitle.textContent =
                chapter.title || `Chapter ${currentChapter}`;
        }

        if (elements.chapterBody) {
            elements.chapterBody.innerHTML = "";

            const paragraphs =
                Array.isArray(chapter.paragraphs)
                    ? chapter.paragraphs
                    : [];

            paragraphs.forEach(function (paragraph) {
                const p = document.createElement("p");

                p.textContent = paragraph;

                elements.chapterBody.appendChild(p);
            });
        }

        updateProgress();
        updateNavigation();

        if (elements.chapterPosition) {
            elements.chapterPosition.scrollIntoView({
                behavior: "smooth",
                block: "nearest"
            });
        }
    }


    async function loadChapter(number) {
        if (loading) {
            return;
        }

        if (number < 1 || number > chapterCount) {
            return;
        }

        if (!seed) {
            return;
        }

        loading = true;

        updateNavigation();

        clearChapter();

        try {
            const response = await fetch(
                `/api/chapter/${encodeURIComponent(seed)}/${number}`,
                {
                    method: "GET",
                    headers: {
                        "Accept": "application/json"
                    },
                    cache: "no-store"
                }
            );

            if (!response.ok) {
                throw new Error(
                    `Chapter request failed: ${response.status}`
                );
            }

            const chapter = await response.json();

            renderChapter(chapter);

        } catch (error) {
            console.error(error);

            if (elements.chapterTitle) {
                elements.chapterTitle.textContent =
                    "Unable to load chapter";
            }

            if (elements.chapterBody) {
                elements.chapterBody.innerHTML = "";

                const message =
                    document.createElement("p");

                message.textContent =
                    "Something went wrong while loading this chapter. Please try again.";

                elements.chapterBody.appendChild(message);
            }

        } finally {
            loading = false;

            updateNavigation();
        }
    }


    function goToChapter(number) {
        loadChapter(number);

        const reader =
            document.getElementById("chapters");

        if (reader) {
            reader.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }
    }


    function newNovel() {
        /*
         * Do not store anything locally.
         *
         * A normal navigation request reaches Flask /,
         * which creates a new cryptographically random seed.
         */
        window.location.href = "/";
    }


    function randomChapter() {
        const number =
            Math.floor(Math.random() * chapterCount) + 1;

        goToChapter(number);
    }


    if (elements.previousChapter) {
        elements.previousChapter.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter - 1);
            }
        );
    }


    if (elements.nextChapter) {
        elements.nextChapter.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter + 1);
            }
        );
    }


    if (elements.previousChapterBottom) {
        elements.previousChapterBottom.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter - 1);
            }
        );
    }


    if (elements.nextChapterBottom) {
        elements.nextChapterBottom.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter + 1);
            }
        );
    }


    if (elements.startReading) {
        elements.startReading.addEventListener(
            "click",
            function () {
                goToChapter(1);
            }
        );
    }


    if (elements.randomChapter) {
        elements.randomChapter.addEventListener(
            "click",
            function () {
                randomChapter();
            }
        );
    }


    if (elements.newNovelButton) {
        elements.newNovelButton.addEventListener(
            "click",
            newNovel
        );
    }


    if (elements.finalNewNovel) {
        elements.finalNewNovel.addEventListener(
            "click",
            newNovel
        );
    }


    if (elements.chapterList) {
        const arcButtons =
            elements.chapterList.querySelectorAll(
                ".arc-button"
            );

        arcButtons.forEach(function (button) {
            button.addEventListener(
                "click",
                function () {
                    const start =
                        Number(button.dataset.start);

                    if (Number.isInteger(start)) {
                        goToChapter(start);
                    }
                }
            );
        });
    }


    /*
     * Keyboard navigation.
     */
    document.addEventListener(
        "keydown",
        function (event) {

            const tag =
                document.activeElement?.tagName;

            if (
                tag === "INPUT" ||
                tag === "TEXTAREA" ||
                tag === "SELECT"
            ) {
                return;
            }

            if (event.key === "ArrowLeft") {
                goToChapter(currentChapter - 1);
            }

            if (event.key === "ArrowRight") {
                goToChapter(currentChapter + 1);
            }
        }
    );


    /*
     * Load Chapter 1 automatically.
     */
    loadChapter(1);

})();(function () {
    "use strict";

    const config = window.NOVEL_CONFIG || {};

    const seed = String(config.seed || "");
    const chapterCount = Number(config.chapterCount || 600);

    let currentChapter = 1;
    let loading = false;


    const elements = {
        chapterPosition: document.getElementById("chapterPosition"),
        chapterArc: document.getElementById("chapterArc"),
        chapterLocation: document.getElementById("chapterLocation"),
        chapterTitle: document.getElementById("chapterTitle"),
        chapterBody: document.getElementById("chapterBody"),
        progressBar: document.getElementById("progressBar"),

        previousChapter: document.getElementById("previousChapter"),
        nextChapter: document.getElementById("nextChapter"),

        previousChapterBottom:
            document.getElementById("previousChapterBottom"),

        nextChapterBottom:
            document.getElementById("nextChapterBottom"),

        startReading:
            document.getElementById("startReading"),

        randomChapter:
            document.getElementById("randomChapter"),

        newNovelButton:
            document.getElementById("newNovelButton"),

        finalNewNovel:
            document.getElementById("finalNewNovel"),

        chapterList:
            document.getElementById("chapterList"),
    };


    function setButtonState(button, disabled) {
        if (!button) {
            return;
        }

        button.disabled = disabled;
    }


    function updateNavigation() {
        const atBeginning = currentChapter <= 1;
        const atEnd = currentChapter >= chapterCount;

        setButtonState(
            elements.previousChapter,
            atBeginning || loading
        );

        setButtonState(
            elements.previousChapterBottom,
            atBeginning || loading
        );

        setButtonState(
            elements.nextChapter,
            atEnd || loading
        );

        setButtonState(
            elements.nextChapterBottom,
            atEnd || loading
        );
    }


    function updateProgress() {
        const percentage =
            (currentChapter / chapterCount) * 100;

        if (elements.progressBar) {
            elements.progressBar.style.width =
                `${Math.min(100, percentage)}%`;
        }
    }


    function clearChapter() {
        if (elements.chapterBody) {
            elements.chapterBody.innerHTML = "";
        }

        if (elements.chapterTitle) {
            elements.chapterTitle.textContent =
                "Loading Chapter...";
        }
    }


    function renderChapter(chapter) {
        if (!chapter) {
            return;
        }

        currentChapter = Number(chapter.number) || 1;

        if (elements.chapterPosition) {
            elements.chapterPosition.textContent =
                `Chapter ${String(currentChapter).padStart(3, "0")}`;
        }

        if (elements.chapterArc) {
            elements.chapterArc.textContent =
                chapter.arc?.title || "STORY";
        }

        if (elements.chapterLocation) {
            elements.chapterLocation.textContent =
                chapter.location || "UNKNOWN";
        }

        if (elements.chapterTitle) {
            elements.chapterTitle.textContent =
                chapter.title || `Chapter ${currentChapter}`;
        }

        if (elements.chapterBody) {
            elements.chapterBody.innerHTML = "";

            const paragraphs =
                Array.isArray(chapter.paragraphs)
                    ? chapter.paragraphs
                    : [];

            paragraphs.forEach(function (paragraph) {
                const p = document.createElement("p");

                p.textContent = paragraph;

                elements.chapterBody.appendChild(p);
            });
        }

        updateProgress();
        updateNavigation();

        if (elements.chapterPosition) {
            elements.chapterPosition.scrollIntoView({
                behavior: "smooth",
                block: "nearest"
            });
        }
    }


    async function loadChapter(number) {
        if (loading) {
            return;
        }

        if (number < 1 || number > chapterCount) {
            return;
        }

        if (!seed) {
            return;
        }

        loading = true;

        updateNavigation();

        clearChapter();

        try {
            const response = await fetch(
                `/api/chapter/${encodeURIComponent(seed)}/${number}`,
                {
                    method: "GET",
                    headers: {
                        "Accept": "application/json"
                    },
                    cache: "no-store"
                }
            );

            if (!response.ok) {
                throw new Error(
                    `Chapter request failed: ${response.status}`
                );
            }

            const chapter = await response.json();

            renderChapter(chapter);

        } catch (error) {
            console.error(error);

            if (elements.chapterTitle) {
                elements.chapterTitle.textContent =
                    "Unable to load chapter";
            }

            if (elements.chapterBody) {
                elements.chapterBody.innerHTML = "";

                const message =
                    document.createElement("p");

                message.textContent =
                    "Something went wrong while loading this chapter. Please try again.";

                elements.chapterBody.appendChild(message);
            }

        } finally {
            loading = false;

            updateNavigation();
        }
    }


    function goToChapter(number) {
        loadChapter(number);

        const reader =
            document.getElementById("chapters");

        if (reader) {
            reader.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }
    }


    function newNovel() {
        /*
         * Do not store anything locally.
         *
         * A normal navigation request reaches Flask /,
         * which creates a new cryptographically random seed.
         */
        window.location.href = "/";
    }


    function randomChapter() {
        const number =
            Math.floor(Math.random() * chapterCount) + 1;

        goToChapter(number);
    }


    if (elements.previousChapter) {
        elements.previousChapter.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter - 1);
            }
        );
    }


    if (elements.nextChapter) {
        elements.nextChapter.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter + 1);
            }
        );
    }


    if (elements.previousChapterBottom) {
        elements.previousChapterBottom.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter - 1);
            }
        );
    }


    if (elements.nextChapterBottom) {
        elements.nextChapterBottom.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter + 1);
            }
        );
    }


    if (elements.startReading) {
        elements.startReading.addEventListener(
            "click",
            function () {
                goToChapter(1);
            }
        );
    }


    if (elements.randomChapter) {
        elements.randomChapter.addEventListener(
            "click",
            function () {
                randomChapter();
            }
        );
    }


    if (elements.newNovelButton) {
        elements.newNovelButton.addEventListener(
            "click",
            newNovel
        );
    }


    if (elements.finalNewNovel) {
        elements.finalNewNovel.addEventListener(
            "click",
            newNovel
        );
    }


    if (elements.chapterList) {
        const arcButtons =
            elements.chapterList.querySelectorAll(
                ".arc-button"
            );

        arcButtons.forEach(function (button) {
            button.addEventListener(
                "click",
                function () {
                    const start =
                        Number(button.dataset.start);

                    if (Number.isInteger(start)) {
                        goToChapter(start);
                    }
                }
            );
        });
    }


    /*
     * Keyboard navigation.
     */
    document.addEventListener(
        "keydown",
        function (event) {

            const tag =
                document.activeElement?.tagName;

            if (
                tag === "INPUT" ||
                tag === "TEXTAREA" ||
                tag === "SELECT"
            ) {
                return;
            }

            if (event.key === "ArrowLeft") {
                goToChapter(currentChapter - 1);
            }

            if (event.key === "ArrowRight") {
                goToChapter(currentChapter + 1);
            }
        }
    );


    /*
     * Load Chapter 1 automatically.
     */
    loadChapter(1);

})();(function () {
    "use strict";

    const config = window.NOVEL_CONFIG || {};

    const seed = String(config.seed || "");
    const chapterCount = Number(config.chapterCount || 600);

    let currentChapter = 1;
    let loading = false;


    const elements = {
        chapterPosition: document.getElementById("chapterPosition"),
        chapterArc: document.getElementById("chapterArc"),
        chapterLocation: document.getElementById("chapterLocation"),
        chapterTitle: document.getElementById("chapterTitle"),
        chapterBody: document.getElementById("chapterBody"),
        progressBar: document.getElementById("progressBar"),

        previousChapter: document.getElementById("previousChapter"),
        nextChapter: document.getElementById("nextChapter"),

        previousChapterBottom:
            document.getElementById("previousChapterBottom"),

        nextChapterBottom:
            document.getElementById("nextChapterBottom"),

        startReading:
            document.getElementById("startReading"),

        randomChapter:
            document.getElementById("randomChapter"),

        newNovelButton:
            document.getElementById("newNovelButton"),

        finalNewNovel:
            document.getElementById("finalNewNovel"),

        chapterList:
            document.getElementById("chapterList"),
    };


    function setButtonState(button, disabled) {
        if (!button) {
            return;
        }

        button.disabled = disabled;
    }


    function updateNavigation() {
        const atBeginning = currentChapter <= 1;
        const atEnd = currentChapter >= chapterCount;

        setButtonState(
            elements.previousChapter,
            atBeginning || loading
        );

        setButtonState(
            elements.previousChapterBottom,
            atBeginning || loading
        );

        setButtonState(
            elements.nextChapter,
            atEnd || loading
        );

        setButtonState(
            elements.nextChapterBottom,
            atEnd || loading
        );
    }


    function updateProgress() {
        const percentage =
            (currentChapter / chapterCount) * 100;

        if (elements.progressBar) {
            elements.progressBar.style.width =
                `${Math.min(100, percentage)}%`;
        }
    }


    function clearChapter() {
        if (elements.chapterBody) {
            elements.chapterBody.innerHTML = "";
        }

        if (elements.chapterTitle) {
            elements.chapterTitle.textContent =
                "Loading Chapter...";
        }
    }


    function renderChapter(chapter) {
        if (!chapter) {
            return;
        }

        currentChapter = Number(chapter.number) || 1;

        if (elements.chapterPosition) {
            elements.chapterPosition.textContent =
                `Chapter ${String(currentChapter).padStart(3, "0")}`;
        }

        if (elements.chapterArc) {
            elements.chapterArc.textContent =
                chapter.arc?.title || "STORY";
        }

        if (elements.chapterLocation) {
            elements.chapterLocation.textContent =
                chapter.location || "UNKNOWN";
        }

        if (elements.chapterTitle) {
            elements.chapterTitle.textContent =
                chapter.title || `Chapter ${currentChapter}`;
        }

        if (elements.chapterBody) {
            elements.chapterBody.innerHTML = "";

            const paragraphs =
                Array.isArray(chapter.paragraphs)
                    ? chapter.paragraphs
                    : [];

            paragraphs.forEach(function (paragraph) {
                const p = document.createElement("p");

                p.textContent = paragraph;

                elements.chapterBody.appendChild(p);
            });
        }

        updateProgress();
        updateNavigation();

        if (elements.chapterPosition) {
            elements.chapterPosition.scrollIntoView({
                behavior: "smooth",
                block: "nearest"
            });
        }
    }


    async function loadChapter(number) {
        if (loading) {
            return;
        }

        if (number < 1 || number > chapterCount) {
            return;
        }

        if (!seed) {
            return;
        }

        loading = true;

        updateNavigation();

        clearChapter();

        try {
            const response = await fetch(
                `/api/chapter/${encodeURIComponent(seed)}/${number}`,
                {
                    method: "GET",
                    headers: {
                        "Accept": "application/json"
                    },
                    cache: "no-store"
                }
            );

            if (!response.ok) {
                throw new Error(
                    `Chapter request failed: ${response.status}`
                );
            }

            const chapter = await response.json();

            renderChapter(chapter);

        } catch (error) {
            console.error(error);

            if (elements.chapterTitle) {
                elements.chapterTitle.textContent =
                    "Unable to load chapter";
            }

            if (elements.chapterBody) {
                elements.chapterBody.innerHTML = "";

                const message =
                    document.createElement("p");

                message.textContent =
                    "Something went wrong while loading this chapter. Please try again.";

                elements.chapterBody.appendChild(message);
            }

        } finally {
            loading = false;

            updateNavigation();
        }
    }


    function goToChapter(number) {
        loadChapter(number);

        const reader =
            document.getElementById("chapters");

        if (reader) {
            reader.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }
    }


    function newNovel() {
        /*
         * Do not store anything locally.
         *
         * A normal navigation request reaches Flask /,
         * which creates a new cryptographically random seed.
         */
        window.location.href = "/";
    }


    function randomChapter() {
        const number =
            Math.floor(Math.random() * chapterCount) + 1;

        goToChapter(number);
    }


    if (elements.previousChapter) {
        elements.previousChapter.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter - 1);
            }
        );
    }


    if (elements.nextChapter) {
        elements.nextChapter.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter + 1);
            }
        );
    }


    if (elements.previousChapterBottom) {
        elements.previousChapterBottom.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter - 1);
            }
        );
    }


    if (elements.nextChapterBottom) {
        elements.nextChapterBottom.addEventListener(
            "click",
            function () {
                goToChapter(currentChapter + 1);
            }
        );
    }


    if (elements.startReading) {
        elements.startReading.addEventListener(
            "click",
            function () {
                goToChapter(1);
            }
        );
    }


    if (elements.randomChapter) {
        elements.randomChapter.addEventListener(
            "click",
            function () {
                randomChapter();
            }
        );
    }


    if (elements.newNovelButton) {
        elements.newNovelButton.addEventListener(
            "click",
            newNovel
        );
    }


    if (elements.finalNewNovel) {
        elements.finalNewNovel.addEventListener(
            "click",
            newNovel
        );
    }


    if (elements.chapterList) {
        const arcButtons =
            elements.chapterList.querySelectorAll(
                ".arc-button"
            );

        arcButtons.forEach(function (button) {
            button.addEventListener(
                "click",
                function () {
                    const start =
                        Number(button.dataset.start);

                    if (Number.isInteger(start)) {
                        goToChapter(start);
                    }
                }
            );
        });
    }


    /*
     * Keyboard navigation.
     */
    document.addEventListener(
        "keydown",
        function (event) {

            const tag =
                document.activeElement?.tagName;

            if (
                tag === "INPUT" ||
                tag === "TEXTAREA" ||
                tag === "SELECT"
            ) {
                return;
            }

            if (event.key === "ArrowLeft") {
                goToChapter(currentChapter - 1);
            }

            if (event.key === "ArrowRight") {
                goToChapter(currentChapter + 1);
            }
        }
    );


    /*
     * Load Chapter 1 automatically.
     */
    loadChapter(1);

})();
