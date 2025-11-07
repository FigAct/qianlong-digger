import time
import logging
import requests
from pathlib import Path
from typing import Optional, Dict
from charset_normalizer import from_bytes

# 配置日志（比print专业）
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def fetcher(
        _url: str,
        delay: int = 0,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 10,
        check_status: bool = True,
        save_path: Optional[str] = None,
        **kwargs
) -> Optional[str]:
    """
    通用网页请求函数

    :param _url: 目标网址(必填）
    :param delay: 请求前延时（秒）
    :param headers: 自定义请求头（默认使用Chrome UA）
    :param timeout: 超时时间（秒）
    :param check_status: 是否检查HTTP状态码
    :param save_path: 保存HTML的文件路径（自动创建目录）
    :param kwargs: 支持 requests.get() 的其他参数（如 cookies, proxies）
    :return: 网页源码或None（失败时）
    """
    # 默认请求头
    default_headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }
    _headers = headers or default_headers

    # 1. 延时（防反爬）
    if delay > 0:
        logger.info(f"延时 {delay} 秒...")
        time.sleep(delay)

    try:
        # 2. 发起请求（带超时）
        logger.info(f"正在请求: {_url}")
        response = requests.get(_url, headers=_headers, timeout=timeout, **kwargs)

        # 3. 检查状态码
        if check_status and response.status_code != 200:
            logger.error(f"请求失败，状态码: {response.status_code}")
            return None

        # 4. 自动编码检测
        _html_best = from_bytes(response.content).best()
        html_content = str(_html_best)
        logger.info(f"成功获取 {len(html_content)} 字符")

        # 5. 保存文件（自动创建目录）
        if save_path:
            save_file = Path(save_path)
            save_file.parent.mkdir(parents=True, exist_ok=True)
            with open(save_file, "w", encoding="utf-8", errors="ignore") as f:
                f.write(html_content)
            logger.info(f"已保存到: {save_file.absolute()}")

        return html_content

    except requests.exceptions.Timeout:
        logger.error(f"请求超时（{timeout}秒）: {_url}")
    except requests.exceptions.RequestException as e:
        logger.error(f"请求异常: {e}")
    except Exception as e:
        logger.error(f"未知错误: {e}")

    return None


# ==================== 测试代码 ====================
if __name__ == "__main__":
    # 测试用例
    url = "https://www.baidu.com"

    # 方式1：基础调用
    _html = fetcher(url, delay=1)

    # # 方式2：保存文件
    # _html = fetcher(url, save_path="./output/test.html")
    #
    # # 方式3：自定义 headers + 代理
    # _html = fetcher(
    #     url,
    #     headers={"User-Agent": "MyBot/1.0"},
    #     timeout=15,
    #     proxies={"http": "http://127.0.0.1:7890"}
    # )