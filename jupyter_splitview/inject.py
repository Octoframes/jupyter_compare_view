import os
import uuid
from pathlib import Path
from jinja2 import Template, StrictUndefined
from IPython.core.display import HTML
from IPython.display import display

def compile_template(in_file: str, **variables) -> str:
    with open(in_file, "r", encoding="utf-8") as file:
        template = Template(file.read(), undefined=StrictUndefined)
    return template.render(**variables)


# injection is used in "" string in JavaScript -> some characters need to be escaped
def sanitise_injection(inject: str) -> str:
    return inject.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "\\n")


def inject_dependencies() -> None:
    js_path = Path(__file__).parents[1] / "vendor/compare_view/browser_compare_view.js"
    # TODO: remove
    # js_path = Path("/home/chris/compare_view/public/browser_compare_view.js")
    js = sanitise_injection(js_path.read_text())

    html_code = compile_template(
        os.path.join((os.path.dirname(__file__)), "inject_dependencies.html"),
        js=js,
    )
    display(HTML(html_code))


def inject_split(image_data_urls, slider_position, wrapper_height, width, height) -> None:
    html_code = compile_template(
        os.path.join((os.path.dirname(__file__)), "inject_split.html"),
        rnd_str=uuid.uuid1(),
        image_data_urls=image_data_urls,
        slider_position=slider_position,
        wrapper_height=wrapper_height,
        width=width,
        height=height,
    )
    display(HTML(html_code))
    # ensure to include the sources every time
    inject_dependencies()

