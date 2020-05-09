#!/usr/bin/env python
# -*- coding: utf8 -*-

# Copyright (C) 2013-2014 Craig Phillips.  All rights reserved.

"""Defines the client object to be used during authentication"""

import os
import json

with open(os.path.join(os.path.dirname(__file__), "client.json"), "r") as fd:
    client_obj = json.load(fd)  # pylint: disable=invalid-name
