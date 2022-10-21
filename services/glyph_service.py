import logging
import os.path

from configs import path_define
from utils import fs_util, hangul_util, glyph_util

logger = logging.getLogger('glyph-service')


def _make_syllable_glyph_full_height(design_context, initial_consonant_index, vowel_index, vowel_placement_mode):
    code_point = hangul_util.get_syllable_code_point(initial_consonant_index, vowel_index)
    logger.info(f'U+{code_point:04X} {chr(code_point)} = {hangul_util.initial_consonants[initial_consonant_index]} {hangul_util.vowels[vowel_index]} \u3000 vowel_placement_mode: {vowel_placement_mode}')
    # TODO
    glyph_data = [[0] * design_context.px] * design_context.px
    # TODO
    file_path = os.path.join(path_define.build_glyphs_dir, str(design_context.px), f'{code_point:04X}.png')
    glyph_util.save_glyph_data_to_png(glyph_data, file_path)
    logger.info(f'make {file_path}')


def _make_syllable_glyph_half_height(design_context, initial_consonant_index, vowel_index, vowel_placement_mode, final_consonant_index):
    code_point = hangul_util.get_syllable_code_point(initial_consonant_index, vowel_index, final_consonant_index)
    logger.info(f'U+{code_point:04X} {chr(code_point)} = {hangul_util.initial_consonants[initial_consonant_index]} {hangul_util.vowels[vowel_index]} {hangul_util.final_consonants[final_consonant_index]} vowel_placement_mode: {vowel_placement_mode}')
    # TODO
    glyph_data = [[0] * design_context.px] * design_context.px
    # TODO
    file_path = os.path.join(path_define.build_glyphs_dir, str(design_context.px), f'{code_point:04X}.png')
    glyph_util.save_glyph_data_to_png(glyph_data, file_path)
    logger.info(f'make {file_path}')


def make_glyphs(design_context):
    outputs_dir = os.path.join(path_define.build_glyphs_dir, str(design_context.px))
    fs_util.make_dirs_if_not_exists(outputs_dir)

    for initial_consonant_index, _ in enumerate(hangul_util.initial_consonants):
        for vowel_index, vowel in enumerate(hangul_util.vowels):
            vowel_placement_mode = hangul_util.get_vowel_placement_mode(vowel)
            _make_syllable_glyph_full_height(design_context, initial_consonant_index, vowel_index, vowel_placement_mode)
            for final_consonant_index, final_consonant in enumerate(hangul_util.final_consonants):
                _make_syllable_glyph_half_height(design_context, initial_consonant_index, vowel_index, vowel_placement_mode, final_consonant_index)
