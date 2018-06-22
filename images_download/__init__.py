
# Name: Haar Cascade Creation
# Desc: Creation of custom Haar Cascades Classifiers
# Repo: https://github.com/IamPhytan/haar-cascade-creation
# Author: IamPhytan
# License: MIT
# Path: -/images_download

import urllib.request
import cv2
import numpy as np
import os
import notification as notif

FOLDERS = ['neg', 'pos']


def get_download_links(config):
    # 1. Get links from wnids-request.txt
    with open('wnids-request.txt', 'r') as links_file:
        wnids = links_file.read().split('\n')

    wnid_links = dict([(row.split()[1].lower(),
                        "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=" + row.split()[0])
                       for row in wnids if len(row) > 0])
    print(wnid_links)

    # 2. Get requests from config file
    requests = [config['REQUEST']['NEGATIVES'], config['REQUEST']['POSITIVES']]
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


def neg_or_pos(config, download_links):
    assert (isinstance(download_links, dict)), "Dictionary expected before downloading images"
    for folder_type, request_links in download_links.items():
        if bool(download_links[folder_type]):
            download_images(config, folder_type, request_links)
        elif not os.path.exists(os.path.join(os.getcwd(), folder_type)):
            os.makedirs(os.path.join(os.getcwd(), folder_type))


def download_images(config, folder, links):
    old_set_name = str()

    if folder == FOLDERS[0]:
        sz = 100
    else:
        sz = 50
    download_folder = os.path.join(os.getcwd(), folder)

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for set_name, images_link in links.items():
        print("Downloading images from", images_link)

        if bool(old_set_name):
            notif.set_completed(config, set_name, old_set_name)

        images_urls = urllib.request.urlopen(images_link).read().decode().split('\n')

        for idx, url in enumerate(images_urls):
            file_numb = len(
                [filename for filename in os.listdir(download_folder) if os.path.isfile(os.path.join(
                    download_folder, filename))])
            try:
                print(str(round(100 * idx / len(images_urls), 4)), '%', url)
                img_path = os.path.join(download_folder, str(file_numb).zfill(4) + '.jpg')
                urllib.request.urlretrieve(url, img_path)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    resized_image = cv2.resize(img, (sz, sz))
                    cv2.imwrite(img_path, resized_image)
            except Exception as e:
                print(str(e))

        old_set_name = set_name

    notif.last_set(config, old_set_name)


def find_litter(config):
    i = 0
    for file_type in FOLDERS:
        for img in os.listdir(file_type):
            for litter in os.listdir('litter'):
                try:
                    current_image_path = os.path.join(os.getcwd(), file_type, str(img))
                    litter = cv2.imread(os.path.join(os.getcwd(), 'litter', str(litter)))
                    question = cv2.imread(current_image_path)

                    if litter.shape == question.shape and not (np.bitwise_xor(litter, question).any()):
                        i += 1
                        print('Rubbish picture found at', current_image_path)
                        os.remove(current_image_path)

                except Exception as e:
                    print(str(e))

    notif.litter_deleted(config, i)


def create_files(config):
    for file_type in FOLDERS:
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)

            elif file_type == 'pos':
                line = file_type + '/' + img + ' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)

    notif.created_files(config)
