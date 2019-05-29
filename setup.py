import os

from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements.txt')) as f:
    requirements = f.read().strip().split('\n')


setup(
    name="unplugged",
    version="0.1.0",
    packages=find_packages(),

    install_requires=requirements,
    author="Anders Jensen",
    author_email="johndoee@tidalstream.org",
    description="Django based plugin system",
    license="MIT",
    url="https://github.com/JohnDoee/unplugged",

)