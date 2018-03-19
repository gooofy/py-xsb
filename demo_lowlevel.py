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
# demo using the low level XSB API
#

from xsbprolog import *

XSB_ROOT = '/opt/xsb-3.8.0/'

argv = (c_char_p * 2)()
argv[0] = XSB_ROOT

xsb_init(1, argv)

c2p_functor("consult", 1, reg_term(1))
c2p_string("ctest",p2p_arg(reg_term(1),1))
if xsb_command():
    raise Exception ("Error consulting ctest")

if xsb_command_string("consult(basics)."):
    raise Exception ("Error (string) consulting basics.")

# Create the query p(300,X,Y) and send it.
c2p_functor("p",3,reg_term(1))
c2p_int(300,p2p_arg(reg_term(1),1))

rcode = xsb_query()

# Print out answer and retrieve next one.
while not rcode:

    if not is_string(p2p_arg(reg_term(2),1)) and is_string(p2p_arg(reg_term(2),2)):
        print "2nd and 3rd subfields must be atoms"
    else:
        print "Answer: %d, %s(%s), %s(%s)" % ( p2c_int(p2p_arg(reg_term(1),1)),
                                               p2c_string(p2p_arg(reg_term(1),2)),
                                               xsb_var_string(1),
                                               p2c_string(p2p_arg(reg_term(1),3)),
                                               xsb_var_string(2))
    rcode = xsb_next()

# Create the string query p(300,X,Y) and send it, use higher-level routines.

xsb_make_vars(3)
xsb_set_var_int(300,1)
rcode = xsb_query_string("p(X,Y,Z).")

# Print out answer and retrieve next one.
while not rcode:
    if not is_string(p2p_arg(reg_term(2),2)) and is_string(p2p_arg(reg_term(2),3)):
        print "2nd and 3rd subfields must be atoms"
    else:
        print "Answer: %d, %s, %s" % (xsb_var_int(1),
                                      xsb_var_string(2),
                                      xsb_var_string(3))
    rcode = xsb_next()

# Close connection */
xsb_close()

