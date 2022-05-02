from .sw_cellmagic import SplitViewMagic
from IPython import get_ipython  # register cell magic
import pkg_resources

__version__: str = pkg_resources.get_distribution(__name__).version

print(f"Jupyter Splitview v{__version__}")
ipy = get_ipython()
ipy.register_magics(SplitViewMagic)