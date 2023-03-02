

def judge_number(file_path, number_range):
    """judge if file_path contains any number from [number_range[0], number_range[1]).

    Args:
        file_path (str): the file path
        number_range (tuple): [number, number)

    Returns:
        _type_: _description_
    """
    name_list = [str(i) for i in range(number_range[0], number_range[1], 1)]
    for i in name_list:
        if i in file_path:
            return True
    return False