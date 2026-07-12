# Web Scraper

A lightweight Python application that demonstrates the basic workflow of a web scraper.

## Overview

Web Scraper simulates downloading an HTML page, extracting useful information, and exporting the collected data.

The project demonstrates modular architecture, text parsing, and clean separation of responsibilities.

## Features

- Download page content (simulation)
- Parse HTML
- Extract article titles
- Export results
- Console report

## Project Structure

```
.
├── main.py
├── fetcher.py
├── parser.py
├── extractor.py
├── models.py
├── exporter.py
├── sample_html.py
├── settings.py
└── README.md
```

## Example Output

```
========= WEB SCRAPER =========

Downloading page...

Articles found:

Python News
Open Source Weekly
AI Trends

----------------------
Total Articles: 3
```

## Technologies

- Python 3

## Future Improvements

- requests
- BeautifulSoup
- Async scraping
- CSV export
- JSON export

MIT License
