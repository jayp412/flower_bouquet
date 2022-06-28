from setuptools import setup, find_packages


setup(
    name='flowerbouquet',
    version='0.1',
    author='Jay',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    # scripts=['bin/script1','bin/script2'],
    license='LICENSE.txt',
    description='Order management package in python',
    long_description=open('README.MD').read(),
)