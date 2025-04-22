import os
import argparse
from PIL import Image

class ColorChanger:
    def change_gray(self, img_path, output_path):
        """
        指定した画像をグレースケールに変換する
        Args:
            img_path (str): 画像のパス
            output_path (str): 変換後の画像のパス
        """
        img = Image.open(img_path)
        gray_img = img.convert('L')

        gray_img.save(output_path)

if __name__ == '__main__':
    # パーサーの作成
    parser = argparse.ArgumentParser(description='コマンドライン引数の例')
    # 引数の定義
    parser.add_argument('--img_path', type=str, help='処理対象の画像パス')
    # 引数を解析
    args = parser.parse_args()

    dir_path = os.path.dirname(args.img_path)
    img_name = os.path.basename(args.img_path)

    output_path = os.path.join(dir_path, f"{img_name}_gray.png")

    color_changer = ColorChanger()
    color_changer.change_gray(args.img_path, output_path)