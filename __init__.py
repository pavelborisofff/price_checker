import os.path
import sys

from loguru import logger
from dotenv import load_dotenv

from config import Preferences


load_dotenv()
prefs = Preferences()

logger.remove()
logger.add(sys.stderr, level='DEBUG')

for dir_name in prefs.dirs.dict().values():
    os.path.exists(dir_name) or os.makedirs(dir_name)

logger.add(prefs.log_file, level=prefs.log_level)
