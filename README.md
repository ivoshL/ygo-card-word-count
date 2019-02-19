Inspired from this video:

Top 10 Cards With The Longest Card Text in YuGiOh
https://www.youtube.com/watch?v=PMIgxc3Z1lM

Scrapes card info (9000+ cards) from https://www.db.yugioh-card.com/ — there may be some cards missing.

# Scripts

To run the script(s) yourself:

1 - create a virtual environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2 - run one of:

`python3 parse_from_web.py` - scrapes https://www.db.yugioh-card.com/ and saves info to `output.json`

`python3 parse_from_web_and_download.py` - saves pages from https://www.db.yugioh-card.com/ to `pages/` and saves info to `output.json`

`python3 parse_from_downloaded_pages.py` - parses info from `pages/` files and saves info to `output.json`

3 - run local server:

```
python3 local_server.py
```

visit http://localhost:8000 to see table.
