# Pyxel Color Converter

Pyxel Color Converterは、任意の画像を[Pyxel](https://github.com/kitao/pyxel)で利用可能な16色のパレットに変換するツールです。

## 使い方

Python 3と、`PIL`、`numpy` ライブラリが必要です。

画像を変換するには、以下のコマンドをターミナル（コマンドライン）から実行してください。

```bash
python pyxel_color_converter.py input_image.png
```

ここで、input_image.pngは変換したい画像のファイル名（パス）です。同じディレクトリに converted_image.pngという名前で新しい画像が作成されます。新しい画像は、Pyxel の 16 色のパレットに変換されます。

さらに、画像の縦または横が256ピクセルを超える場合、画像をリサイズすることもできます。この場合、以下のように--resizeオプションを使用してください。

```bash
python pyxel_color_converter.py --resize input_image.png
```

---

Pyxel Color Converter is a tool to convert any image to the 16-color palette available in [Pyxel](https://github.com/kitao/pyxel).

## Usage

You need Python 3 and the PIL and numpy libraries.

To convert an image, run the following command from the terminal (command line):

```bash
python pyxel_color_converter.py input_image.png
```

Here, input_image.png is the filename (or path) of the image you want to convert. A new image will be created in the same directory with the name converted_image.png. This new image is converted to the 16-color palette of Pyxel.

Moreover, if the width or height of your image exceeds 256 pixels, you have the option to resize the image. To do so, use the --resize option like this:

```bash
python pyxel_color_converter.py --resize input_image.png
```
