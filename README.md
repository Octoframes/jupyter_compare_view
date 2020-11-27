jupyter-splitview
===============================

A splitview widget

Installation
------------

To install use pip:

    $ pip install jupyter-splitview
    $ jupyter nbextension enable --py --sys-prefix jupyter-splitview

To install for jupyterlab

    $ jupyter labextension install jupyter-splitview

For a development installation (requires npm),

    $ git clone https://github.com/kolibril13/jupyter-splitview.git
    $ cd jupyter-splitview
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix jupyter-splitview
    $ jupyter nbextension enable --py --sys-prefix jupyter-splitview
    $ jupyter labextension install js

When actively developing your extension, build Jupyter Lab with the command:

    $ jupyter lab --watch

This takes a minute or so to get started, but then automatically rebuilds JupyterLab when your javascript changes.

Note on first `jupyter lab --watch`, you may need to touch a file to get Jupyter Lab to open.

