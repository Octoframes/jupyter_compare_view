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

    css_abs = os.path.join((os.path.dirname(__file__)), "../vendor/juxtapose/build/css/juxtapose.css")
    js_abs = os.path.join((os.path.dirname(__file__)), "../vendor/juxtapose/build/js/juxtapose.min.js")
    css_rel = os.path.relpath(css_abs)
    js_rel = os.path.relpath(js_abs)

    display(HTML(f"""
        <link rel="stylesheet" href="/files{css_rel}" type="text/css"/>
        <script src="/files{js_rel}"></script>
    """))

except AttributeError:
    print("Can not load SplitViewMagic because this is not a notebook")


