#! /usr/bin/env python
# -*- coding: utf8 -*-
# Copyright (C) 2013 Craig Phillips. All rights reserved.
"""GSync -- RSync for Google Drive."""

import io
import os
from setuptools import setup
from libgsync import __version__

# Get the long description.
HERE = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(HERE, "README.md"), encoding="utf-8") as fobj:
    README = fobj.read()
with io.open(os.path.join(HERE, "CHANGELOG.md"), encoding="utf-8") as fobj:
    CHANGELOG = fobj.read()
DELIMITER = "\n{}\n\n".format(79 * "=")
LONG_DESCRIPTION = DELIMITER.join([README, CHANGELOG])

# Get the license.
with io.open(os.path.join(HERE, "LICENSE"), encoding="utf-8") as fobj:
    LICENSE = fobj.read()

# Get the requirements.
with io.open(os.path.join(HERE, "requirements.txt"), encoding="utf-8") as fobj:
    REQUIREMENTS = fobj.read().splitlines()

setup(**{
    "name":
        "gsync",
    "version":
        __version__,
    "license":
        LICENSE,
    "description":
        "GSync -- RSync for Google Drive",
    "long_description":
        LONG_DESCRIPTION,
    "long_description_content_type":
        "text/markdown",
    "url":
        "https://github.com/iwonbigbro/gsync",
    "author":
        "Craig Phillips",
    "author_email":
        "iwonbigbro@gmail.com",
    "maintainer":
        "Víctor Molina García",
    "maintainer_email":
        "molinav@users.noreply.github.com",
    "keywords": [
        "gsync",
        "rsync",
        "google",
        "drive",
        "transfer",
        "copy",
        "sync",
        "files",
        "ftp",
    ],
    "packages": [
        "libgsync",
        "libgsync.drive",
        "libgsync.options",
        "libgsync.sync",
        "libgsync.sync.file",
    ],
    "scripts": [
        "bin/gsync",
    ],
    "install_requires":
        REQUIREMENTS,
    "setup_requires": [
        "setuptools",
    ],
    "python_requires":
        ", ".join([
            ">=2.7",
            "!=3.0.*",
            "!=3.1.*",
            "!=3.2.*",
            "!=3.3.*",
            "<4",
        ]),
    "test_suite":
        "tests",
})
