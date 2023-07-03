from pathlib import Path
import os


def get_last_subdirs(path): 
    """get the last level of subfolders.

    Args:
        path (_type_): _description_

    Returns:
        _type_: _description_
    """
    if not isinstance(path, Path):
        path = Path(path)
    subdirs = [x for x in path.rglob('*') if x.is_dir()]
    last_subdirs = []
    for subdir in subdirs:
        if len([x for x in subdir.rglob('*') if x.is_dir()]) == 0:
            last_subdirs.append(subdir)
    return last_subdirs