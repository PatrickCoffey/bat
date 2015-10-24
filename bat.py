#!/usr/bin/python

"""
Bat.py
------

simple cli battery status solution!
"""

import sys
import os

_BAT_PATH='/sys/class/power_supply/'
_BAT_NAMES=[]
_CHARGE_FULL='charge_full'
_CHARGE_FULLD='charge_full_design'
_CHARGE_NOW='charge_now'
_CAPACITY_F='capacity'
_CAPACITY_NOW='capacity_level'
_PRESENT='present'

bats = []

class bat(object):
    """

    """

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self._update()

    def _update(self):
        self.charge_full = str(_get_value(os.path.join(self.path, _CHARGE_FULL))).strip()
        self.charge_now = str(_get_value(os.path.join(self.path, _CHARGE_NOW))).strip()
        self.charge_full_design = str(_get_value(os.path.join(self.path, _CHARGE_FULLD))).strip()
        self.capacity_now = str(_get_value(os.path.join(self.path, _CAPACITY_NOW))).strip()
        self.capacity_full = str(_get_value(os.path.join(self.path, _CAPACITY_F))).strip()
        self.present = str(_get_value(os.path.join(self.path, _PRESENT))).strip()
        self.percent = str((float(self.charge_now) / float(self.charge_full)) * 100) + "%"

    def __repr__(self):
        ret = "< battery=" + self.name 
        ret += ", charge_now=" + self.charge_now 
        ret += ", charge_full=" + self.charge_full
        ret += ", percent=" + self.percent
        ret += " >"
        return ret

def _get_value(path):
    with open(path, 'r') as f:
        ret = f.read()
    return ret


for i in range(10):
    _BAT_NAMES.append("BAT" + str(i))

for name in _BAT_NAMES:
    path = os.path.join(_BAT_PATH, name)
    if os.path.exists(path):
        bats.append(bat(name, path))

for battery in bats:
    print(battery)



