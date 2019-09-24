class JugglingException(Exception):
    def __init__(self, message, problematic_beat=None):
        super().__init__(message)
        self.problematic_beat = problematic_beat
