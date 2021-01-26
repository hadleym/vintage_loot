import old_dict as od
import sys
import pandas as pd

def convert(c):
    clazz = c['class']
    old_item = c['old_item_name']
    try:
        return od.m[clazz.strip()][old_item.strip()]
    except KeyError as e:
        return c['old_item_name']

def deadshot(x):
    if (x.endswith('eadshot')):
        return 'Deadshot'
    else:
        return x

def dt(x):
    return pd.to_datetime(x, format='%m/%d/%Y')