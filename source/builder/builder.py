#!bin/python
from modules import *
import argparse, glob, os

p = argparse.ArgumentParser( description = 'Static file generator for DropPod.' )
g = p.add_mutually_exclusive_group()
p.add_argument( 'theme', nargs = '?', help = 'Theme to be built.' )
g.add_argument( '-c', '--compress', action = 'store_true', help = 'Compress static html pages into archive file.' )
g.add_argument( '-g', '--generate', action = 'store_true', help = 'Generate static html pages.' )
g.add_argument( '-l', '--list', action = 'store_true', help = 'List available themes')
p = p.parse_args()

theme = p.theme if p.theme is not None else 'all'
action = 'compress' if p.compress is True else 'generate' if p.generate is True else 'list'

if action == 'list':
    scanner.list()

if action == 'generate':
    generator.generator( theme )

if action == 'compress':
    compressor.compressor( theme )