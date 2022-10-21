import logging

from configs import path_define
from services import design_service, glyph_service
from services.design_service import DesignContext
from utils import fs_util

logging.basicConfig(level=logging.DEBUG)


def main():
    fs_util.delete_dir(path_define.build_glyphs_dir)

    px = 16
    design_service.format_glyph_files(px)
    design_context = DesignContext(px)
    glyph_service.make_glyphs(design_context)


if __name__ == '__main__':
    main()
