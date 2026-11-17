# URL Price Graph

A mobile-friendly, browser-only GitHub Pages tool for saving price-source URLs, pasting JSON responses, and exploring timestamp-versus-price charts.

## Open the website

https://nanokoder007.github.io/bigmint-price-monitor/

## Use it

1. Add a **Series name** and its **Website / API URL**, then select **Save source**.
2. Copy the saved URL when you need to retrieve its data.
3. Paste the JSON response into the response box and choose **Parse & save data**.
4. Switch between saved series using their **Open** buttons. Each series retains its own pasted JSON in this browser.
5. Use **1H**, **4H**, **12H**, **1D**, **1M**, or **ALL** to change the visible time window.
6. On desktop, scroll over the graph to zoom and drag horizontally to pan. On a phone or tablet, drag across the graph to pan; the chart controls remain usable on a narrow screen. Use **Reset** to return to the full series.

The chart accepts arrays like `[[timestamp, price], ...]` and arrays of objects with timestamp and price fields. You can change the timestamp and price selectors when automatic field detection needs adjustment. Numeric Unix timestamps in seconds or milliseconds and ISO date strings are supported. Displayed times use Asia/Kolkata (IST).

## Browser / CORS limitation

The optional direct GET runs in your browser. For a cross-origin endpoint, its server must allow the site's origin through CORS. The app does not bypass CORS, authentication, or access controls. When direct GET is blocked, paste the JSON response body instead.

## Local privacy and storage

Saved source names, URLs, field mappings, and pasted JSON are stored in your browser's local storage on this device. They are not uploaded to a server. Clearing this site's browser data removes the saved series. Avoid including passwords, session cookies, or private API keys in saved URLs.
