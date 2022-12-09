import base64
import enum
import io
import json
import typing
import uuid
from pathlib import Path
from jinja2 import Template, StrictUndefined
import IPython
import PIL


ImageLike = typing.TypeVar('ImageLike')
ImageSource = typing.Union[str, bytes, ImageLike]


def img2bytes(img: ImageLike, format: str, cmap: str) -> bytes:
    with io.BytesIO() as im_file:
        if isinstance(img, PIL.Image.Image):
            img.save(im_file, format=format)
        else:
            # anything other that can be displayed with plt.imshow
            import matplotlib.pyplot as plt

            plt.imsave(im_file, img, format=format, cmap=cmap)
        return im_file.getvalue()


def img2url(img: ImageSource, format: str, cmap: str) -> str:
    if isinstance(img, str):
        return img.strip()
    if isinstance(img, bytes):
        data = img
    else:
        data = img2bytes(img, format=format, cmap=cmap)
    return f"data:image/{format};base64,{str(base64.b64encode(data), 'utf8')}"


def compile_template(in_file: str, **variables) -> str:
    with open(in_file, "r", encoding="utf-8") as file:
        template = Template(file.read(), undefined=StrictUndefined)
    return template.render(**variables)


def prepare_html(image_urls: typing.List[str], height: str, add_controls: bool, config: dict) -> str:
    uid=uuid.uuid1()
    config['key'] = str(uid)
    if add_controls:
        config["controls_id"] = f"controls_{uid}"
    root = Path(__file__).parent
    js_path = root / "../vendor/compare_view/browser_compare_view.js"
    js = js_path.read_text()
    return compile_template(
        root / "template.html",
        uid=uid,
        image_urls=image_urls,
        height=height,
        js=js,
        add_controls=add_controls,
        config=json.dumps(config),
    )


@enum.unique
class StartMode(str, enum.Enum):
    CIRCLE = "circle"
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


def compare(
    image1: ImageSource,
    image2: ImageSource,
    *other_images: ImageSource,
    height: typing.Union[str, int] = 'auto',
    add_controls: bool = True,
    start_mode: typing.Union[StartMode, str] = StartMode.CIRCLE,
    circumference_fraction: float = 0.005,
    circle_size: typing.Optional[float] = None,
    circle_fraction: float = 0.2,
    show_circle: bool = True,
    revolve_imgs_on_click: bool = True,
    slider_fraction: float = 0.01,
    slider_time: float = 400,
    # rate_function: str = 'ease_in_out_cubic',
    start_slider_pos: float = 0.5,
    show_slider: bool = True,
    display_format: str = 'jpeg',
    cmap: typing.Optional[str] = None,
) -> IPython.display.HTML:
    """
    Args:
        height: height of the widget in pixels or "auto"
        add_controls: pass False to not create controls
        start_mode: either "circle", "horizontal" or "vertical"
        circumference_fraction: size of circle outline as fraction of image width or height (whatever is bigger)
        circle_size: the radius in pixel
        circle_fraction: a fraction of the image width or height (whichever is bigger—called max_size in this document)
        show_circle: draw line around circle
        slider_time: time slider takes to reach clicked location
        start_slider_pos: 0.0 -> left; 1.0 -> right
        show_slider: draw line at slider
        display_format: format used for displaying images
        cmap: colormap for grayscale images
    """
    images = [image1, image2, *other_images]
    image_urls = [
        img2url(img, format=display_format, cmap=cmap) for img in images
    ]
    _locals = locals()
    config = {k: _locals[k] for k in [
            'start_mode',
            'circumference_fraction',
            'circle_fraction',
            'show_circle',
            'revolve_imgs_on_click',
            'slider_fraction',
            'slider_time',
            # 'rate_function',
            'start_slider_pos',
            'show_slider',
        ]
        + ['circle_size'] * (circle_size is not None)
    }
    html = prepare_html(
        image_urls=image_urls,
        height=f'{height}px' if not isinstance(height, str) else height,
        add_controls=add_controls,
        config=config,
    )
    return IPython.display.HTML(html)
