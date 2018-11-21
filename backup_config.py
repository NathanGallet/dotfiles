#! /usr/bin/env python3

from distutils.dir_util import copy_tree

config_files = ['i3', 'alacritty', 'nvim', 'polybar', 'rofi']

for config in config_files:
    copy_tree('/home/zios/.config/'+config, '/home/zios/project/dotfiles/'+config)
