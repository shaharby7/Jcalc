class PatternProblem(object):
    def __init__(self, message, problematic_beat, kind=None):
        self.__dict__.update(locals())
        del self.__dict__["self"]

    def add_kind(self, kind):
        if not self.kind:
            self.kind = kind
