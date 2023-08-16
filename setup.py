from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

# with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'package to load needed csv files'
LONG_DESCRIPTION = 'A package that allows to fetch all the required csv files for lab manual exercises.'

# Setting up
setup(
    name="DSPackage",
    version=VERSION,
    author="Aravind S, Ashik Jenly VL",
    author_email="aravind9180@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    package_data={'DSPackage': ['Data/*.csv']},
    install_requires=['pandas'],
    keywords=['python', 'DS', 'datasets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)