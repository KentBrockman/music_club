"""simple code to return or print a hashed password
use for setting up test users"""

import os
import sys

from django.contrib.auth.hashers import make_password

if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'music_club.settings'


def hash_password(password):
    return make_password(password)


if __name__ == '__main__':
    if len(sys.argv) == 0:
        print('supply a password as first argument')
        sys.exit(1)
    print(hash_password(sys.argv[1]))
