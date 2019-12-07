#
# Copyright (c) 2015-2019 CNRS INRIA
#

import numpy as np
from .robot_wrapper import RobotWrapper
from .libpinocchio_pywrap import __version__

from . import libpinocchio_pywrap as pin
from . import utils
from . import visualize
from .explog import exp, log
from .libpinocchio_pywrap import *
from .deprecated import *
from .shortcuts import *

if pin.WITH_FCL:
  try:
    import hppfcl as fcl
    WITH_FCL_BINDINGS = True
  except ImportError:
    WITH_FCL_BINDINGS = False
else:
  WITH_FCL_BINDINGS = False
  
