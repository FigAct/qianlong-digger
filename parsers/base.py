# parsers/base.py
class BaseParser:
    def parse(self, html: str):
        raise NotImplementedError