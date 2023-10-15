import os
"""
__init__.py marks a directory as a Python package. It is executed
when the package is imported.
It is also needed for the Python test runner to discover tests for VS Code.
"""


def package_dir(file):
    """
    Return name of this package, which is the name of its directory.
    """
    path = os.path.normpath(file).split(os.sep)
    return path[len(path)-2]    # e.g. "C_numbers"


def project_dir(file):
    """
    Return path to project directory.
    """
    path = os.path.normpath(file).split(os.sep)
    return os.path.dirname(file)[:-len(PACKAGE_DIR)-1]


def import_sol_module(file):
    """
    Import and return module with name "file + '_sol'".
    Raises ImportError exception, if _sol file does not exist.
    """
    sol_module = (file.split("\\")[-1:])[0].split(".")[0] + "_sol"
    return __import__(sol_module, globals(), locals(), [], 0)


PACKAGE_DIR = package_dir(__file__)
PROJECT_DIR = project_dir(__file__)
