from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python-bites',
    version='0.0.1',
    description='Experimental python code written as learning exercise',
    long_description=readme,
    author='Prashant Chauhan',
    author_email='pchauhan@gmail.com',
    url='https://github.com/git-pchauhan/python-bites',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
