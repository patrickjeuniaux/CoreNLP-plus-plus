"""
1_make_samples.py
---------------------------
Make samples of data sets to test the next scripts.
Patrick Jeuniaux
University of Pisa


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

export SRC="/home/$USER/Documents/dashboard/projects/BNC"


$PYTHON $SRC/1_make_samples.py


"""

#######################################################################

import sys
# reload(sys)  # Python 2
# sys.setdefaultencoding('utf8')

#######################################################################

#CONFIG_PATH = "/home/patrick/Documents/dashboard/projects/old_UD/BNC_config.cnf"
CONFIG_PATH = "BNC_config.cnf"

#######################################################################

import os

HOME = os.path.expanduser("~")

PROG_FOLDER = os.path.join(
    HOME, "Documents", "dashboard", "projects", "UD_parsing")

sys.path.append(PROG_FOLDER)

from CoreNLP import preprocessor

#######################################################################


if __name__ == '__main__':

    # STEP 1
    ########

    preprocessor.init(CONFIG_PATH)

    BNC = "/home/patrick/Documents/data/BNC/1_old_UD"
    ukWac = "/home/patrick/Documents/data/ukWac/1_old_UD"
    Wiki2013 = "/home/patrick/Documents/data/Wiki2013/1_old_UD"

    out = preprocessor.CONFIG.start_folder

    # max number of lines
    mnl = 29065

    #preprocessor.make_sample_files_from_simple_folder(BNC, out, mnl)
    #preprocessor.make_sample_files_from_simple_folder(ukWac, out, mnl)
    #preprocessor.make_sample_files_from_simple_folder(Wiki2013, out, mnl)

    # STEP 2
    ########

    input_file = "/home/patrick/Documents/data/ukWac/1_old_UD/ukwac1.xml"

    output_file = "/home/patrick/Documents/data/old_UD_TEST/1_old_UD/ukWac_8001_cp1252.txt"

    start_line = '<text id="ukwac:http://www.futurelab.org.uk/research/personalisation/report_01.htm">'

    preprocessor.make_specific_sample_file(input_file, output_file, start_line)
