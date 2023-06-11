import logging
import os

from configs import path_define
from utils import glyph_util, hangul_util

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
    index = int(params[0])
    priority = int(params[1])
    return index, priority


def _create_initial_consonant_cellar(px):
    """
    部件：声母
    索引：['fullheight/halfheight']['vertical/horizontal/wrapping'][index]
    结构：glyph_data、优先级、左上填充矩形宽度、左上填充矩形高度
    """
    cellar = {}
    letter_dir = os.path.join(path_define.fragments_dir, str(px), 'initial-consonants')
    for height_mode in ['fullheight', 'halfheight']:
        cellar[height_mode] = {}
        for placement_mode in ['vertical', 'horizontal', 'wrapping']:
            cellar[height_mode][placement_mode] = {}
            for index, _ in enumerate(hangul_util.initial_consonants):
                cellar[height_mode][placement_mode][index] = []
            scan_dir = os.path.join(letter_dir, height_mode, placement_mode)
            for glyph_file_dir, _, glyph_file_names in os.walk(scan_dir):
                for glyph_file_name in glyph_file_names:
                    if not glyph_file_name.endswith('.png'):
                        continue
                    glyph_file_path = os.path.join(glyph_file_dir, glyph_file_name)
                    index, priority = _parse_glyph_file_name(glyph_file_name)
                    glyph_data, width, height = glyph_util.load_glyph_data_from_png(glyph_file_path)
                    # TODO
                    cellar[height_mode][placement_mode][index].append((glyph_data, priority))
            for array in cellar[height_mode][placement_mode].values():
                array.sort(key=lambda item: item[1])
    return cellar


def _create_vowel_cellar(px):
    """
    部件：韵母
    索引：['fullheight/halfheight'][index]
    结构：glyph_data、优先级、左上空白矩形宽度、左上空白矩形高度、底部空白高度
    """
    cellar = {}
    letter_dir = os.path.join(path_define.fragments_dir, str(px), 'vowels')
    for height_mode in ['fullheight', 'halfheight']:
        cellar[height_mode] = {}
        for index, _ in enumerate(hangul_util.vowels):
            cellar[height_mode][index] = []
        scan_dir = os.path.join(letter_dir, height_mode)
        for glyph_file_dir, _, glyph_file_names in os.walk(scan_dir):
            for glyph_file_name in glyph_file_names:
                if not glyph_file_name.endswith('.png'):
                    continue
                glyph_file_path = os.path.join(glyph_file_dir, glyph_file_name)
                index, priority = _parse_glyph_file_name(glyph_file_name)
                glyph_data, width, height = glyph_util.load_glyph_data_from_png(glyph_file_path)
                # TODO
                cellar[height_mode][index].append((glyph_data, priority))
        for array in cellar[height_mode].values():
            array.sort(key=lambda item: item[1])
    return cellar


def _create_final_consonant_cellar(px):
    """
    部件：韵尾
    索引：[index]
    结构：glyph_data、优先级、顶部空白高度
    """
    cellar = {}
    for index, _ in enumerate(hangul_util.final_consonants):
        cellar[index] = []
    scan_dir = os.path.join(path_define.fragments_dir, str(px), 'final-consonants')
    for glyph_file_dir, _, glyph_file_names in os.walk(scan_dir):
        for glyph_file_name in glyph_file_names:
            if not glyph_file_name.endswith('.png'):
                continue
            glyph_file_path = os.path.join(glyph_file_dir, glyph_file_name)
            index, priority = _parse_glyph_file_name(glyph_file_name)
            glyph_data, width, height = glyph_util.load_glyph_data_from_png(glyph_file_path)
            # TODO
            cellar[index].append((glyph_data, priority))
    for array in cellar.values():
        array.sort(key=lambda item: item[1])
    return cellar


class DesignContext:
    def __init__(self, px):
        self.px = px
        self.initial_consonant_cellar = _create_initial_consonant_cellar(px)
        self.vowel_cellar = _create_vowel_cellar(px)
        self.final_consonant_cellar = _create_final_consonant_cellar(px)

    def compose_glyph(self, initial_consonant_index, vowel_index, final_consonant_index):
        height_mode = 'fullheight' if final_consonant_index is None else 'halfheight'
        vowel_placement_mode = hangul_util.get_vowel_placement_mode(vowel_index)

        # TODO
        initial_consonant_infos = self.initial_consonant_cellar[height_mode][vowel_placement_mode][initial_consonant_index]
        if len(initial_consonant_infos) > 0:
            initial_consonant_glyph_data, _ = initial_consonant_infos[0]
        else:
            initial_consonant_glyph_data, _ = glyph_data = [[0] * self.px] * self.px, 0
        # TODO
        vowel_infos = self.vowel_cellar[height_mode][vowel_index]
        if len(vowel_infos) > 0:
            vowel_glyph_data, _ = vowel_infos[0]
        else:
            vowel_glyph_data, _ = glyph_data = [[0] * self.px] * self.px, 0
        # TODO
        glyph_data = glyph_util.merge_glyph_data(self.px, self.px, initial_consonant_glyph_data, vowel_glyph_data)
        return glyph_data
