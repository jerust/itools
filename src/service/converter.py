import subprocess
from pathlib import Path

from config import word_to_pdf_image
from config import pdf_to_html_image
from config import word_to_pdf_means
from src.logger.logger import ilogger


def word_to_pdf(filepath: str):
    filepath = Path(filepath)
    if word_to_pdf_means == "java":
        ...
    return convert_word_to_pdf_go_version(filepath)


def convert_word_to_pdf_go_version(filepath: Path) -> str:
    pdf = filepath.with_suffix(".pdf")
    try:
        subprocess.run(
            [
                "curl",
                "-X",
                "POST",
                word_to_pdf_image,
                "-F",
                f"files=@{filepath}",
                "-o",
                pdf,
            ],
            check=True,
            text=True,
            stdout=subprocess.DEVNULL,  # 禁止标准输出
            stderr=subprocess.DEVNULL,  # 禁止错误输出
        )
    except subprocess.CalledProcessError as error:
        ilogger.error(
            f"Command failed with exit code {error.returncode}: {error.stderr}"
        )
    except FileNotFoundError as error:
        ilogger.error(f"Command not found: {error}")
    except PermissionError as error:
        ilogger.error(f"Permission denied: {error}")
    except Exception as error:
        ilogger.error(f"Unexpected error: {error}")
    return str(pdf)


def pdf_to_html(filepath: str):
    path = Path(filepath)
    try:
        subprocess.run(
            [
                "docker",
                "run",
                "--rm",
                "-v",
                f"{path.parent}:/pdf",
                pdf_to_html_image,
                path.name,
            ],
            check=True,
            text=True,
            stdout=subprocess.DEVNULL,  # 禁止标准输出
            stderr=subprocess.DEVNULL,  # 禁止错误输出
        )
    except subprocess.CalledProcessError as error:
        ilogger.error(
            f"Command failed with exit code {error.returncode}: {error.stderr}"
        )
    except FileNotFoundError as error:
        ilogger.error(f"Command not found: {error}")
    except PermissionError as error:
        ilogger.error(f"Permission denied: {error}")
    except Exception as error:
        ilogger.error(f"Unexpected error: {error}")
    return str(path.with_suffix(".html"))
