from base64 import b64decode
from pathlib import Path

from IPython.core import magic_arguments
from IPython.core.display import HTML
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.display import display
from IPython.utils.capture import capture_output

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
        """Saves the png image and calls the splitview canvas"""
        args = magic_arguments.parse_argstring(SplitViewMagic.splity, line)
        path = args.path

        # save the output
        with capture_output(stdout=False, stderr=False, display=True) as result:
            self.shell.run_cell(cell)

        # save image
        filenames = []
        for output in result.outputs:
            data = output.data
            if "image/png" in data:
                png_bytes_data = data["image/png"]                
                filenames.append(png_bytes_data)

        html_code = f"""
        <div class= "outer_layer" style = "position: relative; padding-top: 300px"   >
        <div class="juxtapose" data-startingposition="35%" style = "height: 400px; width: 400px; top: 1%; left: 1%; position: absolute;"  >
            <img src="data:image/jpeg;base64,{filenames[0]}">'
            <img src="data:image/jpeg;base64,{filenames[1]}">'
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