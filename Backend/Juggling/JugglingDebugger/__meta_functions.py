__pattern_validators = []


def declare_new_pattern_validator(validate_func):
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
    pattern_problems = []
    for pattern_validator in __pattern_validators:
        pattern_validator_indications = pattern_validator(pattern)
        if pattern_validator_indications:
            pattern_problems.extend(pattern_validator_indications)
    return pattern_problems
