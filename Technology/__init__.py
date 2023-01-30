import warnings

Message = "Some feature dependencies are not installed, so they will not be imported"

from .math import *
from .password import *
from .tools import *

try:
    from .spider import *
except BaseException as e:
    warnings.warn(UserWarning(f"{Message}, {e}"))