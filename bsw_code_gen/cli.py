import argparse
import os

from .generator import BSWCodeGen
from json import load
from jsonschema import validate


def main():
    parser = argparse.ArgumentParser(prog='bsw_code_gen',
                                     description='Autosar BSW configuration code generator',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('configuration', type=argparse.FileType('r'), help='JSON input configuration file path')
    parser.add_argument('-source_cfg', type=argparse.FileType('wb'), help='output path of <module_name>_Cfg.c file')
    parser.add_argument('-header_cfg', type=argparse.FileType('wb'), help='output path of <module_name>_Cfg.h file')
    parser.add_argument('-source_pb_cfg',
                        type=argparse.FileType('wb'),
                        help='output path of <module_name>_PBcfg.c file')
    parser.add_argument('-header_pb_cfg',
                        type=argparse.FileType('wb'),
                        help='output path of <module_name>_PBcfg.h file')
    parser.add_argument('-source_rt',
                        type=argparse.FileType('wb'),
                        help='output path of <module_name>_Rt.c file')
    parser.add_argument('-header_rt',
                        type=argparse.FileType('wb'),
                        help='output path of <module_name>_Rt.h file')
    parser.add_argument('-schema', help='JSON validation schema file path')
    parser.add_argument('-template_directory', type=str, default=os.getcwd(), help='jinja2 template directory')

    args = parser.parse_args()

    data = load(args.configuration)

    if args.schema:
        with open(args.schema, 'r') as fp:
            validate(data, load(fp))

    code_generator = BSWCodeGen(data, args.template_directory)

    if args.source_cfg:
        args.source_cfg.write(code_generator.source_cfg.encode())
    if args.header_cfg:
        args.header_cfg.write(code_generator.header_cfg.encode())
    if args.source_pb_cfg:
        args.source_pb_cfg.write(code_generator.source_pb_cfg.encode())
    if args.header_pb_cfg:
        args.header_pb_cfg.write(code_generator.header_pb_cfg.encode())
    if args.source_rt:
        args.source_rt.write(code_generator.source_rt.encode())
    if args.header_rt:
        args.header_rt.write(code_generator.header_rt.encode())


if __name__ == '__main__':
    main()
