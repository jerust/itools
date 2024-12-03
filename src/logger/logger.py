import os
import sys
import logging
from typing import cast
from types import FrameType

from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


class Logger:
    def __init__(self, path: str = "logs"):
        self.logger = logger

        # 日志输出到控制台
        self.logger.add(
            sys.stdout,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "  # 颜色>时间
            "{process.name} | "  # 进程名
            "{thread.name} | "  # 线程名
            "<cyan>{module}</cyan>.<cyan>{function}</cyan>"  # 模块名.方法名
            ":<cyan>{line}</cyan> | "  # 行号
            "<level>{level}</level>: "  # 等级
            "<level>{message}</level>",  # 日志内容
        )

        # 日志写入到文件内
        self.logger.add(
            os.path.join(path, "{time:YYYY-MM-DD}.log"),  # 目录
            format="{time:YYYY-MM-DD HH:mm:ss} - "  # 时间
            "{process.name} | "  # 进程名
            "{thread.name} | "  # 线程名
            "{module}.{function}:{line} - {level} -{message}",  # 模块名.方法名:行号
            encoding="utf-8",
            retention="7 days",  # 设置历史保留时长
            backtrace=True,  # 回溯
            diagnose=True,  # 诊断
            enqueue=True,  # 异步写入
            rotation="00:00",  # 每日更新时间
            # rotation="5kb",  # 切割，设置文件大小，rotation="12:00"，rotation="1 week"
            # filter="my_module"  # 过滤模块
            # compression="zip"   # 文件压缩
        )

        self.init()

    @staticmethod
    def init():
        LOGGER_NAMES = ("uvicorn.asgi", "uvicorn.access", "uvicorn")
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in LOGGER_NAMES:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler()]
