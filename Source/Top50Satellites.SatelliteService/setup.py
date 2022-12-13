from setuptools import setup

setup(
   name='satservice',
   version='0.1.0',
   author='Pawleshhh',
   author_email='mateuszpawlikowski98@gmail.com',
   packages=['satservice'],
   description='Satellite service',
   install_requires=['python-dateutil', 'skyfield', 'numpy']
)