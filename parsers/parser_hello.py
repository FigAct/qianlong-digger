from bs4 import BeautifulSoup
from .base import BaseParser

class ParserHello(BaseParser):
    def parse(self, html: str):
        soup = BeautifulSoup(html, 'lxml')
        # 把 <h1> 标签文本 yield 出去
        for h1 in soup.select('h1'):
            yield {'title': h1.text.strip()}