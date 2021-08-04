from setuptools import setup, find_packages
setup(
  name='fvvdp',
  version='latest',
  description='A visible difference predictor for wide field-of-view video',
  author='Rafal Mantiuk',
  author_email='rkm38@cam.ac.uk',
  packages = ['fvvdp', 'fvvdp.third_party'],
  package_dir = {'fvvdp': 'pytorch'},
  install_requires = [
    'torch', 'pytorch_msssim', 'scikit_video',  'numpy', 'scipy', 'graphviz',
    'natsort',
  ]
)
