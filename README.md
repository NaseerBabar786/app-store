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

## Upload to apps.bulkbazaar.ca with cPanel (GoDaddy)
1. cPanel > Domains > Create A New Domain (or Subdomains): enter `apps.bulkbazaar.ca`, keep the suggested folder (e.g. `public_html/apps.bulkbazaar.ca`), Submit.
2. cPanel > File Manager > open that folder > Upload `apps-bulkbazaar-upload.zip` > right-click it > Extract. Delete the zip afterwards.
3. Optional: upload `bulkbazaar-apps-page/index.html` into `public_html/apps/` so www.bulkbazaar.ca/apps forwards to the store, and add an "Apps" link to your site menu.
4. cPanel > Security > SSL/TLS Status > Run AutoSSL so https works on the new subdomain.

## Or put it online with GitHub Pages
1. Create a GitHub repository and upload `index.html` and `apps.json`.
2. Settings > Pages > Source: "Deploy from a branch", branch `main`, folder `/`.
3. Your store is live at `https://<your-username>.github.io/<repo-name>/`.

APK, EXE and other download files can go in the repo's Releases page and be linked from `links`.

Opening index.html straight from your computer (file://) won't load apps.json in most browsers; use the hosted site or run `python3 -m http.server` in this folder.
