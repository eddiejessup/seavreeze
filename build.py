import jinja2
import yaml
import argparse


parser = argparse.ArgumentParser(description='Render a Jinja2 template.')
parser.add_argument('-t', '--template',
                    help='Jinja2 template to render')
parser.add_argument('-d', '--data', type=argparse.FileType('r'),
                    help='YAML file containing template context')
parser.add_argument('-o', '--output', type=argparse.FileType('w'),
                    help='File to output to')

args = parser.parse_args()


env = jinja2.Environment(
    block_start_string='<%',
    block_end_string='%>',
    variable_start_string='<<',
    variable_end_string='>>',
    comment_start_string='<#',
    comment_end_string='#>',
    loader=jinja2.FileSystemLoader('.')
)

template = env.get_template(args.template)
with args.data as f:
    context = yaml.safe_load(f)
with args.output as f:
    f.write(template.render(**context))
