#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hnparse.core import extract

def test_extract_full_page():
    assert len(extract(1,30)) == 30

def test_extract_part_page():
    assert len(extract(1,15)) == 15

def test_extract_overflow():
    assert len(extract(1,50)) == 30

def test_extract_third_page():
    assert len(extract(3,20)) == 20
