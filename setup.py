from distutils.core import setup
                      
setup (name = 'pysacio',
       version = '0.1',
       description = 'Read and write SAC files from Python',
       py_modules  = [ 'pysacio' ],
       scripts = [ 'sac2ascii' ])
       