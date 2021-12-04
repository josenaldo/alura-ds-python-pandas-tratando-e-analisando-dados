import pprint
from IPython.display import display, Markdown


def print_pretty(dictionary):
    text = pprint.pformat(dictionary)
    code = f'```python\n{text}\n```'
    md = Markdown(code)
    display(md)
