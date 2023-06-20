import logging
import os
from typing import Iterator

import png

from configs import path_define
from utils import fs_util, hangul_util

logger = logging.getLogger('glyph-service')


def _load_glyph_data_from_png(file_path: str) -> tuple[list[list[int]], int, int]:
    width, height, bitmap, _ = png.Reader(filename=file_path).read()
    data = []
    for bitmap_row in bitmap:
        data_row = []
        for x in range(0, width * 4, 4):
            alpha = bitmap_row[x + 3]
            if alpha > 127:
                data_row.append(1)
            else:
                data_row.append(0)
        data.append(data_row)
    return data, width, height


def _save_glyph_data_to_png(data: list[list[int]], file_path: str):
    bitmap = []
    for data_row in data:
        bitmap_row = []
        for x in data_row:
            bitmap_row.append(0)
            bitmap_row.append(0)
            bitmap_row.append(0)
            if x == 0:
                bitmap_row.append(0)
            else:
                bitmap_row.append(255)
        bitmap.append(bitmap_row)
    png.from_array(bitmap, 'RGBA').save(file_path)


def _walk_jamo_dirs() -> Iterator[tuple[str, hangul_util.JamoType, hangul_util.HeightMode | None, hangul_util.MedialPlacementMode | None]]:
    for jamo_type in hangul_util.JamoType:
        if jamo_type == hangul_util.JamoType.INITIAL:
            for height_mode in hangul_util.HeightMode:
                for placement_mode in hangul_util.MedialPlacementMode:
                    for jamo in hangul_util.INITIAL_JAMOS:
                        jamo_file_dir_name = os.path.join(jamo_type, height_mode, placement_mode, jamo)
                        yield jamo_file_dir_name, jamo_type, height_mode, placement_mode
        elif jamo_type == hangul_util.JamoType.MEDIAL:
            for height_mode in hangul_util.HeightMode:
                for jamo in hangul_util.MEDIAL_JAMOS:
                    placement_mode = hangul_util.MedialPlacementMode.get_by_jamo(jamo)
                    jamo_file_dir_name = os.path.join(jamo_type, height_mode, placement_mode, jamo)
                    yield jamo_file_dir_name, jamo_type, height_mode, placement_mode
        elif jamo_type == hangul_util.JamoType.FINAL:
            height_mode = None
            placement_mode = None
            for jamo in hangul_util.FINAL_JAMOS:
                jamo_file_dir_name = os.path.join(jamo_type, jamo)
                yield jamo_file_dir_name, jamo_type, height_mode, placement_mode


def format_jamo_files(font_size: int):
    root_dir = os.path.join(path_define.jamos_dir, str(font_size))
    tmp_dir = os.path.join(path_define.jamos_tmp_dir, str(font_size))
    fs_util.delete_dir(tmp_dir)
    for jamo_file_dir_name, jamo_type, height_mode, placement_mode in _walk_jamo_dirs():
        jamo_file_from_dir = os.path.join(root_dir, jamo_file_dir_name)
        jamo_file_to_dir = os.path.join(tmp_dir, jamo_file_dir_name)
        fs_util.make_dirs(jamo_file_to_dir)

        # TODO
    fs_util.delete_dir(root_dir)
    os.rename(tmp_dir, root_dir)


class DesignContext:
    def __init__(
            self,
            font_size: int,
    ):
        self.font_size = font_size
        self.glyphs_dir = os.path.join(path_define.glyphs_dir, str(font_size))


def collect_jamo_files(font_size: int) -> DesignContext:
    # TODO
    return DesignContext(font_size)


def _make_syllable_glyph(context: DesignContext, initial_index: int, medial_index: int, final_index: int = None):
    # TODO
    pass

    
def make_glyph_files(context: DesignContext):
    fs_util.delete_dir(context.glyphs_dir)
    fs_util.make_dirs(context.glyphs_dir)

    for initial_index in range(len(hangul_util.INITIAL_JAMOS)):
        for medial_index in range(len(hangul_util.MEDIAL_JAMOS)):
            _make_syllable_glyph(context, initial_index, medial_index)
            for final_index in range(len(hangul_util.FINAL_JAMOS)):
                _make_syllable_glyph(context, initial_index, medial_index, final_index)
