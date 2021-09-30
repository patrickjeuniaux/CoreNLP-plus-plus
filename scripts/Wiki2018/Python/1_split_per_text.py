"""
1_split_per_text.py
-------------------
Preprocess the raw corpus before parsing.
Patrick Jeuniaux
University of Pisa

IMPORTANT:
----------

Before running this script, you need to:

1. download a Wikipedia dump
2. extract the Wikipedia dump


1. download a Wikipedia dump
----------------------------

Check the appropriate date here
https://dumps.wikimedia.org/enwiki/latest/

The current dump is from
3 February 2018 (i.e., 2018-02-03).


cd /home/patrick/Documents/data/
mkdir "Wiki20180203"
cd "2018-02-03"
wget https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2



2. extract the Wikipedia dump
-----------------------------


Download and install Wikiextractor:
-----------------------------------

cd "/home/patrick/Documents/repos/"
mkdir "Giuseppe Attardi"
cd "/home/patrick/Documents/repos/Giuseppe Attardi/"
git clone https://github.com/attardi/wikiextractor.git
cd "/home/patrick/Documents/repos/Giuseppe Attardi/wikiextractor"

sudo python setup.py install


Run Wikiextractor:
------------------

cd "/home/patrick/Documents/repos/Giuseppe Attardi/wikiextractor"

python WikiExtractor.py -o "/home/patrick/Documents/data/Wiki20180203/1_raw" "/home/patrick/Documents/data/Wiki20180203/enwiki-latest-pages-articles.xml.bz2"



---> FINALLY :


----------------
Run this script:
----------------

cd ~/

if [[ "$USER" == "patrick" ]]
then
    export PYTHON=/home/$USER/2Python/bin/python2
else
    export PYTHON=/home/$USER/2Python/bin/python2
fi

export SRC="/home/$USER/Documents/dashboard/projects/CoreNLP/datasets/Wiki2018"


$PYTHON $SRC/1_split_per_text.py


"""

#######################################################################

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#######################################################################

#CONFIG_PATH = "/home/patrick/Documents/dashboard/projects/Wiki2018/config.cnf"
CONFIG_PATH = "config.cnf"

#######################################################################

import os

HOME = os.path.expanduser("~")

PROG_FOLDER = os.path.join(
    HOME, "Documents", "dashboard", "projects", "CoreNLP")

sys.path.append(PROG_FOLDER)

from CoreNLP import preprocessor

#######################################################################


if __name__ == '__main__':

    preprocessor.init(CONFIG_PATH)

    preprocessor.clean_Wikipedia_dump()
