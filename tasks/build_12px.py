import logging

from services import glyph_service

logging.basicConfig(level=logging.DEBUG)


def main():
    font_size = 12
    glyph_service.format_jamo_files(font_size)
    context = glyph_service.collect_jamo_files(font_size)
    glyph_service.make_glyph_files(context)


if __name__ == '__main__':
    main()
