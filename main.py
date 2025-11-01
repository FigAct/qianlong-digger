"""
Qianlong-Digger 启动文件
插件式爬虫：换站点只改 config + parser
"""
import argparse
import yaml
from pathlib import Path

# 通用插件（可先硬编码，后续换动态导入）
from fetcher.sync_fetcher import SyncFetcher
from parsers.parser_hello import ParserHello
from pipeline.csv_pipe import CSVPipe
from scheduler.mem_scheduler import MemScheduler


def load_conf(site: str) -> dict:
    """读取 config/<site>.yaml"""
    conf_path = Path(__file__).parent / "config" / f"{site}.yaml"
    with conf_path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def main(site: str = "hello") -> None:
    """主流程：配置 → 调度 → 下载 → 解析 → 输出"""
    cfg = load_conf(site)

    # 1. 初始化插件
    fetch = SyncFetcher(delay=cfg.get("delay", 1))
    parse = ParserHello()  # 将来可动态加载
    pipe = CSVPipe(f"{site}.csv")
    sched = MemScheduler(cfg["start_urls"], cfg.get("max_pages", 1))

    # 2. 逐页抓取
    for url in sched:
        html = fetch.get(url)
        for item in parse.parse(html):
            pipe.write_one(item)

    # 3. 收尾
    pipe.close()
    print(f"✅ {site} done → {site}.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Qianlong Digger")
    parser.add_argument("--site", default="hello", help="config name (without .yaml)")
    args = parser.parse_args()
    main(args.site)