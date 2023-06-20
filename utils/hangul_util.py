from enum import StrEnum
from typing import Final

# 初声辅音（声母）共 19 个
INITIAL_JAMOS: Final[list[str]] = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 中声元音（韵母）共 21 个
MEDIAL_JAMOS: Final[list[str]] = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

# 终声辅音（韵尾）共 27 个
FINAL_JAMOS: Final[list[str]] = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 音节总数
SYLLABLES_COUNT: Final[int] = len(INITIAL_JAMOS) * len(MEDIAL_JAMOS) * (len(FINAL_JAMOS) + 1)
assert SYLLABLES_COUNT == 11172

# 区块范围
BLOCK_START: Final[int] = 0xAC00
BLOCK_END: Final[int] = 0xD7AF


def get_code_point(initial_index: int, medial_index: int, final_index: int = None) -> int:
    code_point = BLOCK_START
    code_point += initial_index * len(MEDIAL_JAMOS) * (len(FINAL_JAMOS) + 1)
    code_point += medial_index * (len(FINAL_JAMOS) + 1)
    if final_index is not None:
        code_point += final_index + 1
    return code_point


class JamoType(StrEnum):
    INITIAL = 'initial'
    MEDIAL = 'medial'
    FINAL = 'final'


class HeightMode(StrEnum):
    FULL = 'full-height'
    HALF = 'half-height'


class MedialPlacementMode(StrEnum):
    VERTICAL = 'vertical'
    HORIZONTAL = 'horizontal'
    WRAPPING = 'wrapping'

    @staticmethod
    def get_by_jamo(jamo: str) -> 'MedialPlacementMode':
        if jamo in ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅣ']:
            return MedialPlacementMode.VERTICAL
        elif jamo in ['ㅗ', 'ㅛ', 'ㅜ', 'ㅟ', 'ㅠ', 'ㅡ']:
            return MedialPlacementMode.HORIZONTAL
        elif jamo in ['ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ']:
            return MedialPlacementMode.WRAPPING
        else:
            raise AssertionError

    @staticmethod
    def get_by_jamo_index(index: int) -> 'MedialPlacementMode':
        return MedialPlacementMode.get_by_jamo(MEDIAL_JAMOS[index])
