"""
All modules at this package would be imported, and therefore any declaration of validator (using the decorator
"declare_new_pattern_validator" from the package JugglingDebugger) would be executed, and therefore all the validators
would run when "debug_pattern" would be invoked.
"""

import os
import pkgutil

directory = os.path.dirname(os.path.realpath(__file__))
for importer, package_name, _ in pkgutil.iter_modules([directory]):
    exec("from .{} import *".format(package_name))
