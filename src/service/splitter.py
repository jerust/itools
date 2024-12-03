from typing import List

from langchain.text_splitter import RecursiveCharacterTextSplitter


def splitter(
    content: str,
    size: int = 500,
    over: int = 0,
    mark: List[str] = ["\n\n", "\n", "(?<=\。)", " ", ""],
) -> List[str]:
    """
    参数:
        text: 文本

        size: 分割尺寸
        建议: 500-1000

        over: 重叠尺寸
        建议: size的10%-20%

        mark: 分割符号
        默认: ["\n\n", "\n", "(?<=\。)", " ", ""]

    文本分割器首先尝试在每个双换行符("\n\n")处拆分文本, 这通常用于分隔段落
    如果生成的块过大, 它接着尝试在每个换行符("\n")处拆分, 这通常用于分隔句子
    如果生成的块仍然过大, 它接着尝试在每个空格(" ")处拆分, 这通常用于分隔单词
    如果生成的块仍然过大, 它会尝试在每个字符("")处拆分
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=size, chunk_overlap=over, separators=mark
    )
    return splitter.split_text(content)
