
# 初声辅音（声母），共 19 个
initial_consonants = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 中声元音（韵母），共 21 个
vowels = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

# 终声辅音（韵尾），共 27 个
final_consonants = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 音节总数
syllables_count = len(initial_consonants) * len(vowels) * (len(final_consonants) + 1)
assert syllables_count == 11172

# 码域范围
unicode_block_start = 0xAC00
unicode_block_end = 0xD7AF


def get_syllable_code_point(initial_consonant_index, vowel_index, final_consonant_index=None):
    """
    根据声母、韵母、韵尾的索引位置获取音节的码位
    """
    code_point = unicode_block_start
    code_point += initial_consonant_index * len(vowels) * (len(final_consonants) + 1)
    code_point += vowel_index * (len(final_consonants) + 1)
    if final_consonant_index is not None:
        code_point += final_consonant_index + 1
    return code_point


def get_vowel_placement_mode(vowel_index):
    """
    获取韵母在音节中的放置模式
    """
    vowel = vowels[vowel_index]
    if vowel in ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅣ']:
        return 'vertical'
    elif vowel in ['ㅗ', 'ㅛ', 'ㅜ', 'ㅟ', 'ㅠ', 'ㅡ']:
        return 'horizontal'
    elif vowel in ['ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ']:
        return 'wrapping'
    else:
        raise Exception(f"'{vowel}' is not a vowel")
