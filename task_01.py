#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """
     Args:
         None
        
     Returns:
         retstr

     Examples:
       >>> know_what_i_mean("hello",2)
           'Know what I mean? hellohello, nudge nudge'
     """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
