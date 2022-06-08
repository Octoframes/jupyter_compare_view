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
    display(HTML("""
    <link rel="stylesheet" href="https://cdn.knightlab.com/libs/juxtapose/latest/css/juxtapose.css" />
    <script src="https://cdn.knightlab.com/libs/juxtapose/latest/js/juxtapose.min.js"></script>
            """))

except AttributeError:
    print("Can not load SplitViewMagic because this is not a notebook")


