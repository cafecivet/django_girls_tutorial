#!C:\Users\mbradford\Documents\django_projects\mysite\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'gunicorn==19.1.1','console_scripts','gunicorn_django'
__requires__ = 'gunicorn==19.1.1'
import sys
from pkg_resources import load_entry_point

sys.exit(
   load_entry_point('gunicorn==19.1.1', 'console_scripts', 'gunicorn_django')()
)
