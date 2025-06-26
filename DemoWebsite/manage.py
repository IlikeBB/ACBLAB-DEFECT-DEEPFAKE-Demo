#!/usr/bin/env python
import os
import sys

def main():
    # 設定 Django 專案的 settings 模組
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deepfake_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("無法匯入 Django") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
