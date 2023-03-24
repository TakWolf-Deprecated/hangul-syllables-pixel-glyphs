from jinja2 import Environment, FileSystemLoader

from configs import path_define

font_sizes = [10, 12, 16]

template_env = Environment(
    trim_blocks=True,
    lstrip_blocks=True,
    loader=FileSystemLoader(path_define.templates_dir),
)
