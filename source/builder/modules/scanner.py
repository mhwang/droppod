from . import common
import glob

def list():
    themes = common.getThemes()
    for theme in themes:
        print( theme )