#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from datetime import datetime, timedelta

# Retrieve files older than 6 hours

outdated = []
for root, dirs, files in os.walk("."):
   for name in files:
      six_hours_ago = datetime.now() - timedelta(hours=6)
      filetime = datetime.fromtimestamp(os.path.getctime(os.path.join(root, name)))
      if filetime < six_hours_ago:
         outdated.append(os.path.join(root, name))
