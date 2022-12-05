import io
import json

from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.utils.capture import capture_output
from PIL import Image

from .compare import compare


@magics_class
class CompareViewMagic(Magics):
    @magic_arguments.magic_arguments()
    @magic_arguments.argument(  # TODO This is currently not used.
        "--position",
        "-p",
        default="50%",
        help="""The start position of the slider. Currently not implemented, use `--config '{"start_slider_pos": 0.73}'` instead""",
    )
    @magic_arguments.argument(
        "--height",
        "-h",
        default="auto",
        help=(
            "The widget's height. The width will be adjusted automatically. \
             If height is `auto`, the vertical resolution of the first image is used."
        ),
    )
    @magic_arguments.argument(
        "--config",
        "-c",
        default="{}",
        help=(
            "The compare view config as described here: https://github.com/Octoframes/compare_view"
        ),
    )
    @cell_magic
    def compare(self, line, cell):  # TODO: make a %%splity deprecated version
        """Saves the png image and creates the compare_view canvas"""

        with capture_output(stdout=False, stderr=False, display=True) as result:
            self.shell.run_cell(cell)

        # saves all jupyter output images into the out_images_base64 list
        out_images_base64 = []
        for output in result.outputs:
            data = output.data
            if "image/png" in data:
                png_bytes_data = data["image/png"]
                if isinstance(png_bytes_data, str):
                    png_bytes_data = f'data:image/png;base64,{png_bytes_data}'
                out_images_base64.append(png_bytes_data)
        if len(out_images_base64) < 2:
            raise ValueError(
                "There need to be at least two images for Jupyter compare_view to work."
            )

        # get the parameters that configure the widget
        args = magic_arguments.parse_argstring(CompareViewMagic.compare, line)
        height = args.height

        return compare(
            *out_images_base64,
            **{
                **json.loads(args.config.strip("'").strip('"')),
                "height": height if height == "auto" else int(height)
            }
        )

    @cell_magic
    def splity(self, line, cell):  # TODO: Delete this somewhere 10/2022.
        import warnings

        print(
            """
**************************************************************
Warning: %%splity is deprecated. Please use %%compare instead.
**************************************************************
"""
        )
        new_line = "%%compare"
        new_line += line
        complete_cell = new_line + "\n" + cell
        self.shell.run_cell(complete_cell)
