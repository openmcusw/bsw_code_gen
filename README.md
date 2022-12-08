# Package description
The purpose of this package is to provide a generic way to generate code across all BSW modules. It might be invoked
from the command line (see ```bsw_code_gen --help```) or imported as a package from another script.

# Required structure
According to Autosar standard, the following files might be generated:
- **\<ModuleName\>.c**
- **\<ModuleName\>.h**
- **\<ModuleName\>_Cfg.c**
- **\<ModuleName\>_Cfg.h**
- **\<ModuleName\>_PBcfg.c**
- **\<ModuleName\>_PBcfg.h**

Moreover, some modules (such as *XCP* for instance) might require a generated structure held in RAM memory (in the case
of *XCP*, the DAQs). Those files will be named:
- **\<ModuleName\>_Rt.c**
- **\<ModuleName\>_Rt.h**

To enforce a consistent file naming across all modules, the package will look for a jinja2 template named 
**source.c.jinja2** to generate the file **\<ModuleName>.c**, **header.h.jinja2** to generate the file 
**\<ModuleName>.h**, **source_cfg.c.jinja2** to generate the file **\<ModuleName>_Cfg.c** and so on.
