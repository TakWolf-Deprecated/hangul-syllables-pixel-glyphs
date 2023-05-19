# 谚文音节像素字形

Unicode 区块「谚文音节（Hangul Syllables; AC00-D7AF）」的像素字形生成程序，目前支持 10、12 和 16 像素。

该项目是 [方舟像素字体](https://github.com/TakWolf/ark-pixel-font) 对应区块的字形解决方案。

## 预览

TODO

## 原理

一个谚文音节由初声辅音（声母）、中声元音（韵母）和终声辅音（韵尾）三个部分组成。

- 初声辅音（声母），共 19 个

```text
ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ
```

- 中声元音（韵母），共 21 个

```text
ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ
```

- 终声辅音（韵尾），共 27 个

```text
ㄱ ㄲ ㄳ ㄴ ㄵ ㄶ ㄷ ㄹ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅁ ㅂ ㅄ ㅅ ㅆ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ
```

声母和韵母一定存在，韵尾可以没有。每个音节，将声部按照“从左到右，自上而下”的方式组合而成。

在 Unicode 区块中，谚文音节按照规律依次排列。也就是说，按照上面的顺序进行排列组合，即可遍历全部的 `19 * 21 * (27 + 1) = 11172` 个音节字符。

## 构建

该项目是一个标准 Python 3 项目。

运行 `build.py` 开始构建，生成的字形图片位于 `build/glyphs` 目录。

## 授权信息

分为「字形」和「程序」两个部分。

### 字形

属于 [方舟像素字体](https://github.com/TakWolf/ark-pixel-font) 的一部分，遵循其 [字体许可证](https://github.com/TakWolf/ark-pixel-font#授权信息) 。

### 程序

使用 [MIT 许可证](LICENSE) 授权。

## 程序依赖

- [Jinja](https://github.com/pallets/jinja)
- [PyPNG](https://gitlab.com/drj11/pypng)
