# Barev.trip

> Travel site for Armenia with an AI guide — Garni, Sevan, Khor Virap, Tatev.

[![Live site](https://img.shields.io/badge/Live%20site-gagmirij080--stack.github.io%2Fbarev--trip-d97706?style=flat-square)](https://gagmirij080-stack.github.io/barev-trip/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

**Live:** https://gagmirij080-stack.github.io/barev-trip/

## Overview

Single-page travel site in Armenian / Russian / English with a tour catalog, a booking form and an AI concierge widget. Static hosting on GitHub Pages, no build step.

## Structure

| Path | Purpose |
| --- | --- |
| `index.html` | The whole site: HTML, CSS and JS in one file |
| `404.html` | Branded not-found page |
| `robots.txt` / `sitemap.xml` | SEO |
| `agent.py` | Tour agent: greetings, recommendations, cost calculator |
| `advanced_agent.py` | Concierge: knowledge base and itinerary builder |
| `AGENT_README.md` | Agent overview |
| `BOOKING_AND_LANG_GUIDE.md` | WordPress booking and multilingual setup |
| `WORDPRESS_MIGRATION_GUIDE.md` | From mockup to a WordPress site |
| `TOURS_CONTENT.am.md` | Ready-to-use copy for six tours |

## Stack

- Vanilla HTML / CSS / JS, nothing to install
- GitHub Pages: branch `main`, folder `/ (root)`
- Photos: Wikimedia Commons (free licenses)
- Fonts: Google Fonts; icons: Font Awesome
- SEO: Open Graph, Twitter Card, canonical URL, sitemap, robots

## Run locally

```bash
python -m http.server 8000
```

Then open http://localhost:8000

## AI agents

```bash
python agent.py
python advanced_agent.py
```

## Deploy

Every push to `main` triggers the Pages build. Status: Settings → Pages.

## License

MIT — see [LICENSE](LICENSE).
