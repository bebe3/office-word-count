from os.path import dirname, join

from setuptools import setup

from office_word_count import __versionstr__

f = open(join(dirname(__file__), "README.md"))
LONG_description = f.read().strip()
f.close()


NAME = "office-word-count"
VERSION = __versionstr__
AUTHOR = "bebe3"
AUTHOR_EMAIL = "i.masashi0323@gmail.com"
URL = "https://github.com/bebe3/office-word-count"
LICENSE = "MIT"
DESCRIPTION = "Word count tool like MS Office Word"
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"
PACKAGES = [
    "office_word_count",
]
INSTALL_REQUIRES = [
    "regex",
]
CLASSIFIERS = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]

setup(
    name=NAME,
    license=LICENSE,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_description,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
)
