"""

Parse the FakeNews data using CoreNLP through parser.py.
Patrick Jeuniaux
University of Pisa


/home/alessandro.bondielli/fake-news/data/notre-dame_dataset_raw/tweets/1121882902621491200.txt
/home/alessandro.bondielli/fake-news/data/notre-dame_dataset_raw/articles/32892_1122130024264605698.txt

IMPORTANT:
----------

1. You need to specify the configuration file. See CONFIG_PATH below.

2. You need to start the CoreNLP server manually before using this script.


Start the server:
-----------------

TEMP=/home/$USER/CoreNLP/shutdown

mkdir $TEMP

cd ~/

CORENLP="/home/$USER/CoreNLP/2018-01-31/*"

java -cp "$CORENLP" -Djava.io.tmpdir=$TEMP -mx4g edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 600000

nohup java -cp "$CORENLP" -Djava.io.tmpdir=$TEMP -mx4g edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 600000 &



Run this script:
----------------

cd ~/

PYTHON=/home/$USER/2Python/bin/python2

SRC="/home/$USER/Documents/repos/PPJMHJ/CoreNLP/scripts/FakeNews"

$PYTHON $SRC/UD_parsing.py

nohup $PYTHON $SRC/UD_parsing.py > UD_parsing.log 2>&1 & echo $! > UD_parsing.pid




Stop the server:
----------------

wget "localhost:9000/shutdown?key=`cat $TEMP`" -O -



To kill processes:
------------------


netstat -ap | grep :9000
kill -9 pid


"""

#######################################################################

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#######################################################################


CONFIG_PATH = "config.cnf"

#######################################################################

import os

# PROG_FOLDER = os.path.expanduser("~/Documents/repos/PPJMHJ/CoreNLP")
PROG_FOLDER = os.path.expanduser("~/Documents/repos/PPJMHJ")

sys.path.append(PROG_FOLDER)

from CoreNLP import factory

# import factory

#######################################################################


if __name__ == '__main__':

    factory.init(CONFIG_PATH)

    factory.run()
