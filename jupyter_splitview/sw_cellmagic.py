import io
from base64 import b64decode

from IPython.core import magic_arguments
from IPython.core.display import HTML
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.display import display
from IPython.utils.capture import capture_output
from PIL import Image


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

        html_code = """
    <div id="foo"></div>

    <script>
        slider = new juxtapose.JXSlider('#foo',
            [
                {
                    src: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.TJNo8135ZBrLCojdcdtNoQHaHa%26pid%3DApi&f=1',
                },
                {
                    src: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.Yh4sZ7LKCEGMYlmmNnxYawHaHa%26pid%3DApi&f=1',
                }
            ],
            {
                animate: true,
                showLabels: false,
                showCredits: false,
                startingPosition: "50%",
                makeResponsive: true,
                // undocumented shit
                callback: (jx_slider) => {
                    // remove juxtapose.js link and logo in bottom left corner
                    jx_slider.slider.removeChild(jx_slider.labCredit);
                },
            });
    </script>
        """
        display(HTML(html_code))
        
