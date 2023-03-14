from IPython import get_ipython
import importlib.metadata
from .compare import compare, StartMode
from .sw_cellmagic import CompareViewMagic

__version__: str = importlib.metadata.version(__name__)


try:
    ipy = get_ipython()
    ipy.register_magics(CompareViewMagic)
    print(f"Jupyter compare_view v{__version__}")
except AttributeError:
    print("Can not load CompareViewMagic because this is not a notebook")
