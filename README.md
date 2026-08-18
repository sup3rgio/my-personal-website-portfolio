# Mathew Yves L. Nipay — Portfolio

A one-page portfolio styled like a technical drawing sheet: a diagram of
you with measurement call-outs, and each section laid out as a numbered
"plate" (Profile, Hobbies, Case Files, Records, Contact).

Built with **Python, HTML, and CSS**. No JavaScript — every animation
(the fade-ins, the diagram draw-in, the mobile menu) runs on pure CSS, so
nothing depends on a script to work.

## Project structure

```
.
├── index.html   # Markup + styling hook — your photo and both
│                  certificates are embedded directly inside this file
├── css/
│   └── style.css # All styling, including the CSS-only animations
└── server.py     # A small Python web server (standard library only)
```

## Why the images are built in

Your photo and both certificates are embedded straight into `index.html`
as base64 image data, instead of sitting next to it as separate files.
That's the fix for the black-image issue on GitHub — it's usually caused
by Git altering binary files on push, or a path/case mismatch between the
file names and what the HTML asks for. With no separate image files, there
is nothing for the browser to fetch and nothing for Git to break.

## Option 1 — open it directly (no setup)

Double-click `index.html`, or drag it into a browser tab. Works completely
on its own, no server required.

## Option 2 — serve it with the Python file

`server.py` uses only Python's built-in `http.server` module — nothing to
install.

1. Make sure Python 3 is installed: `python3 --version`
2. From this folder, run: `python3 server.py`
3. Open your browser to **http://localhost:8000**

Press `Ctrl+C` in the terminal to stop it.

## Put it on GitHub

1. Create a new repository on GitHub (e.g. `portfolio`). Don't add a
   README, license, or .gitignore when prompted — you already have them.
2. Open a terminal inside this folder and run:
   ```
   git init
   git add .
   git commit -m "Initial portfolio"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/portfolio.git
   git push -u origin main
   ```

## Publish it for free with GitHub Pages

1. On GitHub, open your repository and go to **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Under **Branch**, select **main** and folder **/ (root)**, then **Save**.
4. Refresh after a minute — your live URL will appear:
   ```
   https://YOUR-USERNAME.github.io/portfolio/
   ```
   (`server.py` isn't used here — Pages serves `index.html` and
   `css/style.css` directly, which is all a static site needs. The Python
   server is only for running the site on your own computer.)

## Where to customize

- **Your info**: edit the text inside `index.html` (search for your name,
  email, or phone number).
- **Colors/fonts**: defined at the top of `css/style.css` under `:root`.
- **Hobbies**: each card is a `.hobby-card` block in `index.html`.
- **Photos/certificates**: since they're embedded, swapping one means
  generating a new base64 string rather than replacing a file — just ask
  and I'll regenerate `index.html` with a new photo for you.

## Tested

Before delivery, `server.py` was run and checked to confirm: it returns
HTTP 200 for the homepage and stylesheet, serves the correct content
types, returns HTTP 404 for missing pages, and the embedded images load
correctly. `index.html` was also checked for balanced tags and no leftover
or broken references.
