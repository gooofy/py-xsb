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

