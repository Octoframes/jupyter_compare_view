from .sw_cellmagic import SplitViewMagic
from IPython import get_ipython
import pkg_resources

from .inject import inject_dependencies

__version__: str = pkg_resources.get_distribution(__name__).version

print(f"Jupyter Splitview v{__version__}")

try:
    ipy = get_ipython()
    ipy.register_magics(SplitViewMagic)

    inject_dependencies()


except AttributeError:
    print("Can not load SplitViewMagic because this is not a notebook")


