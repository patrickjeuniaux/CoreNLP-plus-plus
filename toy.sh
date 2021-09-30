#!/bin/bash

####################################################################################################################

# This script uses CoreNLP for toy data

####################################################################################################################

# Patrick Jeuniaux

# University of Pisa

####################################################################################################################

# Usage:

# export toy="/home/$USER/Documents/dashboard/projects/CoreNLP/toy.sh"
# . $toy

####################################################################################################################

# params
# coreNLP_format="conllu"
coreNLP_format="conll"
overwrite_ok=0 # 1 or 0

# I/O
CORENLP="/home/$USER/CoreNLP/2018-01-31"
#CORENLP="/home/$USER/CoreNLP/2018-02-27"
input_folder="/home/$USER/Documents/dashboard/data/inventions"
filelist="/tmp/filelist.txt"


if [[ $overwrite_ok != 1 ]] && [[ $overwrite_ok != 0 ]]; then
   echo "overwrite_ok must be either 1 or 0"
   kill -INT $$
fi


if [ "$coreNLP_format" = "conllu" ]; then
   output_folder="/home/$USER/Documents/dashboard/data/CoNLL-U"
elif [ "$coreNLP_format" = "conll" ]; then
   output_folder="/home/$USER/Documents/dashboard/data/CoNLL"
else
   echo "Choose 'conll' or 'connllu' as CoreNLP format"
   kill -INT $$
fi


####################################################################################################################

# Remove file lists if exists
[ -e $filelist ] && rm $filelist

# Create output folder if does not exists
mkdir -p "$output_folder"

# Determine which files must be copied in the filelist
for input_file in $input_folder/*; do

    input_filename=$(basename "$input_file")

    output_file="$output_folder"/$input_filename.$coreNLP_format

    if [ $overwrite_ok == 1 ] || [ ! -e "$output_file" ]; then

        echo "$input_file" >> $filelist

        echo "$input_file"
    fi

done

# Use CoreNLP

if [ -e $filelist ]; then
  java -cp "$CORENLP/*" -mx4g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,cleanxml,ssplit,pos,lemma,ner,depparse -filelist $filelist -outputFormat $coreNLP_format -outputDirectory "$output_folder"
fi

