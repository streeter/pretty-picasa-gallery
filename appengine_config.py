import os
import sys
from google.appengine.dist import use_library
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
use_library('django', '1.2')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
