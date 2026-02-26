"""
reader - Simple utilities for common tasks
"""

try:
    from . import rfiles
except Exception as e:
    print(f"Error loading rfiles: {e}")

try:
    from . import rhtml
except Exception as e:
    print(f"Error loading rhtml: {e}")

try:
    from . import raudio
except Exception as e:
    print(f"Error loading raudio: {e}")

try:
    from . import rmouse
except Exception as e:
    print(f"Error loading rmouse: {e}")

__version__ = "1.0.0"

'''from . import rfiles
from . import rhtml
from . import raudio
from . import rmouse

# You can also expose specific functions directly
from .rfiles import create, read, write, delete, run, stop
from .rhtml import get, browse, browseget, openjs, openhtml
from .raudio import play, stop, beep
from .rmouse import mouse, position, scroll

__version__ = "1.0.0"
__all__ = ['rfiles', 'rhtml', 'raudio', 'rmouse']'''
