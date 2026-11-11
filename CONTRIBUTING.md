# Contributing

Thanks for taking an interest in Barev.trip.

## Workflow

1. Create a branch: `git checkout -b feat/short-description`.
2. Make your change. The site is a single file, so most edits live in `index.html`.
3. Open the page locally (no build step):

```bash
python -m http.server 8000
# then open http://localhost:8000
```

4. Commit using a conventional prefix: `feat:`, `fix:`, `docs:`, `chore:`.
5. Open a pull request describing what changed and why.

## Style

- Keep the site dependency-free: no frameworks, no bundlers.
- Preserve the existing CSS naming and section comments.
- Keep CSS and JS inside `index.html` unless a file grows beyond ~500 lines.
- Images must come from sources that allow hotlinking and have clear licences (Wikimedia Commons, Unsplash licence, etc.).

## Checklist before opening a PR

- [ ] Page renders with no console errors.
- [ ] All images and fonts load (check the Network tab).
- [ ] `404.html`, `robots.txt` and `sitemap.xml` still reference the correct host.
- [ ] README or CHANGELOG updated when behaviour changes.
