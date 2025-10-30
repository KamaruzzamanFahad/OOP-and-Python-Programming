

def person(first_name, **additional_names):
    full_name = first_name
    for key, value in additional_names.items():
        full_name += ' ' + value
    return full_name