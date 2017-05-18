import xml.etree.ElementTree as ET


def decode_hidden_html(s):
    return s.replace('‹', '<').replace('›', '>')


def parse_to_cvml_elem(s):
    if '‹' in s or '›' in s:
        raise ValueError('Very sorry, characters "‹" and "›" cannot '
                         'appear in strings that appear to also contain '
                         'CVML content')
    s_transformed = (
        s
        # Hide the HTML brackets while the XML is parsed.
        .replace('<', '‹').replace('>', '›')
        # Make the XML stand-ins into proper brackets.
        .replace('[[', '<').replace(']]', '>')
    )
    # Wrap in outer tags to make into valid XML.
    s_wrapped = f'<t>{s_transformed}</t>'
    try:
        return ET.fromstring(s_wrapped)
    except ET.ParseError as exc:
        raise ValueError('ERROR in string: {s_wrapped}') from exc


def str_contains_cvml(s):
    return '[[' in s and ']]' in s


def expand_cvml_tag_core(mu, lang):
    def expand(elem):
        return expand_cvml_tag(elem, lang=lang)
    if mu.tag == 'link':
        name = expand(mu.find('name'))
        url = expand(mu.find('url'))
        if lang == 'html':
            s = r'<a href="%s">%s</a>' % (url, name)
        elif lang == 'tex':
            s = r'\href{%s}{%s}' % (url, name)
    elif mu.tag == 'mu':
        mu_inner = mu.find(lang)
        if mu_inner.getchildren():
            raise ValueError(f'CVML tag "{mu.tag}/{lang}" cannot have inner '
                             'tags')
        s = mu_inner.text
        if lang == 'html':
            s = decode_hidden_html(s)
    elif mu.tag == 'cite':
        contents = expand(mu)
        if lang == 'tex':
            s = r'\textit{%s}' % contents
        elif lang == 'html':
            s = r'<cite>%s</cite>' % contents
    elif mu.tag == 'small':
        contents = expand(mu)
        if lang == 'tex':
            s = r'\smaller{%s}' % contents
        elif lang == 'html':
            s = r'<small>%s</small>' % contents
    else:
        raise ValueError(f'No CVML tag "{mu.tag}"')
    if mu.tail is not None:
        s += mu.tail
    return s


def expand_cvml_tag(x, lang):
    s = ''
    if x.text is not None:
        s += x.text
    for mu in x.getchildren():
        s_tag = expand_cvml_tag_core(mu, lang)
        s += s_tag
        x.remove(mu)
    return s


def expand_cvml_str(s, lang):
    if str_contains_cvml(s):
        x = parse_to_cvml_elem(s)
        s = expand_cvml_tag(x, lang)
    return s


def process_str_container(node, func):
    if isinstance(node, list):
        key_vals = enumerate(node)
    elif isinstance(node, dict):
        key_vals = node.items()
    else:
        raise ValueError(f'Cannot walk over node of type {type(node)}')
    for key, item in key_vals:
        if isinstance(item, (dict, list)):
            process_str_container(item, func)
        elif isinstance(item, str):
            node[key] = func(item)


def expand_context_inplace(context, lang):
    process_str_container(context,
                          func=lambda s: expand_cvml_str(s, lang=lang))
