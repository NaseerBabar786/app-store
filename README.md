# Bulk Bazaar App Store

A small "Play Store" style website that lists every app you build.

- `index.html` is the store page (catalog, categories, search, app detail pages).
- `apps.json` is the only file you edit to add, change or remove apps.

## Add an app
Copy one block inside `"apps"` in apps.json and change the fields:

| Field | Meaning |
|---|---|
| id | short unique name used in the link, e.g. `budget-buddy` |
| name, tagline, description, whatsNew | text shown in the store |
| category | Finance, Games, Tools... new categories appear automatically |
| icon | `{"letter": "B", "color": "#0F9D74"}` or `{"image": "icons/budget.png"}` |
| featured | `true` to show it in the Featured row |
| version, updated (YYYY-MM-DD), size, platforms | info shown on the detail page |
| links | any of `web`, `android`, `ios`, `windows`, `mac`, `source`, each a URL |
| example | remove this line once the app is real |

## Hosting
Live at https://apps.bulkbazaar.ca from GitHub repo NaseerBabar786/app-store (GitHub Pages, branch main). It is a separate site from www.bulkbazaar.ca and only borrows its look.

## Put a copy online with GitHub Pages
1. Create a GitHub repository and upload `index.html` and `apps.json`.
2. Settings > Pages > Source: "Deploy from a branch", branch `main`, folder `/`.
3. Your store is live at `https://<your-username>.github.io/<repo-name>/`.

APK, EXE and other download files can go in the repo's Releases page and be linked from `links`.

Opening index.html straight from your computer (file://) won't load apps.json in most browsers; use the hosted site or run `python3 -m http.server` in this folder.
