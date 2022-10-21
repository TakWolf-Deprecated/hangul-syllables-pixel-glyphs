import logging
import os

from configs import path_define
from utils import glyph_util

logger = logging.getLogger('design-service')


def format_glyph_files(px):
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


def _parse_glyph_file_name(glyph_file_name):
    """
    解析字形源文件名称
    例子：'0-0.png'
    """
    params = glyph_file_name.removesuffix('.png').split('-')
    assert len(params) == 2, glyph_file_name
    index = params[0]
    weight = params[1]
    return index, weight


def _create_initial_consonant_cellar(px):
    """
    部件：声母
    索引：['fullheight/halfheight']['vertical/horizontal/wrapping'][index]
    结构：glyph_data、左上填充矩形宽度、左上填充矩形高度
    """
    cellar = {}
    letter_dir = os.path.join(path_define.fragments_dir, str(px), 'initial-consonants')
    for height_mode in ['fullheight', 'halfheight']:
        cellar[height_mode] = {}
        for placement_mode in ['vertical', 'horizontal', 'wrapping']:
            cellar[height_mode][placement_mode] = {}
            scan_dir = os.path.join(letter_dir, height_mode, placement_mode)
            for glyph_file_dir, _, glyph_file_names in os.walk(scan_dir):
                for glyph_file_name in glyph_file_names:
                    if not glyph_file_name.endswith('.png'):
                        continue
                    glyph_file_path = os.path.join(glyph_file_dir, glyph_file_name)
                    index, weight = _parse_glyph_file_name(glyph_file_name)
                    glyph_data, width, height = glyph_util.load_glyph_data_from_png(glyph_file_path)
                    # TODO
                    cellar[height_mode][placement_mode][index] = (glyph_data)
    return cellar


def _create_vowel_cellar(px):
    """
    部件：韵母
    索引：['fullheight/halfheight'][index]
    结构：glyph_data、左上空白矩形宽度、左上空白矩形高度、底部空白高度
    """
    cellar = {}
    letter_dir = os.path.join(path_define.fragments_dir, str(px), 'vowels')
    for height_mode in ['fullheight', 'halfheight']:
        cellar[height_mode] = {}
        scan_dir = os.path.join(letter_dir, height_mode)
        for glyph_file_dir, _, glyph_file_names in os.walk(scan_dir):
            for glyph_file_name in glyph_file_names:
                if not glyph_file_name.endswith('.png'):
                    continue
                glyph_file_path = os.path.join(glyph_file_dir, glyph_file_name)
                index, weight = _parse_glyph_file_name(glyph_file_name)
                glyph_data, width, height = glyph_util.load_glyph_data_from_png(glyph_file_path)
                # TODO
                cellar[height_mode][index] = (glyph_data)
    return cellar


def _create_final_consonant_cellar(px):
    """
    部件：韵尾
    索引：[index]
    结构：glyph_data、顶部空白高度
    """
    cellar = {}
    scan_dir = os.path.join(path_define.fragments_dir, str(px), 'final-consonants')
    for glyph_file_dir, _, glyph_file_names in os.walk(scan_dir):
        for glyph_file_name in glyph_file_names:
            if not glyph_file_name.endswith('.png'):
                continue
            glyph_file_path = os.path.join(glyph_file_dir, glyph_file_name)
            index, weight = _parse_glyph_file_name(glyph_file_name)
            glyph_data, width, height = glyph_util.load_glyph_data_from_png(glyph_file_path)
            # TODO
            cellar[index] = (glyph_data)
    return cellar


class DesignContext:
    def __init__(self, px):
        self.px = px
        self.initial_consonant_cellar = _create_initial_consonant_cellar(px)
        self.vowel_cellar = _create_vowel_cellar(px)
        self.final_consonant_cellar = _create_final_consonant_cellar(px)
