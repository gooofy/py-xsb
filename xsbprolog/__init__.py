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
# low level XSB interface, converted to ctypes from XSB 3.8's emu/cinterf.h
#

import sys
import json

from six    import python_2_unicode_compatible, text_type, string_types
from ctypes import cdll, c_longlong, c_int64, c_int32, c_int, c_double, c_char_p, POINTER, c_size_t, create_string_buffer, byref

libxsb = cdll.LoadLibrary('libxsb.so')

is_64bits = sys.maxsize > 2**32

if is_64bits:
    c_prolog_term = c_longlong
    c_prolog_int  = c_int64
    c_cell        = c_longlong
else:
    c_prolog_term = c_long
    c_prolog_int  = c_int32
    c_cell        = c_long

c_void = c_int
c_int_p = POINTER(c_int)

XSB_SUCCESS        = 0
XSB_FAILURE        = 1
XSB_ERROR          = 2
XSB_OVERFLOW       = 3
XSB_SPECIAL_RETURN = 4

#
# Low level C interface
#

# DllExport extern prolog_term call_conv reg_term(CTXTdeclc reg_num);
reg_term = libxsb.reg_term
reg_term.restype = c_prolog_term
reg_term.argtypes = [c_int]

# DllExport extern xsbBool call_conv c2p_int(CTXTdeclc prolog_int, prolog_term);
c2p_int = libxsb.c2p_int
c2p_int.restype = c_int
c2p_int.argtypes = [c_prolog_int,c_prolog_term]

# DllExport extern xsbBool call_conv c2p_float(CTXTdeclc double, prolog_term);
c2p_float = libxsb.c2p_float
c2p_float.restype = c_int
c2p_float.argtypes = [c_double,c_prolog_term]

# DllExport extern xsbBool call_conv c2p_string(CTXTdeclc char*, prolog_term);
c2p_string = libxsb.c2p_string
c2p_string.restype = c_int
c2p_string.argtypes = [c_char_p,c_prolog_term]

# DllExport extern xsbBool call_conv c2p_list(CTXTdeclc prolog_term);
c2p_list = libxsb.c2p_list
c2p_list.restype = c_int
c2p_list.argtypes = [c_prolog_term]

# DllExport extern xsbBool call_conv c2p_nil(CTXTdeclc prolog_term);
c2p_nil = libxsb.c2p_nil
c2p_nil.restype = c_int
c2p_nil.argtypes = [c_prolog_term]

# DllExport extern void call_conv ensure_heap_space(CTXTdeclc int, int);
ensure_heap_space = libxsb.ensure_heap_space
ensure_heap_space.restype = c_void
ensure_heap_space.argtypes = [c_int,c_int]

# DllExport extern xsbBool call_conv c2p_functor(CTXTdeclc char*, int, prolog_term);
c2p_functor = libxsb.c2p_functor
c2p_functor.restype = c_int
c2p_functor.argtypes = [c_char_p,c_int,c_prolog_term]

# DllExport extern xsbBool call_conv c2p_functor_in_mod(CTXTdeclc char*, char*, int, prolog_term);
c2p_functor_in_mod = libxsb.c2p_functor_in_mod
c2p_functor_in_mod.restype = c_int
c2p_functor_in_mod.argtypes = [c_char_p,c_char_p,c_int,c_prolog_term]

# DllExport extern void call_conv c2p_setfree(prolog_term);
c2p_setfree = libxsb.c2p_setfree
c2p_setfree.restype = c_void
c2p_setfree.argtypes = [c_prolog_term]

# DllExport extern void call_conv c2p_chars(CTXTdeclc char*, int, prolog_term);
c2p_chars = libxsb.c2p_chars
c2p_chars.restype = c_void
c2p_chars.argtypes = [c_char_p,c_int,c_prolog_term]

# DllExport extern prolog_int   call_conv p2c_int(prolog_term);
p2c_int = libxsb.p2c_int
p2c_int.restype = c_prolog_int
p2c_int.argtypes = [c_prolog_term]

# DllExport extern double   call_conv p2c_float(prolog_term);
p2c_float = libxsb.p2c_float
p2c_float.restype = c_double
p2c_float.argtypes = [c_prolog_term]

# DllExport extern char*    call_conv p2c_string(prolog_term);
p2c_string = libxsb.p2c_string
p2c_string.restype = c_char_p
p2c_string.argtypes = [c_prolog_term]

# DllExport extern char*    call_conv p2c_functor(prolog_term);
p2c_functor = libxsb.p2c_functor
p2c_functor.restype = c_char_p
p2c_functor.argtypes = [c_prolog_term]

# DllExport extern int      call_conv p2c_arity(prolog_term);
p2c_arity = libxsb.p2c_arity
p2c_arity.restype = c_int
p2c_arity.argtypes = [c_prolog_term]

# DllExport extern char*    call_conv p2c_chars(CTXTdeclc prolog_term,char*,int);
p2c_chars = libxsb.p2c_chars
p2c_chars.restype = c_char_p
p2c_chars.argtypes = [c_prolog_term,c_char_p,c_int]

# DllExport extern prolog_term call_conv p2p_arg(prolog_term, int);
p2p_arg = libxsb.p2p_arg
p2p_arg.restype = c_prolog_term
p2p_arg.argtypes = [c_prolog_term,c_int]

# DllExport extern prolog_term call_conv p2p_car(prolog_term);
p2p_car = libxsb.p2p_car
p2p_car.restype = c_prolog_term
p2p_car.argtypes = [c_prolog_term]

# DllExport extern prolog_term call_conv p2p_cdr(prolog_term);
p2p_cdr = libxsb.p2p_cdr
p2p_cdr.restype = c_prolog_term
p2p_cdr.argtypes = [c_prolog_term]

# DllExport extern prolog_term call_conv p2p_new(CTXTdecl);
p2p_new = libxsb.p2p_new
p2p_new.restype = c_prolog_term
p2p_new.argtypes = []

# DllExport extern xsbBool        call_conv p2p_unify(CTXTdeclc prolog_term, prolog_term);
p2p_unify = libxsb.p2p_unify
p2p_unify.restype = c_int
p2p_unify.argtypes = [c_prolog_term,c_prolog_term]

# # DllExport extern xsbBool        call_conv p2p_call(prolog_term);
# p2p_call = libxsb.p2p_call
# p2p_call.restype = c_int
# p2p_call.argtypes = [c_prolog_term]

# # DllExport extern void	     call_conv p2p_funtrail();
# p2p_funtrail = libxsb.p2p_funtrail
# p2p_funtrail.restype = c_void
# p2p_funtrail.argtypes = []

# DllExport extern prolog_term call_conv p2p_deref(prolog_term);
p2p_deref = libxsb.p2p_deref
p2p_deref.restype = c_prolog_term
p2p_deref.argtypes = [c_prolog_term]

# DllExport extern xsbBool call_conv is_var(prolog_term);
is_var = libxsb.is_var
is_var.restype = c_int
is_var.argtypes = [c_prolog_term]

# DllExport extern xsbBool call_conv is_int(prolog_term);
is_int = libxsb.is_int
is_int.restype = c_int
is_int.argtypes = [c_prolog_term]

# DllExport extern xsbBool call_conv is_float(prolog_term);
is_float = libxsb.is_float
is_float.restype = c_int
is_float.argtypes = [c_prolog_term]

# DllExport extern xsbBool call_conv is_string(prolog_term);
is_string = libxsb.is_string
is_string.restype = c_int
is_string.argtypes = [c_prolog_term]

# DllExport extern xsbBool call_conv is_atom(prolog_term);
is_atom = libxsb.is_atom
is_atom.restype = c_int
is_atom.argtypes = [c_prolog_term]

# DllExport extern xsbBool call_conv is_list(prolog_term);
is_list = libxsb.is_list
is_list.restype = c_int
is_list.argtypes = [c_prolog_term]

# DllExport extern xsbBool call_conv is_nil(prolog_term);
is_nil = libxsb.is_nil
is_nil.restype = c_int
is_nil.argtypes = [c_prolog_term]

# DllExport extern xsbBool call_conv is_functor(prolog_term);
is_functor = libxsb.is_functor
is_functor.restype = c_int
is_functor.argtypes = [c_prolog_term]

# DllExport extern xsbBool call_conv is_charlist(prolog_term,int*);
is_charlist = libxsb.is_charlist
is_charlist.restype = c_int
is_charlist.argtypes = [c_prolog_term,c_int_p]

# DllExport extern xsbBool call_conv is_attv(prolog_term);
is_attv = libxsb.is_attv
is_attv.restype = c_int
is_attv.argtypes = [c_prolog_term]

# extern int   c2p_term(CTXTdeclc char*, char*, prolog_term);
c2p_term = libxsb.c2p_term
c2p_term.restype = c_int
c2p_term.argtypes = [c_char_p,c_char_p,c_prolog_term]

# extern int   p2c_term(CTXTdeclc char*, char*, prolog_term);
p2c_term = libxsb.p2c_term
p2c_term.restype = c_int
p2c_term.argtypes = [c_char_p,c_char_p,c_prolog_term]

#
# Routines to call xsb from C
#

# DllExport extern int call_conv xsb_init(int, char**);
xsb_init = libxsb.xsb_init
xsb_init.restype = c_int
xsb_init.argtypes = [c_int,POINTER(c_char_p)]

# DllExport extern int call_conv xsb_init_string(char*);
xsb_init_string = libxsb.xsb_init_string
xsb_init_string.restype = c_int
xsb_init_string.argtypes = [c_char_p]

# DllExport extern int call_conv pipe_xsb_stdin();
pipe_xsb_stdin = libxsb.pipe_xsb_stdin
pipe_xsb_stdin.restype = c_int
pipe_xsb_stdin.argtypes = []

# DllExport extern int call_conv writeln_to_xsb_stdin(char*);
writeln_to_xsb_stdin = libxsb.writeln_to_xsb_stdin
writeln_to_xsb_stdin.restype = c_int
writeln_to_xsb_stdin.argtypes = [c_char_p]

# DllExport int call_conv xsb_query_save(CTXTdeclc int);
xsb_query_save = libxsb.xsb_query_save
xsb_query_save.restype = c_int
xsb_query_save.argtypes = [c_int]

# DllExport int call_conv xsb_query_restore(CTXTdecl);
xsb_query_restore = libxsb.xsb_query_restore
xsb_query_restore.restype = c_int
xsb_query_restore.argtypes = []

# DllExport extern int call_conv xsb_command(CTXTdecl);
xsb_command = libxsb.xsb_command
xsb_command.restype = c_int
xsb_command.argtypes = []

# DllExport extern int call_conv xsb_command_string(CTXTdeclc char*);
xsb_command_string = libxsb.xsb_command_string
xsb_command_string.restype = c_int
xsb_command_string.argtypes = [c_char_p]

# DllExport extern int call_conv xsb_query(CTXTdecl);
xsb_query = libxsb.xsb_query
xsb_query.restype = c_int
xsb_query.argtypes = []

# DllExport extern int call_conv xsb_query_string(CTXTdeclc char*);
xsb_query_string = libxsb.xsb_query_string
xsb_query_string.restype = c_int
xsb_query_string.argtypes = [c_char_p]

# # DllExport extern int call_conv xsb_query_string_string(CTXTdeclc char*,VarString*,char*);
# xsb_query_string_string = libxsb.xsb_query_string_string
# xsb_query_string_string.restype = c_int
# xsb_query_string_string.argtypes = [c_char_p,c_varstring_p,c_char_p]

# DllExport extern int call_conv xsb_query_string_string_b(CTXTdeclc char*,char*,int,int*,char*);
xsb_query_string_string_b = libxsb.xsb_query_string_string_b
xsb_query_string_string_b.restype = c_int
xsb_query_string_string_b.argtypes = [c_char_p,c_char_p,c_int,c_int_p,c_char_p]

# DllExport extern int call_conv xsb_next(CTXTdecl);
xsb_next = libxsb.xsb_next
xsb_next.restype = c_int
xsb_next.argtypes = []

# # DllExport extern int call_conv xsb_next_string(CTXTdeclc VarString*,char*);
# xsb_next_string = libxsb.xsb_next_string
# xsb_next_string.restype = c_int
# xsb_next_string.argtypes = [c_varstring_p,c_char_p]

# DllExport extern int call_conv xsb_next_string_b(CTXTdeclc char*,int,int*,char*);
xsb_next_string_b = libxsb.xsb_next_string_b
xsb_next_string_b.restype = c_int
xsb_next_string_b.argtypes = [c_char_p,c_int,c_int_p,c_char_p]

# DllExport extern int call_conv xsb_get_last_answer_string(CTXTdeclc char*,int,int*);
xsb_get_last_answer_string = libxsb.xsb_get_last_answer_string
xsb_get_last_answer_string.restype = c_int
xsb_get_last_answer_string.argtypes = [c_char_p,c_int,c_int_p]

# DllExport extern int call_conv xsb_close_query(CTXTdecl);
xsb_close_query = libxsb.xsb_close_query
xsb_close_query.restype = c_int
xsb_close_query.argtypes = []

# DllExport extern int call_conv xsb_close(CTXTdecl);
xsb_close = libxsb.xsb_close
xsb_close.restype = c_int
xsb_close.argtypes = []

# DllExport extern char* call_conv xsb_get_init_error_message();
xsb_get_init_error_message = libxsb.xsb_get_init_error_message
xsb_get_init_error_message.restype = c_char_p
xsb_get_init_error_message.argtypes = []

# DllExport extern char* call_conv xsb_get_init_error_type();
xsb_get_init_error_type = libxsb.xsb_get_init_error_type
xsb_get_init_error_type.restype = c_char_p
xsb_get_init_error_type.argtypes = []

# DllExport extern char* call_conv xsb_get_error_message(CTXTdecl);
xsb_get_error_message = libxsb.xsb_get_error_message
xsb_get_error_message.restype = c_char_p
xsb_get_error_message.argtypes = []

# DllExport extern char* call_conv xsb_get_error_type(CTXTdecl);
xsb_get_error_type = libxsb.xsb_get_error_type
xsb_get_error_type.restype = c_char_p
xsb_get_error_type.argtypes = []

# # DllExport extern void call_conv print_pterm(CTXTdeclc Cell, int, VarString*);
# print_pterm = libxsb.print_pterm
# print_pterm.restype = c_void
# print_pterm.argtypes = [c_cell,c_int,c_varstring_p]

# # DllExport extern char* p_charlist_to_c_string(CTXTdeclc prolog_term, VarString*, char*, char*);
# p_charlist_to_c_string = libxsb.p_charlist_to_c_string
# p_charlist_to_c_string.restype = c_char_p
# p_charlist_to_c_string.argtypes = [c_prolog_term,c_varstring_p,c_char_p,c_char_p]

# DllExport extern void c_string_to_p_charlist(CTXTdeclc char*, prolog_term, int, char*, char*);
c_string_to_p_charlist = libxsb.c_string_to_p_charlist
c_string_to_p_charlist.restype = c_void
c_string_to_p_charlist.argtypes = [c_char_p,c_prolog_term,c_int,c_char_p,c_char_p]

# DllExport extern void c_bytes_to_p_charlist(CTXTdeclc char*, size_t, prolog_term, int, char*, char*);
c_bytes_to_p_charlist = libxsb.c_bytes_to_p_charlist
c_bytes_to_p_charlist.restype = c_void
c_bytes_to_p_charlist.argtypes = [c_char_p,c_size_t,c_prolog_term,c_int,c_char_p,c_char_p]

#
# macros for constructing answer terms and setting and retrieving atomic
# values in them. To pass or retrieve complex arguments, you must use
# the lower-level ctop_* routines directly.
#

# build an answer term of arity i in reg 2 
def xsb_make_vars(i):
    return c2p_functor("ret", i, reg_term(2))

# set argument i of answer term to integer value v, for filtering 
def xsb_set_var_int(v, i):
    return c2p_int(v, p2p_arg(reg_term(2),i))

# set argument i of answer term to atom value s, for filtering 
def xsb_set_var_string(s, i):
    return c2p_string(s.encode('utf8'), p2p_arg(reg_term(2),i))

# set argument i of answer term to atom value f, for filtering
def xsb_set_var_float(f, i):
    return c2p_float(f, p2p_arg(reg_term(2),i))

# return integer argument i of answer term 
def xsb_var_int(i):
    return p2c_int(p2p_arg(reg_term(2), i))

# return string (atom) argument i of answer term 
def xsb_var_string(i):
    return p2c_string(p2p_arg(reg_term(2),i)).decode('utf8')

# return float argument i of answer term 
def xsb_var_float(i):
    return p2c_float(p2p_arg(reg_term(2),i))

#
# higher-level convenience functions
#

class XSBJSON:

    """ just a base class that indicates to_dict() and __init__(json_dict) are supported
        for JSON (de)-serialization """

    def to_dict(self):
        raise Exception ("to_dict is not implemented, but should be!")

@python_2_unicode_compatible
class XSBAtom(XSBJSON):

    def __init__ (self, name=None, json_dict=None):
        if json_dict:
            self.name = json_dict['name']
        else:
            self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'XSBAtom(name=%s)' % self.name

    def to_dict(self):
        return {'pt': 'atom', 'name': self.name}

@python_2_unicode_compatible
class XSBVariable(XSBJSON):

    def __init__ (self, name=None, json_dict=None):
        if json_dict:
            self.name = json_dict['name']
        else:
            self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'XSBVariable(name=%s)' % self.name

    def to_dict(self):
        return {'pt': 'variable', 'name': self.name}

@python_2_unicode_compatible
class XSBString(XSBJSON):

    def __init__ (self, value=None, json_dict=None):
        if json_dict:
            self.value = json_dict['value']
        else:
            self.value = value

    def __str__(self):
        return '"' + self.value + '"'

    def __repr__(self):
        return 'XSBString(value=%s)' % self.value

    def to_dict(self):
        return {'pt': 'string', 'value': self.value}

@python_2_unicode_compatible
class XSBFunctor(XSBJSON):

    def __init__ (self, name=None, args=None, json_dict=None):
        if json_dict:
            self.name = json_dict['name']
            self.args = json_dict['args']
        else:
            self.name = name
            self.args = args

    def __str__(self):
        if not self.args:
            return self.name
        return self.name + '(' + ','.join(map(lambda a: str(a), self.args)) + ')'

    def __repr__(self):
        return 'XSBFunctor(name=%s, args=%s)' % (self.name, repr(self.args))

    def __getitem__(self, sliced):
        return self.args[sliced]

    def to_dict(self):
        return {'pt': 'functor', 'name': self.name, 'args': self.args}

def xsb_hl_init(args):

    argv = (c_char_p * (len(args)+1))()
    for i, a in enumerate(args):
        argv[i] = a

    xsb_init(len(args), argv)

def xsb_hl_command(cmd):

    if isinstance(cmd, XSBFunctor):
        cmds = str(cmd) + '.'
    elif isinstance(cmd, string_types):
        cmds = cmd
    else:
        raise Exception ('XSBFunctor or String expected.')

    rcode = xsb_command_string(cmds)
    if rcode == XSB_FAILURE:
        raise Exception ("XSB Command %s %s failure (%d)." % (fname, repr(args), rcode))
    elif rcode == XSB_ERROR:
        raise Exception ("XSB Command %s %s error(%d): %s %s" % (fname, repr(args), rcode, xsb_get_error_type(), xsb_get_error_message()))
    elif rcode == XSB_OVERFLOW:
        raise Exception ("XSB Command %s %s overflow (%d)." % (fname, repr(args), rcode))
    
def xsb_term2py(term):

    if is_float(term):
        return p2c_float(term)

    elif is_int(term):
        return p2c_int(term)

    elif is_var(term):
        return XSBVar(name=p2c_string(term).decode('utf8', errors='ignore'))

    elif is_atom(term):
        return XSBAtom(name=p2c_string(term).decode('utf8', errors='ignore'))

    elif is_functor(term):

        name = p2c_functor(term)

        args = []
        for i in range(p2c_arity(term)):
            arg = p2p_arg(term, i+1)
            args.append(xsb_term2py(arg))

        return XSBFunctor(name=name, args=args)

    elif is_string(term):
        return XSBString(value=p2c_string(term).decode('utf8', errors='ignore'))

    else:
        list_len = c_int()
        if is_charlist(term, byref(list_len)):
            buf = create_string_buffer(list_len.value+1)
            p2c_chars(term, buf, list_len.value+1)
            return XSBString(value=buf.value.decode('utf8', errors='ignore'))
        else:
            res = []
            while is_list(term):
                res.append(xsb_term2py(p2p_car(term)))
                term = p2p_cdr(term)
        
            if not is_nil(term):
                res.append(xsb_term2py(term))
        
            return res

    raise Exception ('failed to detect datatype of %s' % xsb_format_term(term))

def xsb_hl_query(query):

    if isinstance(query, XSBFunctor):
        querys = str(query) + '.'
    elif isinstance(query, string_types):
        querys = query
    else:
        raise Exception ('XSBFunctor or String expected.')

    rcode = xsb_query_string(querys)
    res = []

    while not rcode:

        term = reg_term(2)
        # import pdb; pdb.set_trace()

        try:
            res.append(xsb_term2py(term))
        except Exception as e:
            xsb_close_query()
            raise e

        rcode = xsb_next()

    if rcode == XSB_ERROR:
        raise Exception ("XSB Query %s error(%d): %s %s" % (qs, rcode, xsb_get_error_type(), xsb_get_error_message()))
    elif rcode == XSB_OVERFLOW:
        raise Exception ("XSB Query %s overflow (%d)." % (qs, rcode))

    return res

#
# JSON interface
#

class XSBJSONEncoder(json.JSONEncoder):

    def default(self, o):

        if isinstance (o, XSBJSON):
            return o.to_dict()

        try:
            return json.JSONEncoder.default(self, o)
        except TypeError:
            import pdb; pdb.set_trace()


_xsb_json_encoder = XSBJSONEncoder()

def xsb_to_json(pl):
    return _xsb_json_encoder.encode(pl)

def _xsb_from_json(o):

    if o == None:
        return None

    if not 'pt' in o:
        return o

    if o['pt'] == 'atom':
        return XSBAtom(json_dict=o)
    if o['pt'] == 'functor':
        return XSBFunctor(json_dict=o)
    if o['pt'] == 'variable':
        return XSBVariable(json_dict=o)
    if o['pt'] == 'string':
        return XSBString(json_dict=o)

    raise Exception('cannot convert from json: %s .' % repr(o))

def json_to_xsb(jstr):
    return json.JSONDecoder(object_hook = _xsb_from_json).decode(jstr)


