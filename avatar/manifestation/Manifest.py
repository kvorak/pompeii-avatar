from types import ModuleType, FunctionType, BuiltinFunctionType
from functools import partial
import inspect


class FunctionManifest(object):


    def __init__(self, name_func_tuple):
        self._args = None 
        self._varargs = None 
        self._keywords = None 
        self._defaults = None

        self._name, self._func = name_func_tuple

        try:
            self._args, self._varargs, self._keywords, self._defaults = inspect.getargspec(self._func)
        except TypeError as e:
            self._errors = [e]

        self._docstring = self._func.__doc__


    def __str__(self):
        return self._docstring


class ModuleManifest(object):
    """description of class"""
    

    def __init__(self, _module):
        if not isinstance(_module, ModuleType):
            raise TypeError("module must be a valid python module")

        self._module = _module 
        self._kvp = inspect.getmembers(self._module)

    
    def _filter_by(self, func=lambda x: True):
        return inspect.getmembers(self._module, func)


    def callables(self):
        return map(FunctionManifest, self._filter_by(inspect.isfunction))


    def doc(self):
        return self.__doc__
"""
from manifestation.Manifest import ModuleManifest, FunctionManifest
import manifestation.views
import inspect

mine = ModuleManifest(manifestation.views)
funcs = map(FunctionManifest, mine._filter_by(inspect.isfunction))

"""