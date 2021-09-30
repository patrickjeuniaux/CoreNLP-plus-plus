"""
2_preprocess_old_UD.py
---------------------------
Preprocess the old UD parsed corpora before the new parsing.
Patrick Jeuniaux
University of Pisa



This function launches the plain text extraction of a linguistic parse.
The goal is to recreate the original text that was used,
putting each sentence on a separate line.

The following 'old' corpora have all the same format:
- BNC
- ukWac
- Wikipedia (2009)



Example of the parse:

<text id="bnc:1">
<s>
FACTSHEET   factsheet   NN  1   5   DEP
WHAT    what    WP  2   3   SBJ
IS  be  VBZ 3   1   NMOD
AIDS    AIDS    NP  4   0   ROOT
?   ?   SENT    5   0   ROOT
</s>

These lines are at the beginning of the parse for the BNC.

The plain text extraction will retrieve the sentence:

FACTSHEET WHAT IS AIDS ?



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

export SRC="/home/$USER/Documents/dashboard/projects/CoreNLP/datasets/Wiki2009"


$PYTHON $SRC/2_preprocess_old_UD.py


"""

#######################################################################

import sys
# reload(sys)  # Python 2
# sys.setdefaultencoding('utf8')

#######################################################################

#CONFIG_PATH = "/home/patrick/Documents/dashboard/projects/Wiki2009/Wiki2009_config.cnf"
CONFIG_PATH = "Wiki2009_config.cnf"

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

    preprocessor.extract_plain_text_from_parse()
