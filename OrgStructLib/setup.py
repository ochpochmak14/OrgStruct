from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='OrgStructLib',
  version='0.0.1',
  author='ochpochmak14',
  author_email='makhmudovemin441@gmail.com',
  description='A lightweight and efficient Python library for managing company structures, employees, and organizational hierarchies.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/ochpochmak14/OrgStruct',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='company organization hierarchy employee management HR staff team structure workforce business automation corporate personnel department company structure team management Python HR system employee database company API organizational chart',
  project_urls={
    'GitHub': 'https://github.com/ochpochmak14/OrgStruct'
  },
  python_requires='>=3.9'
)