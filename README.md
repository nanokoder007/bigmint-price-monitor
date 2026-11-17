# URL Price Graph

A mobile-friendly GitHub Pages tool for exploring timestamp-versus-price JSON as interactive charts.

## Open the website

https://nanokoder007.github.io/bigmint-price-monitor/

## Shared price-source URLs

The website now loads the shared source catalogue from `docs/sources.json`. Every device and browser sees the same saved source names and URLs after the file is committed to GitHub.

To add, rename, or remove a source for everyone:

1. Open [docs/sources.json](https://github.com/nanokoder007/bigmint-price-monitor/edit/main/docs/sources.json).
2. Edit the JSON array. Each entry needs a unique `id`, a `name`, and a `url`.
3. Commit the change to the `main` branch.
4. Reload the website on any device.

Example entry:

```json
{
  "id": "bigmint-ferrous-1038",
  "name": "BigMint Ferrous (1038)",
  "url": "https://www.bigmint.co/prices_tg/graph/1038/INR/f?market=ferrous"
}
```

The website also has a **Copy this browser's URLs for GitHub** control. It is useful for migrating sources that were previously saved only in one browser: copy the generated JSON, open the GitHub editor, replace the file contents, and commit.

## Use the chart

1. Choose a saved source.
2. Copy its URL when you need to retrieve the JSON manually.
3. Paste the JSON response into the response box and choose **Parse & save data**.
4. Switch between saved series using their **Open** buttons.
5. Use **1H**, **4H**, **12H**, **1D**, **1M**, or **ALL** to change the visible time window.
6. On desktop, scroll over the graph to zoom and drag horizontally to pan. Use **Reset** to return to the full series.

The chart accepts arrays like `[[timestamp, price], ...]` and arrays of objects with timestamp and price fields. Numeric Unix timestamps in seconds or milliseconds and ISO date strings are supported. Displayed times use Asia/Kolkata (IST).

## What is shared, and what is not

- **Shared across devices:** source names and URLs in `docs/sources.json`.
- **Still local to each browser:** pasted JSON responses, chart history, current selection, and field mappings. These are stored in browser local storage so the website does not need a GitHub write token.

This means the source list will match on your laptop and other devices, but a chart's pasted data will not automatically sync. The data can be shared too in a later step by moving it into a committed data file or a controlled collector.

## Browser / CORS limitation

The optional direct GET runs in your browser. For a cross-origin endpoint, its server must allow the site's origin through CORS. The app does not bypass CORS, authentication, or access controls. When direct GET is blocked, paste the JSON response body instead.

## Privacy

This is a public repository. Source names and URLs in `docs/sources.json` are publicly visible. Do not include passwords, session cookies, private API keys, or confidential information in URLs.
