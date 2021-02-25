import os
from pathlib import Path
from environ import environ  # noqa

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

env = environ.Env()

# The environment should be passed on by docker and there is no need to read env manually,
# but these lines are there to make environments work if someone wants to run the app without docker:
if os.path.exists(BASE_DIR / '.env.local'):
    env.read_env(str(BASE_DIR / '.env.local'))
elif os.path.exists(BASE_DIR / '.env.production'):
    env.read_env(str(BASE_DIR / '.env.production'))
