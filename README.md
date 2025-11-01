# 爬虫项目

---
#主要是学习使用

初学者

| 目录           | 跟什么打交道                         | 典型文件                                 | 换站点要动吗？       |
|--------------|--------------------------------|--------------------------------------|---------------|
| `config/`    | **YAML 配置**（URL、限速、字段名）        | `douban.yaml` `novel.yaml`           | ✅ 新建一个 YAML   |
| `scheduler/` | **任务队列 & 去重**（内存/Redis）        | `mem_scheduler.py`                   | ❌ 不动          |
| `fetcher/`   | **网络层**（同步/异步、重试、限速）           | `sync_fetcher.py` `async_fetcher.py` | ❌ 不动（可插拔）     |
| `parsers/`   | **HTML/JSON 解析**（一行行 yield 字典） | `parser_douban.py` `parser_novel.py` | ✅ 新建一个 Parser |
| `pipeline/`  | **输出落地**（CSV/JSON/MySQL）       | `csv_pipe.py` `json_pipe.py`         | ❌ 不动（可插拔）     |
| `utils/`     | **工具 & 日志**（公共函数、日志格式）         | `log.py` `helper.py`                 | ❌ 不动          |
