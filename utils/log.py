"""
这是一个模板
"""
import logging

def logger_init(path="loging"):

    # 配置：同时输出到控制台和文件
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"{path}"),  # 保存到文件
            logging.StreamHandler()  # 同时输出到控制台
        ]
    )

    logger = logging.getLogger(__name__)

    logger.info("这条会同时出现在控制台和 app.log 文件中")