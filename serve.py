#!/usr/bin/env python2

try:
    from src.config.config import *
except:
    print "You forgot to create a config! Try working from the example:"
    print "Do: mv src/config/config_example.py src/config/config.py"
    print "then edit src/config/config.py"
    exit(1)

from sys import argv
from src.bot import *
import datetime

#Logger is run. Roboraj is contained within
bot = Logger(config, "log/" + str(datetime.date.today()) + "-lorenzo.html").run()
