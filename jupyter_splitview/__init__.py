from .sw_cellmagic import SplitViewMagic
from IPython import get_ipython  # register cell magic
import pkg_resources

__version__: str = pkg_resources.get_distribution(__name__).version

def load_ipython_extension(ipython):
  print(f"Registering Jupyter Splitview v{__version__}")
  ipython.register_magics(SplitViewMagic)
