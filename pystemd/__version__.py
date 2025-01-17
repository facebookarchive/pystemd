#!/usr/bin/env python3
#
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the LICENSE file in
# the root directory of this source tree.
#

import sys

# during development this version is always at least "one up" the
# latest release.
__version__ = "0.12.0"

sys.modules[__name__] = __version__
