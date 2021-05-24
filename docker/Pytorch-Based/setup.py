from setuptools import setup, find_packages

setup(name='FederatedLearning',   # インストールするディレクトリ名
      version='0.1.0',
      description='Project description',
      author='',
      author_email='',
      url='',
      install_requirs=[
          'torch==1.8.0', 
          'numpy==1.20.3'、
          'torchvision', 
          'matplotlib'
            ],
      packages=find_packages()
      )