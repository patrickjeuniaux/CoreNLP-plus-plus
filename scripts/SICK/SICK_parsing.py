"""
SICK_parsing.py
-----------------
Parse SICK dataset prepared by Ludovica Pannitto
for UD using CoreNLP through parser.py.
Patrick Jeuniaux
University of Pisa

IMPORTANT:
----------

1. You need to specify the configuration file. See CONFIG_PATH below.

2. You need to start the CoreNLP server manually before using this script.


Start the server:
-----------------

cd ~/

export CORENLP="/home/$USER/CoreNLP/2018-01-31/*"

java -cp "$CORENLP" -mx4g edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 30000

Run this script:
----------------

cd ~/

if [[ "$USER" == "patrick" ]]
then
    export PYTHON=/home/$USER/2Python/bin/python2
else
    export PYTHON=/home/$USER/2Python/bin/python2
fi

export SRC="/home/$USER/Documents/dashboard/projects/CoreNLP/datasets/SICK"


$PYTHON $SRC/SICK_parsing.py


Stop the server:
----------------

wget "localhost:9000/shutdown?key=`cat /tmp/corenlp.shutdown`" -O -



To kill processes:
------------------


netstat -ap | grep :9000
kill -9 pid

OR:

kill $( lsof -i:9000 -t )


"""

#######################################################################

import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

#######################################################################

#CONFIG_PATH = "/home/patrick/Documents/dashboard/projects/SICK/SICK_config.cnf"
CONFIG_PATH = "SICK_config.cnf"

#######################################################################

import os

HOME = os.path.expanduser("~")

PROG_FOLDER = os.path.join(
    HOME, "Documents", "dashboard", "projects", "CoreNLP")

sys.path.append(PROG_FOLDER)

from CoreNLP import factory

#######################################################################


if __name__ == '__main__':

    factory.init(CONFIG_PATH)

    factory.run()
