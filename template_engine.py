import os
import re

pattern = r'{{(.*?)}}'


def parse_args(obj):
    comp = re.compile(pattern)
    result = comp.findall(obj)
    return result or ()


def replace_template(app, path, **options):
    content = '<h1>Not Found Template.</h1>'
    path = os.path.join(app.template_folder, path)
    print(str(path))
    if os.path.exists(path):
        with open(path, 'rb') as f:
            content = f.read().decode()
        args = parse_args(content)
        if options:
            for arg in args:
                key = arg.strip()
                old_value = '{{{{{}}}}}'.format(arg)
                new_value = str(options.get(key, ''))
                content = content.replace(old_value, new_value)

    return content
