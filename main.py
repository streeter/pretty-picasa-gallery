#!/usr/bin/python2.5

"""Main entrance point for all requests."""

__author__ = 'chris@chrisstreeter.com (Chris Streeter)'

import appengine_config
import django.core.handlers.wsgi
from google.appengine.ext.webapp import util

def main():
  application = django.core.handlers.wsgi.WSGIHandler()
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()
