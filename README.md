# Haar Cascade Creation
Creation of custom Haar Cascade Classifiers

![GitHub release](https://img.shields.io/github/tag/iamphytan/haar-cascade-creation.svg?label=version&style=flat-square)
![GitHub Issues](https://img.shields.io/github/issues/iamphytan/haar-cascade-creation.svg?style=flat-square)
![Downloads](https://img.shields.io/github/downloads/iamphytan/haar-cascade-creation/total.svg?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)

## Motivation
This script downloads the data and creates the files needed for 
the training of your own Haar Cascade Classifiers with OpenCV. 

This script is **made for Python3** and is based on a
 [tutorial][PythonProgramming] made by
 [@Sentdex](https://github.com/Sentdex).

## Installation
The following steps explain how to configure the script before running it:

1. Clone the repo: `git clone https://github.com/IamPhytan/haar-cascade-creation.git`
2. Download the requirements (or create a `virtualenv` before) : `pip3 install -r requirements.txt`
3. In [wnids-image-net.txt](wnids-image-net.txt), choose the WordNet Ids that will be used in your request
 to ImageNet. Insert them with appropriate keywords in [wnids-request.txt](wnids-request.txt).
4. Add your requests to the [configuration_file](config.json). The keywords that are used in the request are 
those that have been inserted in [wnids-request.txt](wnids-request.txt)
5. Run script: `python3 main.py`

## License
[MIT](https://opensource.org/licenses/MIT)

[PythonProgramming]: https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
[email-servers]: https://www.werockyourweb.com/list-outgoing-smtp-mail-servers/