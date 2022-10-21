import logging

import configs
from configs import path_define
from services import design_service, glyph_service
from utils import fs_util

logging.basicConfig(level=logging.DEBUG)


def main():
    fs_util.delete_dir(path_define.build_glyphs_dir)

    for px in configs.font_sizes:
        design_service.verify_glyph_files(px)
        design_context = design_service.create_context(px)
        glyph_service.make_glyphs(design_context)


if __name__ == '__main__':
    main()
