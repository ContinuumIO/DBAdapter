import os
import sys
import glob
from distutils.core import setup, Command
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
import dbadapter.pyodbc_setup
import versioneer


class CleanInplace(Command):
    user_options = []

    def initialize_options(self):
        self.cwd = None

    def finalize_options(self):
        self.cwd = os.getcwd()

    def run(self):
        files = glob.glob('./dbadapter/pyodbc.*.so')
        for file in files:
            try:
                os.remove(file)
            except OSError:
                pass


def setup_odbc(include_dirs, lib_dirs):
    src_path = os.path.join(os.path.dirname(__file__), 'dbadapter/pyodbc/src')
    src = [os.path.abspath(os.path.join(src_path, f))
           for f in os.listdir(src_path)
           if f.endswith('.cpp') ]

    if sys.platform == 'win32':
        libraries = ['odbc32', 'advapi32']
    elif sys.platform == 'darwin':
        if os.environ.get('UNIXODBC_PATH', ''):
            include_dirs.append(os.path.join(os.environ.get('UNIXODBC_PATH')))
            include_dirs.append(os.path.join(os.environ.get('UNIXODBC_PATH'), 'include'))
            lib_dirs.append(os.path.join(os.environ.get('UNIXODBC_PATH'), 'DriverManager', '.libs'))
            libraries = ['odbc']
        else:
            libraries = ['odbc']
    else:
        libraries = ['odbc']

    return Extension('dbadapter.pyodbc',
                     src,
                     include_dirs=include_dirs,
                     libraries=libraries,
                     library_dirs=lib_dirs)


def run_setup():

    include_dirs = [os.path.join('dbadapter', 'lib'),
                    numpy.get_include()]
    if sys.platform == 'win32':
        include_dirs.append(os.path.join(sys.prefix, 'Library', 'include'))
    else:
        include_dirs.append(os.path.join(sys.prefix, 'include'))

    lib_dirs = []
    if sys.platform == 'win32':
        lib_dirs.append(os.path.join(sys.prefix, 'Library', 'lib'))
    else:
        lib_dirs.append(os.path.join(sys.prefix, 'lib'))

    ext_modules = []
    packages = ['dbadapter', 'dbadapter.lib', 'dbadapter.tests']
    ext_modules.append(setup_odbc(include_dirs, lib_dirs))

    versioneer.versionfile_source = 'dbadapter/_version.py'
    versioneer.versionfile_build = 'dbadapter/_version.py'
    versioneer.tag_prefix = ''
    versioneer.parentdir_prefix = 'dbadapter-'

    cmdclass = versioneer.get_cmdclass()
    cmdclass['build_ext'] = build_ext
    cmdclass['cleanall'] = CleanInplace

    setup(name='dbadapter',
          version = versioneer.get_version(),
          description='optimized IO for NumPy/Blaze',
          author='Continuum Analytics',
          author_email='noreply@continuum.io',
          ext_modules=ext_modules,
          packages=packages,
          cmdclass=cmdclass)


if __name__ == '__main__':
    run_setup()
