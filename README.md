# Quarterly Earnings — RevealJS Deck

This is a single-file RevealJS presentation suitable for GitHub Pages.

## Contact

**Email:** 24ds3000004@ds.study.iitm.ac.in

## Quick Preview
Just open `index.html` in a modern browser.

## Publish on GitHub Pages
1. Create a new GitHub repository (e.g., `earnings-deck`).
2. Add `index.html` to the repo root and commit.
3. In **Settings → Pages**, set **Source** to `Deploy from a branch` and select the default branch root. Save.
4. Your site will be published at `https://<your-username>.github.io/earnings-deck/`.

### CLI steps
```bash
git init
git add index.html README.md
git commit -m "Add RevealJS earnings deck"
git branch -M main
git remote add origin https://github.com/<your-username>/earnings-deck.git
git push -u origin main
# Then enable Pages in Settings → Pages
```

## Features checklist
- Email shown: 24ds3000004@ds.study.iitm.ac.in
- Markdown slide (via `data-markdown`)
- Animated fragments
- Code sample with syntax highlighting
- Mathematical equations (KaTeX)
- Speaker notes
- Ready for GitHub Pages (CDN assets,