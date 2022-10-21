import logging
import os

import minify_html

import configs
from configs import path_define
from utils import hangul_util, fs_util

logger = logging.getLogger('html-service')


def _make_tool_html_file(matrix, name):
    template = configs.template_env.get_template('tool.html')
    html = template.render(matrix=matrix)
    html = minify_html.minify(html, minify_css=True, minify_js=True)
    fs_util.make_dirs_if_not_exists(path_define.build_html_dir)
    html_file_path = os.path.join(path_define.build_html_dir, f'{name}.html')
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html)
    logger.info(f'make {html_file_path}')


def make_tool_1_html_file():
    matrix = []
    for initial_consonant_index, _ in enumerate(hangul_util.initial_consonants):
        for vowel_index, _ in enumerate(hangul_util.vowels):
            line = [chr(hangul_util.get_syllable_code_point(initial_consonant_index, vowel_index))]
            for final_consonant_index, _ in enumerate(hangul_util.final_consonants):
                line.append(chr(hangul_util.get_syllable_code_point(initial_consonant_index, vowel_index, final_consonant_index)))
            matrix.append(line)
    _make_tool_html_file(matrix, 'tool-1')


def make_tool_2_html_file():
    matrix = []
    for initial_consonant_index, _ in enumerate(hangul_util.initial_consonants):
        line = []
        for vowel_index, _ in enumerate(hangul_util.vowels):
            line.append(chr(hangul_util.get_syllable_code_point(initial_consonant_index, vowel_index)))
        matrix.append(line)
    _make_tool_html_file(matrix, 'tool-2')
