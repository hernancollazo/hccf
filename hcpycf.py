#!/usr/bin/python
# -*- coding: utf-8 -*-

###
# hcpycf.py
###
# Python Common functions Package
###
# Use At Your Own Risk!
###
# Copyright (c) 2015 - Hernan Collazo <hernan.collazo@gmail.com>
###
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
###
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
###
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
###

__author__ = "Hernan Collazo <hernan.collazo@gmail.com>"
__version__ = "1.2"
__copyright__ = "Copyright (c) 2010-2015"
__license__ = "GPL"

import os
import re
import sys
import socket
import string
import time
import datetime
import ConfigParser
import shutil
import commands
import smtplib
from random import *

#########################################################################
### Common Functions ####################################################
#########################################################################


def separator():
    "Just display a line"
    print "\n**************************************************************************************\n"


def readConfigValue(configFile, section, variable):
    "Get a var value from config file"
    myCfg = ConfigParser.ConfigParser()
    myCfg.read(configFile)
    cfgVar = myCfg.get(section, variable)
    return cfgVar


def clear():
    "Just clear the console"
    os.system('clear')
    return


def alertMsg(message):
    "Show message in console with special colors"
    " https://www.siafoo.net/snippet/88 "
    print "\033[1;41m" + message + "\033[1;m"
    return


def pause():
    "Just a pause at console"
    raw_input("\nPresione ENTER para continuar...\n")
    return


def isAlphanumeric(string):
    "Check that string just have alphanumeric charaters"
    pattern = r'[^a-z0-9A-Z]'
    if re.search(pattern, string):
        return False
    else:
        return True


def random_password():
    "Return a random password"
    chars = string.ascii_letters + string.digits
    return "".join(choice(chars) for x in range(randint(8, 16)))


def ValidateEmail(email):
    "Validate Email addresses. Return 1 if OK"
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return 1
    return 0


def dateStamp():
    "Return date-stam string"
    dateStamp = time.strftime("%Y%m%d-%H%M%S", time.localtime())
    return dateStamp


def sendEmail(mailFrom, mailTo, mailSubject, mailBody, SMTPServer="localhost", SMTPTimeOut=30):
    "Send basic email"
    msg = "" + "From: " + mailFrom + "\n"
    msg = msg + "To: " + mailTo + "\n"
    msg = msg + "Subject: " + mailSubject + "\n"
    msg = msg + "\n"
    msg = msg + mailBody
    socket.setdefaulttimeout(SMTPTimeOut)
    try:
        server = smtplib.SMTP(SMTPServer)
        server.set_debuglevel(0)
    except socket.timeout:
        print "\n\n**** ERROR **** server timeout!\n\n"
        sys.exit(0)
    except smtplib.socket.gaierror:
        return False
    server.sendmail(mailFrom, mailTo, msg)
    server.quit()


def comp_dates(d1, d2):
    "compare two dates, returning diff in seconds"
    return time.mktime(time.strptime(d2, "%Y-%m-%d %H:%M:%S")) -\
        time.mktime(time.strptime(d1, "%Y-%m-%d %H:%M:%S"))


def make_unicode(input):
    "convert a string to utf-8"
    if type(input) != unicode:
        input = input.decode('utf-8')
        return input
    else:
        return input
