from setuptools import setup, find_packages
from os import path

setup(
  name='Brewgorithm',
  version='2.1.3',
  description='Machine Learning Library For Beer',
  url='https://github.com/ericzhao28/brewgorithm_devkit.git',
  author='Eric Zhao, Brewgorithm, and Contributors',
  author_email='elzhao@caltech.edu',
  license='MIT',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
  ],
  keywords='beer data ai machine_learning',
  packages=find_packages(exclude=['docs', 'tests']),
  package_data={'': ['*.txt', '*.model']},
  include_package_data=True,
  install_requires=['keras', 'gensim', 'spacy', 'h5py', 'tensorflow']
)

