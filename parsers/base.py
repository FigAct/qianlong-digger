# parsers/base.py
class BaseParser:
    def parse(self, html: str):
        """
        解析 HTML 并返回结构化数据。

        Args:
                html: 待解析的完整 HTML 字符串。

        Returns:
                包含字段的字典，例如 {"title": "xxx", "links": [...]}。

        Raises:
                NotImplementedError: 子类必须覆盖此方法。
        """
        raise NotImplementedError