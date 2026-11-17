# URL Price Graph

A browser-only GitHub Pages tool. Paste a JSON GET endpoint, fetch it manually, and plot timestamp versus price. No scheduler, backend proxy, or response storage is used.

## Open the website

https://nanokoder007.github.io/bigmint-price-monitor/

## How to use

1. Paste a JSON endpoint URL into **GET endpoint**.
2. Click **Fetch & chart**.
3. The app looks for rows such as `[[timestamp, price], ...]` or objects with timestamp and price fields.
4. Use the timestamp and price selectors to correct the field mapping if needed.
5. The graph, latest value, last observation time, and recent readings are shown below.

You can alternatively expand **Paste the JSON response directly**, paste a JSON response body, and click **Parse pasted JSON**.

Timestamps expressed in seconds are converted to milliseconds; millisecond timestamps are retained. ISO date strings are also supported. Dates are shown in India Standard Time (Asia/Kolkata).

## Browser/CORS limitation

The GET request is made directly by your browser. For a cross-origin URL, the server must allow the GitHub Pages origin using CORS response headers. The website does not bypass CORS, authentication, or other access controls. It does not send cookies or credentials and it does not proxy requests through a server.

If the endpoint does not allow browser CORS access, retrieve the JSON using a method you are authorized to use and paste the response body into the JSON box.

## Privacy

Your URL and response are processed in the browser tab only. The app does not save them to a database or send them to this repository. Avoid putting passwords, session cookies, or private API keys into URLs.
