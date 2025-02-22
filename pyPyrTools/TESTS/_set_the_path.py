"""
Dumb little utility for adding the top-level pyPyrTools directory
to the python module path at runtime. Should be sufficient for any script to
just call ``import _set_the_path``. There are probably better ways to do this.
"""
import sys
import os
tests_fullpath = os.path.dirname(os.path.abspath(__file__))
toplevel_dir_fullpath = tests_fullpath[:tests_fullpath.find('pyPyrTools/pyPyrTools')+11]
sys.path.insert(0, toplevel_dir_fullpath)
