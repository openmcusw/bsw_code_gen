import argparse
import os

from .bsw_code_gen import BSWCodeGen
from json import load
from jsonschema import validate


def main():
    parser = argparse.ArgumentParser(prog='bsw_code_gen',
                                     description='Autosar BSW configuration code generator',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('configuration', type=argparse.FileType('r'), help='JSON configuration file path')
    parser.add_argument('source', type=argparse.FileType('wb'), help='output source file path')
    parser.add_argument('header', type=argparse.FileType('wb'), help='output header file path')
    parser.add_argument('-schema', help='JSON validation schema file path')
    parser.add_argument('-template_directory', type=str, default=os.getcwd(), help='jinja2 template directory')

    args = parser.parse_args()

    data = load(args.configuration)

    if args.schema:
        with open(args.schema, 'r') as fp:
            validate(data, load(fp))

    code_generator = BSWCodeGen(data, args.template_directory)

    args.source.write(code_generator.source.encode())
    args.header.write(code_generator.header.encode())


if __name__ == '__main__':
    main()
