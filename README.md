# BigMint Price Monitor

A GitHub Pages dashboard shell for charting price history. Automated BigMint collection is currently paused pending written authorization for programmatic API access.

## Setup

1. In **Settings → Pages**, choose **Deploy from a branch**, select branch `main`, folder `/docs`, then Save.
2. The dashboard can display historical data in `docs/data/history.json`.
3. To enable automatic updates, first obtain written approval and the official API endpoint/authentication terms from BigMint. Then connect an approved API integration.

## Adding more price series

Edit `sources.json` in the repository root and add another item to the `sources` array. Use a unique `id`, display `name`, and BigMint graph `url`. The workflow copies this configuration to `docs/sources.json` for the dashboard.

## Data and privacy

This is a public repository. Collected prices and source URLs are published in the repository. Do not add credentials or private data. 
## BigMint data access

BigMint's published terms restrict scripted extraction, scraping, and regular downloading of its website content without prior written consent. Its historical-data page describes API plug-ins as case-by-case and subject to approval. This repository therefore does not run a scheduled scraper. Do not add cookies, passwords, or API tokens to source files. Once BigMint provides an approved API, connect it through a server-side function and store any credential as a private deployment secret.
