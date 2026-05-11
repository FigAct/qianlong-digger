"""
 S05 - 网页图片的爬取及本地保存

 来源：https://spiderbuf.cn/web-scraping-practices?order=rating

 爬虫练习网站：Spiderbuf
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from fetcher import base
import logging, os, requests
from lxml import etree
from datetime import datetime

# 必要变量
url = "https://spiderbuf.cn/web-scraping-practice/scraping-images-from-web"
# 时间获取，文件名获取
now = datetime.now()
now = now.strftime("%Y%m%d%H%M%S")
file = os.path.splitext(os.path.basename(__file__))[0]

# 初始化日志器
dir_path : str = os.path.abspath(os.path.dirname(__file__))
PATH_LOG = os.path.join(dir_path, "log", f"{file}", f"{now + file}.log")
PATH_HTML = os.path.join(dir_path, "save_html", f"{file}", f"{now + file}.html")
dir_log = os.path.dirname(PATH_LOG)
if not os.path.exists(dir_log):
    os.makedirs(dir_log, exist_ok=True)

# 日志初始化
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"{PATH_LOG}", encoding='utf-8'),  # 保存到文件
        logging.StreamHandler()  # 同时输出到控制台
    ]
)
logger = logging.getLogger(__name__)

def parsers(_html:str)->list:
    """解析html"""
    root = etree.HTML(_html)
    logger.info("html树生成")
    image = root.xpath('//img/@src')
    logger.info("image url 获得成功")
    return image

def get_image(_url:list[str])-> None:
    """获得图片"""
    _image_path : str = os.path.join(dir_path, "image", file)
    if not os.path.exists(_image_path):
        os.makedirs(_image_path, exist_ok=True)

    for i in _url:
        file_url = "https://spiderbuf.cn" + i
        file_name : str = i.lstrip("/").replace("/", "_")
        file_path = os.path.join(_image_path, file_name)
        jpg = requests.get(file_url).content
        with open(file_path, "wb") as f:
            f.write(jpg)
            logger.info(f"图片保存到{file_path}")


if __name__ == "__main__":
    html = base.fetcher(url, save_path=PATH_HTML) # 获得源码
    url = parsers(html)
    get_image(url)
    # url = ['/static/images/beginner/1kwfkui2.jpg', '/static/images/beginner/9cwjdins.jpg',
    #        '/static/images/beginner/ti8btii4.jpg', '/static/images/beginner/7jucrlfr.jpg',
    #        '/static/images/beginner/zzugx8tl.jpg', '/static/images/beginner/1ky9g5dp.jpg']
    # get_image(url)


