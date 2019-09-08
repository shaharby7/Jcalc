class PatternProblem(object):
    def __init__(self, message, problematic_beat, kind=None):
        self.__dict__.update(locals())
        del self.__dict__["self"]

    def add_kind(self, kind):
        if not self.kind:
            self.kind = kind

    def __repr__(self):
        return """Problem of kind {} at beat number {}
        {}""".format(self.kind, self.problematic_beat, self.message)
