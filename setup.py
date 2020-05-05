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

setup(
    name='gsync',
    description='GSync - RSync for Google Drive',
    version=__version__,
    license='BSD License',
    author='Craig Phillips',
    author_email='iwonbigbro@gmail.com',
    keywords=[
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
    url='https://github.com/iwonbigbro/gsync',
    long_description=delim.join([
        "Gsync %s - %s" % (__version__, str(datetime.utcnow())),
        open("README.md").read(),
        "Change history",
        open("CHANGELOG.md").read()
    ]),
    test_suite="tests",
    setup_requires=[
        'setuptools',
    ],
    install_requires=REQUIREMENTS,
    packages=[
        'libgsync',
        'libgsync.drive',
        'libgsync.options',
        'libgsync.sync',
        'libgsync.sync.file',
    ],
    scripts=[
        'bin/gsync',
    ],
)
