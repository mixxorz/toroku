"""Development settings
"""

from toroku.settings.base import *

# This key should only be used on development
SECRET_KEY = '62l1$&--)pj2u@w9n3wuq3!u@3_)mxw$9p)272)o^$3j!n2l@f'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Import machine specific dev settings
try:
    from toroku.settings.local import *
except ImportError:
    pass
