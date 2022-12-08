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
    def source_cfg(self):
        template = self.environment.get_template('source_cfg.c.jinja2')
        return template.render(**self.config)

    @property
    def header_cfg(self):
        template = self.environment.get_template('header_cfg.h.jinja2')
        return template.render(**self.config)

    @property
    def source_pb_cfg(self):
        template = self.environment.get_template('source_pb_cfg.c.jinja2')
        return template.render(**self.config)

    @property
    def header_pb_cfg(self):
        template = self.environment.get_template('header_pb_cfg.h.jinja2')
        return template.render(**self.config)

    @property
    def source_rt(self):
        template = self.environment.get_template('source_rt.c.jinja2')
        return template.render(**self.config)

    @property
    def header_rt(self):
        template = self.environment.get_template('header_rt.h.jinja2')
        return template.render(**self.config)
