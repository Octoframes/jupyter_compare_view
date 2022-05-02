from base64 import b64decode
from io import BytesIO, StringIO
from pathlib import Path

import PIL
from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.display import display
from IPython.utils.capture import capture_output
from IPython.core.display import HTML


@magics_class
class SplitViewMagic(Magics):
    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
        "--path",
        "-p",
        default=Path.cwd(),
        help=("the path where the image will be saved to"),
    )
    @cell_magic
    def splity(self, line, cell):
        """Saves the png image and the css style for the html page"""
        args = magic_arguments.parse_argstring(SplitViewMagic.splity, line)
        path = args.path

        # save the output
        with capture_output(stdout=False, stderr=False, display=True) as result:
            self.shell.run_cell(cell)

        # print(result.outputs)
        # save image
        num = 0
        filenames = []
        for output in result.outputs:
            # display(output)
            data = output.data
            if "image/png" in data:
                png_bytes = data["image/png"]
                if isinstance(png_bytes, str):
                    png_bytes = b64decode(png_bytes)
                assert isinstance(png_bytes, bytes)
                bytes_io = BytesIO(png_bytes)
                image = PIL.Image.open(bytes_io)
                filename = path / f"splitview_image_{num}.png"
                image.save(filename, "png")
                filenames.append(filename)
                num += 1

        html_code = f"""
        <div class= "outer_layer" style = "position: relative; padding-top: 300px"   >
        <div class="juxtapose" data-startingposition="35%" style = "height: 400px; width: 400px; top: 1%; left: 1%; position: absolute;"  >
            <img src="{filenames[0].name}" />  <!-- here, the image path is loaded by acceccing it with an f-string, so cool! -->
            <img src="{filenames[1].name}" />
        </div>

        </div>
        <script src="https://cdn.knightlab.com/libs/juxtapose/latest/js/juxtapose.min.js"></script>
        <link rel="stylesheet" href="https://cdn.knightlab.com/libs/juxtapose/latest/css/juxtapose.css">
        <script>
        var el = document.getElementById('knightlab-logo');
        el.remove(); 
        </script>

        <style>
        .knightlab-logo {{
            color: blue;
        }}
            </style>
        """
        display(HTML(html_code))