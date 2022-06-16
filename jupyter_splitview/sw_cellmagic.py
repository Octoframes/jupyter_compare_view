import io
from base64 import b64decode

from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.utils.capture import capture_output
from PIL import Image

from .inject import inject_split

g_cell_id = 0


@magics_class
class SplitViewMagic(Magics):
    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
        "--position",
        "-p",
        default="50%",
        help=("The start position of the slider"),
    )
    @magic_arguments.argument(
        "--height",
        "-h",
        default="300",
        help=(
            "The widget's height. The width will be adjusted automatically. \
             If height is `auto`, the vertical resolution of the first image is used."
        ),
    )
    @cell_magic
    def splity(self, line, cell):
        """Saves the png image and calls the splitview canvas"""

        with capture_output(stdout=False, stderr=False, display=True) as result:
            self.shell.run_cell(cell)

        # saves all jupyter output images into the out_images_base64 list
        out_images_base64 = []
        for output in result.outputs:
            data = output.data
            if "image/png" in data:
                png_bytes_data = data["image/png"]
                out_images_base64.append(png_bytes_data)

        # get the parameters that configure the widget
        args = magic_arguments.parse_argstring(SplitViewMagic.splity, line)

        slider_position = args.position
        widget_height = args.height

        if widget_height == "auto":
            imgdata = b64decode(out_images_base64[0])
            # maybe possible without the PIL dependency?
            im = Image.open(io.BytesIO(imgdata))
            widget_height = im.size[1]

        image_data_urls = [f"data:image/jpeg;base64,{base64.strip()}" for base64 in out_images_base64]

        # every juxtapose html node needs unique id
        global g_cell_id
        inject_split(
            cell_id=g_cell_id,
            image_data_urls=image_data_urls,
            slider_position=slider_position,
            wrapper_height=int(widget_height)+4,
            height=int(widget_height),
        )
        g_cell_id += 1

