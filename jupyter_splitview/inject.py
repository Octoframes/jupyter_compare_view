import json
import os
import uuid
from pathlib import Path
from jinja2 import Template, StrictUndefined
from IPython.core.display import HTML, JSON
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
    js = sanitise_injection(js_path.read_text())

    html_code = compile_template(
        os.path.join((os.path.dirname(__file__)), "inject_dependencies.html"),
        js=js,
    )
    display(HTML(html_code))


def inject_split(image_urls, height, config) -> None:
    key=uuid.uuid1()
    # inject controls id and key -> only Config remaining, not BrowserConfig for compare_view
    # TODO: come up with better solution
    config_parsed = json.loads(config.strip("'").strip('"'))
    config_parsed["controls_id"] = f"controls_{key}"
    config_parsed["key"] = str(key)
    html_code = compile_template(
        os.path.join((os.path.dirname(__file__)), "inject_split.html"),
        key=key,
        image_urls=image_urls,
        height=height,
        config=json.dumps(config_parsed),
    )
    display(HTML(html_code))
    # ensure to include the sources every time
    inject_dependencies()

