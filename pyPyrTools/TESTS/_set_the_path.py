"""
Dumb little utility for adding the top-level pyPyrTools directory
to the python module path at runtime. Should be sufficient for any script to
just call ``import _set_the_path``. There are probably better ways to do this.
"""
import sys
import os
tests_fullpath = os.path.dirname(os.path.abspath(__file__))
pyPyrTools_module_fullpath = tests_fullpath[:test_fullpath.rfind('/')]
repo_fullpath = pyPyrTools_module_fullpath[:pyPyrTools_module_fullpath.rfind('/')]
sys.path.insert(0, pyPyrTools_module_fullpath)
sys.path.insert(0, repo_fullpath)
