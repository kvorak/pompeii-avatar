def dir_module_as_kvpd(module):
    return 

def make_manifest(module):
    """ Returns a manifestation of the loaded module's API using Python's native inspection

    @param module: Either an imported module, or a string that is resolvable to one

    >>> myAvatar = make_manifest(re)
    """

    if isinstance(module, basestring):
        # load the selected module into the variable
        raise NotImplementedError("TODO: implement lazy loading of modules by string names")

    # and this is where we build the Manifest object
    manifest = manifest(module)
