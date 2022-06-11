import os

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

    css_path = os.path.join((os.path.dirname(__file__)), "../vendor/juxtapose/build/css/juxtapose.css")
    js_path = os.path.join((os.path.dirname(__file__)), "../vendor/juxtapose/build/js/juxtapose.min.js")
    with open(css_path, "r") as file:
        css = file.read()
    with open(js_path, "r") as file:
        js = file.read()

    html_code = f"""
        <style>{css}</style>
        <script>{js}</script>
    """
    display(HTML(html_code))


except AttributeError:
    print("Can not load SplitViewMagic because this is not a notebook")


