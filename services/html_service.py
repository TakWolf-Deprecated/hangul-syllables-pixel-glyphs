import logging
import os

import minify_html

import configs
from configs import path_define
from utils import hangul_util, fs_util

logger = logging.getLogger('html-service')


def make_tool_1_html_file():
    matrix = []
    code_point = hangul_util.unicode_block_start
    syllables_count = 0
    for _ in hangul_util.initial_consonants:
        for _ in hangul_util.vowels:
            line = [chr(code_point)]
            code_point += 1
            syllables_count += 1
            for _ in hangul_util.final_consonants:
                line.append(chr(code_point))
                code_point += 1
                syllables_count += 1
            matrix.append(line)
    assert syllables_count == hangul_util.syllables_count

    template = configs.template_env.get_template('tool.html')
    html = template.render(matrix=matrix)
    html = minify_html.minify(html, minify_css=True, minify_js=True)
    fs_util.make_dirs_if_not_exists(path_define.build_html_dir)
    html_file_path = os.path.join(path_define.build_html_dir, 'tool-1.html')
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html)
    logger.info(f'make {html_file_path}')
