from PIL import Image
from typing import Union
import os


def read_rbga_png(png_path: Union[str, os.PathLike]) -> Image.Image:
    png_alpha = Image.open(png_path)
    png_alpha.load()
    return png_alpha


def remove_png_alpha_channel(png_alpha: Image.Image) -> Image.Image:
    png = Image.new("RGB", png_alpha.size, (255, 255, 255))
    png.paste(png_alpha, mask=png_alpha.split()[3])
    return png


def whitify_wrapper(png_path: Union[str, os.PathLike]):
    png = read_rbga_png(png_path)
    png = remove_png_alpha_channel(png)
    png.save(png_path, "PNG")
