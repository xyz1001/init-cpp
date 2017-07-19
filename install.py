#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import shutil

def main():
    try:
        shutil.copy("initcpp.py", "/usr/local/bin")
    except PermissionError:
        print("请以超级用户权限执行该文件")
        exit(1)

    dest = "/usr/local/share/initcpp"
    if os.path.exists(dest):
        shutil.rmtree(dest)

    try:
        shutil.copytree("catch", os.path.join(dest, "catch"))
        shutil.copytree("gitignore", os.path.join(dest, "gitignore"))
    except Exception:
        print("拷贝文件失败")
        raise


if __name__ == "__main__":
    main()