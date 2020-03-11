import os

CHECKPOINT_FILE = '.checkpoint'

def add_flag(brand_name):
    if os.path.exists(CHECKPOINT_FILE):
        os.remove(CHECKPOINT_FILE)
    open(CHECKPOINT_FILE, 'w').write(brand_name)

def read():
    # will throw error if no file found catch in build.py
    brand_name = open(CHECKPOINT_FILE, 'r').read()
    return brand_name

def remove():
    os.remove(CHECKPOINT_FILE)