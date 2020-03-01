# Local file storage
import sys
import os
from pathlib import Path 
current_path = Path().resolve()
abs_path = str(current_path.parent)
sys.path.append(abs_path)

DATA_PATH = current_path.parent / 'data'
THEMES_PATH = current_path.parent / 'themes'
