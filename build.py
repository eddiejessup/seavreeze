import argparse

import cv_lib


arg_to_get_env_func_map = {
    'html': cv_lib.get_html_jinja_env,
    'tex': cv_lib.get_tex_jinja_env,
}


parser = argparse.ArgumentParser(description='Render a Jinja2 template.')
parser.add_argument('-t', '--template',
                    required=True,
                    help='Jinja2 template to render')
parser.add_argument('-d', '--data', type=argparse.FileType('r'),
                    required=True,
                    help='YAML file containing template context')
parser.add_argument('-f', '--format', choices=arg_to_get_env_func_map.keys(),
                    required=True,
                    help='YAML file containing template context')
parser.add_argument('-o', '--output', type=argparse.FileType('w'),
                    required=True,
                    help='File to output to')

args = parser.parse_args()

get_jinja_env_func = arg_to_get_env_func_map[args.format]
env = get_jinja_env_func()
cv_lib.render(env, args.template, args.data, args.output, args.format)
