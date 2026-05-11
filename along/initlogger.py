import logging

def get(
        name,
        path_log:str=None
)-> logging.Logger:
    """
    :param name: 填写调用模块的__name__变量
    :param path_log: 存放日志的文件路径
    :return:
    """
    if path_log is not None:
        handlers=[
                logging.FileHandler(f"{path_log}", encoding='utf-8'),  # 保存到文件
                logging.StreamHandler()  # 同时输出到控制台
        ]
    else:
        handlers = [
            logging.StreamHandler()  # 同时输出到控制台
        ]
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=handlers
    )
    return logging.getLogger(name)



