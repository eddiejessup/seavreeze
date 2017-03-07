import yaml

import jinja2


def get_html_jinja_env():
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader('.'),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def get_tex_jinja_env():
    return jinja2.Environment(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='<<',
        variable_end_string='>>',
        comment_start_string='<#',
        comment_end_string='#>',
        loader=jinja2.FileSystemLoader('.'),
    )


def render(env, template_file, data_file, output_file):
    template = env.get_template(template_file)
    with data_file as f:
        context = yaml.safe_load(f)
    with output_file as f:
        f.write(template.render(**context))
