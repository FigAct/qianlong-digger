import random, time, requests

class SyncFetcher:
    """
        发出网络请求。

        Args:
                delay: 设置间隔时间

        """
    def __init__(self, delay=1):
        self.delay = delay

    def get(self, url: str) -> str:
        time.sleep(random.uniform(0.5, self.delay))
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.text