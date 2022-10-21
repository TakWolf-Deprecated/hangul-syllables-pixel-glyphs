import logging
import os

from configs import path_define
from utils import glyph_util

logger = logging.getLogger('design-service')


def verify_glyph_files(px):
    px_dir = os.path.join(path_define.fragments_dir, str(px))
    for glyph_file_dir, _, glyph_file_names in os.walk(px_dir):
        for glyph_file_name in glyph_file_names:
            if not glyph_file_name.endswith('.png'):
                continue
            glyph_file_path = os.path.join(glyph_file_dir, glyph_file_name)
            glyph_data, width, height = glyph_util.load_glyph_data_from_png(glyph_file_path)
            assert px == width == height, glyph_file_path
            glyph_util.save_glyph_data_to_png(glyph_data, glyph_file_path)
            logger.info(f'format glyph file {glyph_file_path}')


class DesignContext:
    def __init__(self, px):
        self.px = px


def create_context(px):
    return DesignContext(px)
