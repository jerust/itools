# 应用程序地址
host = "0.0.0.0"

# 应用程序端口
port = 8888

# 模型使用设备
device = "cpu"  # "mps"、"cuda"、"npu"、"cpu"

# 模型公共目录
public = "/Users/go2rust/Documents/code/python/project/itools"

# 嵌入模型目录
embedding = f"{public}/huggingface/maidalun1020/bce-embedding-base_v1"

# 重排模型目录
reranker = f"{public}/huggingface/maidalun1020/bce-reranker-base_v1"

# 语义模型目录
semantics = f"{public}/huggingface/paraphrase-multilingual-MiniLM-L12-v2"

# word转pdf方式
word_to_pdf_means = "go"

# word转pdf路由
word_to_pdf_route = "http://127.0.0.1:3000/forms/libreoffice/convert"

# pdf转html镜像
pdf_to_html_image = "pdf2html:latest"

# 应用程序日志
log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s | %(processName)s | %(threadName)s | "
            "%(module)s.%(funcName)s:%(lineno)d | %(levelname)s | %(message)s"
        },
        "access": {"format": "%(asctime)s | %(levelname)s | %(message)s"},
    },
    "handlers": {
        "default": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "access": {
            "class": "logging.StreamHandler",
            "formatter": "access",
        },
    },
    "loggers": {
        "uvicorn": {
            "level": "INFO",
            "handlers": ["default"],
            "propagate": False,
        },
        "uvicorn.access": {
            "level": "INFO",
            "handlers": ["access"],
            "propagate": False,
        },
    },
}
