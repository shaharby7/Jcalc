class PatternProblem(object):
    """
    A class that is used to describe a logical problem in a pattern.
    """
    def __init__(self, message, problematic_beat, kind=None):
        self.__dict__.update(locals())
        del self.__dict__["self"]

    def add_kind(self, kind):
        """
        Normally should not be called, and should be used only at the body of the decorator
        "declare_new_pattern_validator"
        """
        if not self.kind:
            self.kind = kind

    def __repr__(self):
        return """Problem of kind {} at beat number {}
        {}""".format(self.kind, self.problematic_beat, self.message)
