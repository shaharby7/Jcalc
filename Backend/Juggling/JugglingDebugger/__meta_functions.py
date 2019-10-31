__pattern_validators = []


def declare_new_pattern_validator(validate_func):
    """
    The function should be used as a decorator, to register a function as a validator for function and therefore to run
    any time "debug_pattern" is being called.
    Also, the decorator is doing another two things:
    * Making sure that the value that is return from the validation function is a list.
    * Setting the "king" attributes of all PatternProblems at the list of the output to be the name of the validation
        function.

    :param validate_func: the validation function.
    :return: None
    """
    def real_validation_func(pattern):
        pattern_problems = validate_func(pattern)
        if pattern_problems:
            if not isinstance(pattern_problems, list):
                pattern_problems = [pattern_problems]
            [pattern_problem.add_kind(validate_func.__name__)
             for pattern_problem in pattern_problems]
            return pattern_problems

    __pattern_validators.append(real_validation_func)


def debug_pattern(pattern):
    """
    The functions is responsible for running all the validators declared at the package "validators" (for more details
    see the documentation for the validators package). Any validator should return a list of PattenProblem, and the
    function returns all the lists united.
    :param pattern:
    :return: list of all problems at the pattern
    """
    pattern_problems = []
    for pattern_validator in __pattern_validators:
        pattern_validator_indications = pattern_validator(pattern)
        if pattern_validator_indications:
            pattern_problems.extend(pattern_validator_indications)
    return pattern_problems
