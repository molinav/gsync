#!/usr/bin/env python

# Copyright (C) 2013 Craig Phillips.  All rights reserved.

import io
import os
from datetime import datetime
from setuptools import setup
from libgsync import __version__

# Get the requirements.
HERE = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(HERE, "requirements.txt"), encoding="utf-8") as fobj:
    REQUIREMENTS = fobj.read().splitlines()

delim = """
=============================================================================

"""

setup(**{
    "name":
        "gsync",
    "version":
        __version__,
    "license":
        "BSD License",
    "description":
        "GSync - RSync for Google Drive",
    "long_description":
        delim.join([
            "Gsync %s - %s" % (__version__, str(datetime.utcnow())),
            open("README.md").read(),
            "Change history",
            open("CHANGELOG.md").read()
        ]),
    "url":
        "https://github.com/iwonbigbro/gsync",
    "author":
        "Craig Phillips",
    "author_email":
        "iwonbigbro@gmail.com",
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
    "test_suite":
        "tests",
})
