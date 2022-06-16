import os
from pathlib import Path
from jinja2 import Template, StrictUndefined
from IPython.core.display import HTML
from IPython.display import display

def compile_template(in_file: str, **variables) -> str:
    with open(f"{in_file}", "r", encoding="utf-8") as file:
        template = Template(file.read(), undefined=StrictUndefined)
    return template.render(**variables)


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


def inject_split(cell_id, image_data_urls, slider_position, wrapper_height, height) -> None:
    html_code = compile_template(
        os.path.join((os.path.dirname(__file__)), "inject_split.html"),
        cell_id=cell_id,
        image_data_urls=image_data_urls,
        slider_position=slider_position,
        wrapper_height=wrapper_height,
        height=height,
    )
    display(HTML(html_code))
    # ensure to include the sources every time
    inject_dependencies()

