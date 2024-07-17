# FLOMO TO LOGSEQ

## 介绍

### 此脚本 

临时写的脚本，将 flomo 导出的 HTML 笔记转换为 logseq 笔记：

- 使用 flomo 里 time 的日期作为文件名，时间作为三级标题，同一天内有多条记录的会合并
- logseq 存放图片的文件夹名字为 assets。

### 为什么

之前找的其他人的都不太和心意

也尝试了 flomo->notion->obsidian->logseq 的流程，此方案优缺点都很明显，缺点难以接受

优点：

- 能保留 flomo 原始的链接

缺点：

- flomo 同步到 notion 是没有图片的
- 从 notion 导入到 obsidian 以后的 markdown 文件的文件名、文件格式都需要处理
  - 同一天的多个文件需要合并
  - 文件内没有具体时间，只有日期，合并效果不好
  - 文件头部的 yaml 属性需要处理，麻烦
    ```yaml
    ---
    tags:
      - xxx
    Created At: 2024-03-26
    Link: https://v.flomoapp.com/mine/?memo_id=xxxx
    ---
    ```

## 使用方法

1. 从 flomo 导出所有数据（as HTML）到本地并解压缩
2. 复制 `html2md.py` 和 `merge.py` 到解压缩后的文件夹
3. 修改 `html2md.py` 中的 `xxxx的笔记.html` 参数作为输入文件
4. 运行 `python3 html2md.py`
5. 运行 `python3 merge.py`