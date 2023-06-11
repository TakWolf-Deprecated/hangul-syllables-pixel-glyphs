import logging

from configs import path_define
from services import template_service
from utils import fs_util

logging.basicConfig(level=logging.DEBUG)


def main():
    fs_util.delete_dir(path_define.build_html_dir)

    template_service.make_tool_1_html_file()
    template_service.make_tool_2_html_file()


if __name__ == '__main__':
    main()
