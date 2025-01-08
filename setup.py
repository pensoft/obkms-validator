import os
from setuptools import setup

# Requirements
with open("requirements/prod.txt") as f:
    requires = f.read().strip().split("\n")

# Readme
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='obkms-validator',
    keywords='openbiodiv pensoft biodiversity knowledge system',
    version='1.0.0',
    description='Validator for obkms identifiers in xmls',
    license='MIT',
    long_description=read('README.md'),
    author='Georgi Zhelezov',
    author_email='g.zhelezov@pensoft.net',
    install_requires=requires,
    url="https://github.com/pensoft/obkms-validator",
    py_modules=['config', 'validator']
)