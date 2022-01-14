from setuptools import setup

setup(
   name='Grid2viz-dataset-NeurIPS-Robustness_dec12_1',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.com',
   packages=['Grid2viz-dataset-NeurIPS-Robustness_dec12_1'],  #same as name
   install_requires=['grid2viz-dataset-neurips', 'jupyter-server-proxy', 'jupyter-dash','grid2viz'], #external packages as dependencies
)
