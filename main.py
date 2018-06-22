#! /usr/bin/env python3
# coding: utf-8

# Name: Haar Cascade Creation
# Desc: Creation of custom Haar Cascades Classifiers
# Repo: https://github.com/IamPhytan/haar-cascade-creation
# Author: IamPhytan
# License: MIT
# Path: -

import json
import sys
import images_download

if __name__ == '__main__':

    assert (sys.version_info[0] >= 3), "Python 3 or a more recent version is required."

    with open('config.json', 'r') as f:
        config = json.load(f)

    download_links = images_download.get_download_links(config)
    print(download_links)
    images_download.neg_or_pos(download_links)
