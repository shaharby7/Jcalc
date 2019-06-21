import os
import pkgutil

directory = os.path.dirname(os.path.realpath(__file__))
for importer, package_name, _ in pkgutil.iter_modules([directory]):
    exec("from .{} import *".format(package_name))
