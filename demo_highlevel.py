#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Copyright 2017, 2018 Guenter Bartsch
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

from xsbprolog import xsb_hl_init, xsb_hl_command, xsb_hl_query, xsb_close, XSBFunctor, XSBVariable, xsb_to_json, json_to_xsb

XSB_ROOT = '/opt/xsb-3.8.0/'

xsb_hl_init([XSB_ROOT])

# simple string-based interface

xsb_hl_command('consult(ft).')

for row in xsb_hl_query('label(X, L).'):
    print u"label of %s is %s" % (row[0], row[1])

# structured XSB* interface

for row in xsb_hl_query(XSBFunctor('descend', [XSBVariable('X'), XSBVariable('Y')])):
    print u"decendant of %s is %s" % (row[0], row[1])

for row in xsb_hl_query(u'A = 1, B = 0.5, C = "hello", D = yes, E = foo(bar), F = [1.1,2.2], G = \'günter\'.'):

    for i, r in enumerate(row):
        print u"#%d: %-10s (type: %-20s, class: %-20s)" % (i, r, type(r), r.__class__)

    js = xsb_to_json(row)
    print "json: %s" % js

    row2 = json_to_xsb(js)
    print "restored: %s" % str(row2)

# Close connection 
xsb_close()

