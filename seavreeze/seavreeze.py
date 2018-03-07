import argparse

from . import render


def main():
    parser = argparse.ArgumentParser(description='Render a Jinja2 template.')
    parser.add_argument('-t', '--template',
                        required=True,
                        help='Jinja2 template to render')
    parser.add_argument('-d', '--data', type=argparse.FileType('r'),
                        required=True,
                        help='YAML file containing template context')
    parser.add_argument('-f', '--format',
                        choices=render.ARG_TO_ENV_KWARGS.keys(),
                        required=True)
    parser.add_argument('-o', '--output', type=argparse.FileType('w'),
                        required=True,
                        help='File to output to')
    args = parser.parse_args()
    render.render(args.template, args.data, args.output, args.format)


if __name__ == '__main__':
    main()
