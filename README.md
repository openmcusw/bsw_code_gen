# Package description
The purpose of this package is to provide a generic way to generate code across all BSW modules.
It might be invoked from the command line (see ```bsw_code_gen --help```) or imported as a package from an other script.

# Required structure
According to Autosar standard, the following files might be generated:
- **\<ModuleName\>.c**
- **\<ModuleName\>.h**
- **\<ModuleName\>_Cfg.c**
- **\<ModuleName\>_Cfg.h**
- **\<ModuleName\>_PBcfg.c**
- **\<ModuleName\>_PBcfg.h**

To enforce a consistent file naming across all modules, the package will look for a jinja2 template named 
**source.c.jinja2** to generate the file **\<ModuleName>.c**, **header_cfg.h.jinja2** to generate the file 
**\<ModuleName>_Cfg.h** and so on.
