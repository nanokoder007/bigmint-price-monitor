# BigMint Price Monitor

A free GitHub Pages dashboard that stores and charts BigMint price history. The collector runs four times daily (12:00 AM, 6:00 AM, 12:00 PM and 6:00 PM India time) using GitHub Actions.

## Setup

1. In **Settings → Pages**, choose **Deploy from a branch**, select branch `main`, folder `/docs`, then Save.
2. In **Actions**, enable workflows if GitHub asks.
3. Open **Actions → Collect BigMint prices → Run workflow** for the first collection.
4. Your dashboard will be at https://nanokoder007.github.io/bigmint-price-monitor/ after Pages finishes deploying.

The scheduled workflow uses UTC cron times corresponding to 00:00, 06:00, 12:00 and 18:00 IST. GitHub Actions schedules are best-effort and may be delayed.

## Adding more price series

Edit `sources.json` in the repository root and add another item to the `sources` array. Use a unique `id`, display `name`, and BigMint graph `url`. The workflow copies this configuration to `docs/sources.json` for the dashboard.

## Data and privacy

This is a public repository. Collected prices and source URLs are published in the repository. Do not add credentials or private data. The collector expects BigMint's graph response to contain a `point` array of [timestamp, price] pairs. If BigMint changes its response format or blocks automated requests, the workflow will report an error and collection may stop until adjusted.
