#!/usr/bin/env python
#####################################
# Installation module for Subbrute
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Matthew Cranford"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update subbrute written by TheRook"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/TheRook/subbrute"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="subbrute"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git" # ToDo

# BYPASS UPDATES
BYPASS_UPDATE="YES"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="cd {INSTALL_LOCATION}, apt-get install python-dnspython"