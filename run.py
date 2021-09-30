"""
run.py
------

Patrick Jeuniaux
University of Pisa



----------
IMPORTANT:
----------


You need to start the CoreNLP server manually before using this script.



-----------------
Start the server:
-----------------

cd ~/

export CORENLP="/home/$USER/CoreNLP/2018-01-31/*"
export CORENLP="/home/$USER/CoreNLP/2018-02-27/*"

java -cp "$CORENLP" -mx4g edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 300000




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

export SRC="/home/$USER/Documents/dashboard/projects/CoreNLP"


$PYTHON $SRC/run.py toy.cnf 1
$PYTHON $SRC/run.py toy.cnf 2


----------------
Stop the server:
----------------

wget "localhost:9000/shutdown?key=`cat /tmp/corenlp.shutdown`" -O -



----------------
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

import os

HOME = os.path.expanduser("~")

PROG_FOLDER = os.path.join(
    HOME, "Documents", "dashboard", "projects")

sys.path.append(PROG_FOLDER)

#######################################################################

import argparse

#######################################################################

if __name__ == '__main__':

    description = "Example: --> python run.py toy.cnf 1"

    ap = argparse.ArgumentParser(description=description)
    ap.add_argument("conf", help="configuration file")
    ap.add_argument("op", type=int, help="operation (number)")
    args = ap.parse_args()

    conf = args.conf
    op = int(args.op)

    # UD parsing
    ############

    if op == 1:
        # 1. clean, per text
        from CoreNLP import preprocessor
        preprocessor.init(conf)
        preprocessor.clean_Wikipedia_dump()

    elif op == 2:
        # 2. UD parsing
        from CoreNLP import factory
        factory.init(conf)
        factory.run()
