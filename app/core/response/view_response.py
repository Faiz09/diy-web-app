from jinja2 import Environment, FileSystemLoader
from config.config import get_templates_path


class ViewResponse:
    template = None
    context = None
    headers = None
    mime_type = None

    def __init__(self, template, **context):
        self.template = template
        self.context = context
        self.headers = [(
            'Content-type', 'text/html'
        )]
        self.mime_type = 'text/html'

    def send(self):
        template_path = get_templates_path()
        return Environment(
            loader=FileSystemLoader(template_path),
            autoescape=True
        ).get_template(self.template).render(self.context)