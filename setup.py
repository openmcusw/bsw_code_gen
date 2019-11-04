from setuptools import setup

setup(
    name='bsw_code_gen',
    version='0.1.0',
    packages=['bsw_code_gen'],
    url='https://github.com/openmcusw/bsw_code_gen',
    license='BSD-2',
    author='Guillaume Sottas',
    author_email='guillaumesottas@gmail.com',
    description='Generic code generator used to generate C sources and headers of BSW modules',
    entry_points={
        'console_scripts': ['bsw_code_gen=bsw_code_gen:main']
    },
    install_requires=['jinja2',
                      'jsonschema'],
)
