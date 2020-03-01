%reload_ext autoreload
%autoreload 2

import os
import sys
sys.path.insert(0, '../')
sys.path.insert(0, '../scripts')
from config import *

from utils import *

from copy import deepcopy
import numpy as np
import pandas as pd
pd.options.display.max_columns = 999

import warnings
warnings.filterwarnings('ignore')