#!/usr/bin/env python3
"""Collect configured BigMint graph series into docs/data/history.json."""
import json, os, sys, time
from datetime import datetime, timezone
from urllib.request import Request, urlopen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(ROOT, "sources.json")
DOCS_CONFIG = os.path.join(ROOT, "docs", "sources.json")
HISTORY = os.path.join(ROOT, "docs", "data", "history.json")

def fetch(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; PriceHistoryBot/1.0)", "Accept": "application/json,text/plain,*/*"})
    with urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))

def normalize_ts(value):
    ts = int(float(value))
    return ts * 1000 if ts < 100_000_000_000 else ts

def main():
    with open(CONFIG, encoding="utf-8") as f:
        config = json.load(f)
    os.makedirs(os.path.dirname(HISTORY), exist_ok=True)
    try:
        with open(HISTORY, encoding="utf-8") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = {"updatedAt": None, "sources": {}}
    history.setdefault("sources", {})
    for src in config.get("sources", []):
        sid, url = src["id"], src["url"]
        print("Fetching", src.get("name", sid), url)
        payload = fetch(url)
        points = payload.get("point") if isinstance(payload, dict) else None
        if points is None and isinstance(payload, dict):
            points = payload.get("data")
        if not isinstance(points, list):
            raise ValueError(f"Unexpected BigMint response for {sid}: expected a 'point' array")
        old = history["sources"].get(sid, [])
        merged = {int(p[0]): float(p[1]) for p in old if isinstance(p, list) and len(p) >= 2}
        added = 0
        for p in points:
            if not isinstance(p, (list, tuple)) or len(p) < 2:
                continue
            ts, price = normalize_ts(p[0]), float(p[1])
            if price == price and abs(price) != float("inf"):
                merged[ts] = price
                added += 1
        history["sources"][sid] = [[ts, merged[ts]] for ts in sorted(merged)]
        print(f"Stored {len(history['sources'][sid])} unique points ({added} received in this response)")
    history["updatedAt"] = int(time.time() * 1000)
    with open(HISTORY, "w", encoding="utf-8") as f:
        json.dump(history, f, separators=(",", ":"))
        f.write("\n")
    # Keep dashboard source configuration in sync.
    with open(DOCS_CONFIG, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
        f.write("\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("Collection failed:", exc, file=sys.stderr)
        sys.exit(1)
