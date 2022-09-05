from setuptools import setup, find_packages

setup(
    name='data-apps-utils-documentation',
    version=open("version.txt").read().rstrip(),
    packages=find_packages(),
    entry_points={}
)
