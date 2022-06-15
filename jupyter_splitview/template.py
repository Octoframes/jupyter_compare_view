from jinja2 import Template, StrictUndefined

def compile_template(in_file: str, **variables) -> str:
    with open(f"{in_file}", "r", encoding="utf-8") as file:
        template = Template(file.read(), undefined=StrictUndefined)
    return template.render(**variables)

