#! /usr/bin/env python3

from distutils.dir_util import copy_tree
from shutil import copyfile

config_directories = ['i3', 'alacritty', 'nvim', 'polybar', 'rofi', 'compton']
config_files = ['.spacemacs']

for directory in config_directories:
    copy_tree('/home/zios/.config/' + directory, '/home/zios/project/dotfiles/' + directory)

for file in config_files:
    copyfile('/home/zios/' + file, '/home/zios/project/dotfiles/' + file)
