#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Copyright 2017 Guenter Bartsch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#
# demo using the high level XSB interface
#

from xsbprolog import xsb_hl_init, xsb_hl_command, xsb_hl_query, xsb_close

XSB_ROOT = '/opt/xsb-3.8.0/'

xsb_hl_init([XSB_ROOT])

xsb_hl_command('consult', ['ft'])

for row in xsb_hl_query('label', ['X', 'L']):
    print u"label of %s is %s" % (row['X'], row['L'])

for row in xsb_hl_query('descend', ['X', 'Y']):
    print u"decendant of %s is %s" % (row['X'], row['Y'])


# Close connection 
xsb_close()

