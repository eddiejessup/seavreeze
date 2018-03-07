import yaml
import jinja2

from . import cvml


HTML_JINJA_ENV_KWARGS = dict(
    trim_blocks=True,
    lstrip_blocks=True,
)

TEX_JINJA_ENV_KWARGS = dict(
    block_start_string='<%',
    block_end_string='%>',
    variable_start_string='<<',
    variable_end_string='>>',
    comment_start_string='<#',
    comment_end_string='#>',
)


ARG_TO_ENV_KWARGS = {
    'html': HTML_JINJA_ENV_KWARGS,
    'tex': TEX_JINJA_ENV_KWARGS,
}


def get_jinja_env(lang):
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader('.'),
        **ARG_TO_ENV_KWARGS[lang]
    )


def render(template_file, data_file, output_file, lang):
    env = get_jinja_env(lang)
    template = env.get_template(template_file)
    with data_file as f:
        context = yaml.safe_load(f)
    cvml.expand_context_inplace(context, lang)
    with output_file as f:
        f.write(template.render(**context))
