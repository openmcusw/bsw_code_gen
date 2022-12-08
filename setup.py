import os.path

from setuptools import setup

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'requirements.txt')), 'r') as fp:
    install_requires = fp.read().splitlines()

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'README.md')), 'r') as fp:
    long_description = fp.read()

setup(
    name='bsw_code_gen',
    version='0.1.5',
    packages=['bsw_code_gen'],
    url='https://github.com/openmcusw/bsw_code_gen',
    license='BSD-2',
    author='Guillaume Sottas',
    author_email='guillaumesottas@gmail.com',
    description='Generic code generator used to generate C sources and headers of BSW modules',
    long_description=long_description,
    entry_points={
        'console_scripts': ['bsw_code_gen=bsw_code_gen:main']
    },
    install_requires=install_requires,
)
