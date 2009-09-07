import numpy
from distutils.core import setup, Extension
                      
setup (name = 'psacio',
       include_dirs = [ numpy.get_include() ],
       version = '0.1',
       description = 'Read and write SAC files from Python',
       py_modules  = [ 'pysacio' ],
       scripts = [ 'sac2ascii' ])
       