# Light Novel World

Complete Python/Flask procedural light-novel website.

- Every HTTP refresh/request generates a new novel.
- UI and layout are generated from the novel's genre and visual identity.
- HTML5 + CSS3 + vanilla JavaScript frontend.
- No database.
- No localStorage, sessionStorage, IndexedDB, cookies, login, or signup.
- Responsive mobile/tablet/desktop design.
- Render Blueprint included.
- GitHub-ready.

The design uses a modern component-oriented visual language inspired by the requested UI Watermelon aesthetic, implemented directly in CSS/HTML rather than requiring React.

## Run

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Visit http://127.0.0.1:10000

## Deploy

Push to GitHub, then create a Render Blueprint from `render.yaml`.

Because the novel must be generated on every request, Render should run this as a Python web service, not a static-site service.
