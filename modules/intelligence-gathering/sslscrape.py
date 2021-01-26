#!/usr/bin/env python
#####################################
# Installation module for SSLScrap
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Matthew Cranford"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update SSLScrap written by Peter Kim"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/cheetz/sslScrape.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="sslscrape"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git" # ToDo

# BYPASS UPDATES
BYPASS_UPDATE="YES"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="cd {INSTALL_LOCATION}, pip3 install ndg-httpsclient, pip3 install python-masscan"