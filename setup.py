import os
import sys
import uwsgiconfig as uc
import shutil

from distutils.core import setup, Distribution
from distutils.command.install import install


print sys.argv

class uWSGIInstall(install):

	def run(self):
		uc.build_uwsgi(sys.prefix + '/bin/' + uc.UWSGI_BIN_NAME, uc.uver, uc.cflags, uc.ldflags)

class uWSGIDistribution(Distribution):

	def __init__(self, *attrs):
		Distribution.__init__(self, *attrs)
		self.cmdclass['install'] = uWSGIInstall
		


setup(name='uWSGI',
      version='0.9.5',
      description='The uWSGI server',
      author='Unbit',
      author_email='info@unbit.it',
      url='http://projects.unbit.it/uwsgi/',
      license='GPL2',
      distclass = uWSGIDistribution,
     )



