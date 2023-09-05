def make_no_round_brackets(input):
    result = input.replace('(', '').replace(')', '')
    return result

def make_no_square_brackets(input):
    result = input.replace('[', '').replace(']', '')
    return result

def make_no_curly_brackets(input):
    result = input.replace('{', '').replace('}', '')
    return result

def make_no_brackets(input):
    result = make_no_round_brackets(make_no_square_brackets(make_no_curly_brackets(input)))
    return result