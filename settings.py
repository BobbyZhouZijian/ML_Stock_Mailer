# settings.py
from dotenv import load_dotenv
import os
# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only

load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def get(name):
    return os.getenv(name)
