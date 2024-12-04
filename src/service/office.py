import json
from typing import Union

import pandas as pd
from tabulate import tabulate
from pandas import DataFrame, Series
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import PDFMinerLoader

from src.logger.logger import ilogger


def docx_reader(filepath: str):
    try:
        content = Docx2txtLoader(filepath).load()[0].page_content
        return (content, None)
    except Exception as error:
        ilogger.error(f"Failed to read docx file: {error}")
        return ("", error)


def pdf_reader(filepath: str):
    try:
        content = PDFMinerLoader(filepath).load()[0].page_content
        return (content, None)
    except Exception as error:
        ilogger.error(f"Failed to read pdf file: {error}")
        return ("", error)


def excel_reader(
    filepath: str, readmode: str = "plain", sheet: Union[str, None] = None
):
    """xls和xlsx格式都支持

    Args:
        filepath (str): 文件路径
        readmode (str): 读取模式, "table"代表返回表格、"plain"代表表格纯文本
        sheet (Union[str, None]): 要读取的工作表名称，默认为空表示读取所有工作表

    Returns:
        Dict[str, str]: 每个工作表的数据作为字符串存储在字典中
    """
    try:
        content = dict()
        sheets = (
            {sheet: pd.read_excel(filepath, sheet_name=sheet)}
            if sheet
            else pd.read_excel(filepath, sheet_name=None)
        )
        for sheet, df in sheets.items():
            if isinstance(df, DataFrame):
                content[sheet] = format_dataframe(df, readmode)
            elif isinstance(df, Series):
                df = df.to_frame().T
                content[sheet] = format_dataframe(df, readmode)
            else:
                ilogger.error(
                    f"Unsupported type returned for sheet '{sheet}': {type(df)}"
                )
        return (json.dumps(content, ensure_ascii=False), None)
    except Exception as error:
        ilogger.error(f"Failed to read excel file: {error}")
        return ("", error)


def format_dataframe(dataframe: DataFrame, readmode: str) -> str:
    """格式化DataFrame为指定模式的字符串"""
    dataframe = (
        dataframe.drop_duplicates()
        .fillna("")
        .loc[:, ~dataframe.columns.str.contains("^Unnamed")]
        .astype(str)
    )
    if readmode == "table":
        return json.dumps(dataframe.to_dict("records"), ensure_ascii=False)
    else:
        return tabulate(dataframe, headers="keys", tablefmt="grid", showindex=False)
