class MemScheduler:
    def __init__(self, start_urls, max_pages=1, page_size=1):
        self.q = start_urls[:max_pages]

    def __iter__(self):
        return iter(self.q)