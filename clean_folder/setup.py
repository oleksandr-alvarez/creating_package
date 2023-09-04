from setuptools import setup, find_namespace_packages

name = 'clean_folder'
version = '1'
author = 'Viktor Mansilla'
author_email = 'alvarez2304@gmail.com'
description = 'Make your folder look clean'
packages = find_namespace_packages()
entry_points = {
    'console_scripts' : ['clean-folder = clean_folder.clean : main']
}



setup(
    name = name,
    version = version, 
    author = author,
    author_email = author_email,
    description = description,
    packages = packages,
    entry_points = entry_points
)