# Light Novel World

A procedurally generated long-form light novel website built with Python, Flask, HTML, CSS, and JavaScript.

Project Identifier: `blssnvj21`

---

## 1. What Is This Website?

Light Novel World is a web application that automatically creates a new fictional light novel when the website is opened or refreshed.

Each generated novel contains:

- A unique novel title
- A genre
- A secondary genre
- A fictional world
- A protagonist
- A power/ability system
- A major conflict
- A faction
- Supporting characters
- Multiple story arcs
- 600 chapters
- Approximately 800 words per chapter
- A responsive reading interface

The website does not require the visitor to create an account.

There is no login system.

There is no database.

There is no localStorage.

There is no sessionStorage.

---

# 2. Basic Website Flow

The website works approximately like this:

```text
Visitor opens website
        │
        ▼
Flask receives request
        │
        ▼
A fresh random novel seed is created
        │
        ▼
Novel generator creates the novel
        │
        ├── Title
        ├── Genre
        ├── World
        ├── Characters
        ├── Power system
        ├── Conflict
        └── Story arcs
        │
        ▼
Flask sends the generated novel to the HTML template
        │
        ▼
Browser displays the novel website
        │
        ▼
Visitor selects a chapter
        │
        ▼
JavaScript requests the chapter from Flask
        │
        ▼
Flask generates that chapter from:
        │
        ├── Novel seed
        └── Chapter number
        │
        ▼
Chapter is returned as JSON
        │
        ▼
JavaScript displays the chapter
