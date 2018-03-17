#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Copyright 2017 Guenter Bartsch
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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

