import os
import sys
import time
import tkinter as tk
from tkinter import filedialog

def find_large_files(root_dir, size_limit):
    large_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) > size_limit:
                relative_path = os.path.relpath(file_path, start=root_dir)
                large_files.append(relative_path)
    return large_files

def main():
    root = tk.Tk()
    root.withdraw()  # 不显示主窗口

    root_dir = filedialog.askdirectory(title="请选择搜索的根目录")
    if not root_dir:
        root_dir = os.getcwd()

    size_limit = input("请输入文件大小限制（单位MB，默认为300MB）:")
    size_limit = int(size_limit) * 1024 * 1024 if size_limit else 300 * 1024 * 1024

    large_files = find_large_files(root_dir, size_limit)
    if not large_files:
        print("没有找到大于指定大小的文件。")
        return

    print("以下文件将被删除：")
    for file in large_files:
        print(file)

    try:
        print("10秒后将删除文件。按任意键中断...")
        time.sleep(10)
    except KeyboardInterrupt:
        print("程序已中断。")
        sys.exit()

    for file in large_files:
        os.remove(os.path.join(root_dir, file))
        print(f"{file} 已删除。")

if __name__ == "__main__":
    main()
