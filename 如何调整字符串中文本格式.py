# -*- coding: utf-8 -*-

import re
log = open("scout_log_20160628.txt").read()

result = re.sub("(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", r"\g<month>/\g<day>/\g<year>", log)

print result