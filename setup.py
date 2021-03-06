import setuptools
from numpy.distutils.core import setup, Extension

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

ext1 = Extension(name = 'knpy.bins.byindexfast',
                 sources = ['knpy/bins/byindexfast.f90'])

setup(name = 'knpy',
      version = '1.0.0',
      description       = "Personal python utility functions.",
      long_description  = long_description,
      long_description_content_type = 'text/markdown',
      url               = 'https://github.com/knaidoo29/knpy',
      author            = "Krishna Naidoo",
      author_email      = "krishna.naidoo.11@ucl.ac.uk",
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=['numpy', 'matplotlib', 'healpy'],
      ext_modules = [ext1],
      python_requires = '>=3',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Mathematics',
      ],)
