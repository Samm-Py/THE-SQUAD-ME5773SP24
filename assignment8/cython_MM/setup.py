from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np




exts = []
openmp_compile_flag = True
mod1 = Extension('MM',
              sources=['MM.pyx'],
              include_dirs=[np.get_include()],  # include header from numpy.      
              extra_compile_args=["-I.","-I.","-O3", '-qopenmp'],  # enables flag for c99 standard.
              extra_link_args=['-qopenmp',"-O3"],
              libraries=['m','ifcore','ifcoremt','svml','intlc'], # Link to math library.
    )


setup(
    ext_modules=cythonize( mod1, annotate=False),
)




exts = []
openmp_compile_flag = True
mod1 = Extension('MM_dot',
              sources=['MM_dot.pyx'],
              include_dirs=[np.get_include()],  # include header from numpy.      
              extra_compile_args=["-I.","-I.","-O3", '-qopenmp'],  # enables flag for c99 standard.
              extra_link_args=['-qopenmp',"-O3"],
              libraries=['m','ifcore','ifcoremt','svml','intlc'], # Link to math library.
    )


setup(
    ext_modules=cythonize( mod1, annotate=False),
)