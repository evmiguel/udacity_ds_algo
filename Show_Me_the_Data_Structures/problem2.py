import os

def find_files_recursive(suffix, path, list):
    if os.path.isfile(path):
        if (suffix in path):
            list.append(path)
        return list
    else:
        for file in os.listdir(path):
            find_files_recursive(suffix,path+os.sep+file, list)
    return list

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    assert path
    if not suffix:
        return []
    return find_files_recursive(suffix, path, [])

print(find_files('.c', 'testdir'))
# ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']

print(find_files('.s', 'testdir'))
# []

print(find_files('', 'testdir'))
# []

print(find_files(None, 'testdir'))
# []

try:
    print(find_files('.c', ''))
except AssertionError:
    pass


