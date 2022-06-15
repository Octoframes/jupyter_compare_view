import os
from pathlib import Path

from .sw_cellmagic import SplitViewMagic
from IPython import get_ipython
from IPython.core.display import HTML
from IPython.display import display
import pkg_resources

from .template import compile_template

__version__: str = pkg_resources.get_distribution(__name__).version

# injection is used in "" string in JavaScript -> some characters need to be escaped
def sanitise_injection(inject: str) -> str:
    return inject.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "\\n")


def inject_dependencies() -> None:
    css_path = Path(__file__).parents[1] / "vendor/juxtapose/build/css/juxtapose.css"
    js_path = Path(__file__).parents[1] / "vendor/juxtapose/build/js/juxtapose.min.js"

    html_code = compile_template(
        os.path.join((os.path.dirname(__file__)), "inject_dependencies.html"),
        juxtapose_css = sanitise_injection(css_path.read_text()),
        juxtapose_js = sanitise_injection(js_path.read_text()),
    )
    display(HTML(html_code))


print(f"Jupyter Splitview v{__version__}")

try:
    ipy = get_ipython()
    ipy.register_magics(SplitViewMagic)

    inject_dependencies()


except AttributeError:
    print("Can not load SplitViewMagic because this is not a notebook")


