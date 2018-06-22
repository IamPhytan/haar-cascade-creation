
# Name: Haar Cascade Creation
# Desc: Creation of custom Haar Cascades Classifiers
# Repo: https://github.com/IamPhytan/haar-cascade-creation
# Author: IamPhytan
# License: MIT
# Path: -/images_download

FOLDERS = ['neg', 'pos']

def get_download_filed(config):
    # 1. Get links from wnids-request.txt
    with open('wnids-request.txt', 'r') as links_file:
        wnids = links_file.read().split('\n')

    wnid_links = dict([(row.split()[1].lower(),
                        "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=" + row.split()[0])
                       for row in wnids if len(row) > 0])
    print(wnid_links)

    # 2. Get requests from config file
    requests = [config['NEGATIVES'], config['POSITIVES']]
    for delim in ',;.':
        requests = [req.replace(delim, '') for req in requests]
    splitted_request = [req.lower().split(' ') for req in requests]
    print(splitted_request)

    # 3. Join the links and the request in a single dictionary
    for i in range(len(splitted_request)):
        request_links = dict()
        for avail_link in wnid_links.keys():
            if avail_link in splitted_request[i]:
                request_links[avail_link] = wnid_links[avail_link]
        splitted_request[i] = request_links
    download_links = dict(zip(FOLDERS, splitted_request))

    return download_links