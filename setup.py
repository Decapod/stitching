#!/usr/bin/env python

import glob
from distutils.core import setup, Extension

setup (name = 'decapod_stitching',
       version = '0.0',
       author      = "Thomas Breuel",
       description = """Stitching commands for DECAPOD.""",
       scripts = glob.glob("decapod-*"),
       )
