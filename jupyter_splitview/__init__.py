from pathlib import Path

from .sw_cellmagic import SplitViewMagic
from IPython import get_ipython
from IPython.core.display import HTML
from IPython.display import display
import pkg_resources

__version__: str = pkg_resources.get_distribution(__name__).version

print(f"Jupyter Splitview v{__version__}")

try:
    ipy = get_ipython()
    ipy.register_magics(SplitViewMagic)

    css_path = Path(__file__).parents[1] / "vendor/juxtapose/build/css/juxtapose.css"
    js_path = Path(__file__).parents[1] / "vendor/juxtapose/build/js/juxtapose.min.js"

    html_code = f"""
        <style>{css_path.read_text()}</style>
        <script>{js_path.read_text()}</script>
    """
    display(HTML(html_code))


except AttributeError:
    print("Can not load SplitViewMagic because this is not a notebook")


