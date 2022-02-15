from .main import whitify_wrapper
import click


@click.command()
@click.argument("png_path", type=click.Path(exists=True), required=True)
def whitify(png_path):
    whitify_wrapper(png_path)


if __name__ == "__main__":
    whitify()
