import os
import re

from bs4 import BeautifulSoup


def parse_html_to_markdown(html_file, output_dir):
    # 读取 HTML 文件
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # 提取 memos 信息
    memos = soup.find_all("div", class_="memo")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 处理每个 memo
    for memo in memos:
        time = memo.find("div", class_="time").text.strip()
        date = time.split(" ")[0]  # 提取日期部分
        mytime = time.split(" ")[1]  # 提取时间部分
        content = memo.find("div", class_="content").text.strip()
        files = memo.find("div", class_="files")

        # 处理文件名中的特殊字符
        filename = re.sub(r"\W+", "_", date) + ".md"

        # 如果文件已存在，则追加内容；否则，创建新文件
        file_path = os.path.join(output_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(f"\n### {mytime}\n{content}\n")
                # 处理图片链接
                if files:
                    for file in files.find_all("img"):
                        file_src = file.get("src")
                        if file_src:
                            # 提取图片文件名
                            file_name = os.path.basename(file_src)
                            f.write(f"![Image](../assets/{file_name})\n")
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"### {mytime}\n{content}\n")
                # 处理图片链接
                if files:
                    for file in files.find_all("img"):
                        file_src = file.get("src")
                        if file_src:
                            # 提取图片文件名
                            file_name = os.path.basename(file_src)
                            f.write(f"![Image](../assets/{file_name})\n")

# 调用函数进行解析
parse_html_to_markdown('xxxx的笔记.html', 'output')