from jinja2 import Environment, FileSystemLoader


class BSWCodeGen(object):
    def __init__(self, config, template_directory):
        self._config = config
        self.environment = Environment(loader=FileSystemLoader(template_directory))

    @property
    def config(self):
        return self._config

    @property
    def source(self):
        template = self.environment.get_template('source.c.jinja2')
        return template.render(**self.config)

    @property
    def header(self):
        template = self.environment.get_template('header.h.jinja2')
        return template.render(**self.config)

    @property
    def source_config(self):
        template = self.environment.get_template('config.c.jinja2')
        return template.render(**self.config)

    @property
    def header_config(self):
        template = self.environment.get_template('config.h.jinja2')
        return template.render(**self.config)
