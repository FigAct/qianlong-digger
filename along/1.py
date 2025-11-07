import requests, lxml

def fetcher(url, delay = 0):
    _HEADERS = {
        # 豆瓣最吃 UA，不留直接 418
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    _delay = delay