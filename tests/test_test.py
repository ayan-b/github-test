import jinja2
import pytest

PATH_TO_TEMPLATES = './templates'


def get_rendered_file():
    context = {
        'var': 'dummy-0.0.0'
    }
    filename = 'hello.py.jj2'
    rendered = jinja2.Environment(
        loader=jinja2.FileSystemLoader(PATH_TO_TEMPLATES)
    ).get_template(filename).render(context)
    return rendered

def test_underscore_replacement():
    rendered = get_rendered_file()
    assert 'dummy-0.0.0' in rendered
    assert 'dummy_0.0.0' not in rendered
