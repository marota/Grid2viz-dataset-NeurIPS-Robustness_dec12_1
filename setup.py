from setuptools import setup

setup(
   name='grid2viz-dataset-neurips-robustness',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.com',
   packages=['grid2viz-dataset-neurips'],  #same as name
   install_requires=['grid2viz-dataset-neurips', 'jupyter-server-proxy', 'jupyter-dash','grid2viz'], #external packages as dependencies
)
