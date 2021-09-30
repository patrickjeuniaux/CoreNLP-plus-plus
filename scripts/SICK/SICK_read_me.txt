----------------
SICK_read_me.txt
----------------




----------------------
UD-parsed SICK dataset
----------------------





-------------
This document
-------------

This document is the 'read me' file for the UD-parsed SICK data set.





-----------------------
Authors of the document
-----------------------

Patrick Jeuniaux & Ludovica Pannitto
University of Pisa
2018-04-23




-----------
The dataset
-----------


This 4.9 MB dataset contains 9840 sentence pairs from the SICK dataset, analyzed with CoreNLP.


The CoreNLP analysis covers:

- index
- word
- lemma
- POS
- named entity 
- UD dependencies 

(see the 'output examples' section for more explanations)






---------------
Files structure
---------------

/extra/corpora/corpora-en/SICK

/extra/corpora/corpora-en/SICK/SICK_read_me.txt

/extra/corpora/corpora-en/SICK/1_original
/extra/corpora/corpora-en/SICK/1_original/SICK.txt
/extra/corpora/corpora-en/SICK/1_original/readme.txt

/extra/corpora/corpora-en/SICK/2_per_pair

/extra/corpora/corpora-en/SICK/3_UD/





----------------
The SICK dataset
----------------

> Sentences Involving Compositional Knowledge

> A data set for compositional distributional semantics

> Distributional Semantic Models (DSMs) approximate the meaning of words with vectors summarizing their patterns of co-occurrence in corpora. Recently, several compositional extensions of DSMs (Compositional DSMs, or CDSMs) have been proposed, with the purpose of representing the meaning of phrases and sentences by composing the distributional representations of the words they contain. SICK (Sentences Involving Compositional Knowledge) provides a benchmark for CDSM testing. In fact, it includes a large number of sentence pairs that are rich in the lexical, syntactic and semantic phenomena that CDSMs are expected to account for (e.g., contextual synonymy and other lexical variation phenomena, active/passive and other syntactic alternations, impact of negation, determiners and other grammatical elements), but do not require dealing with other aspects of existing sentential data sets (e.g., STS, RTE) that are not within the scope of compositional distributional semantics.

> The SICK data set consists of 10,000 English sentence pairs, built starting from two existing paraphrase sets: the 8K ImageFlickr data set (http://nlp.cs.illinois.edu/HockenmaierGroup/data.html) and the SEMEVAL-2012 Semantic Textual Similarity Video Descriptions data set (http://www.cs.york.ac.uk/semeval-2012/task6/index.php?id=data). Each sentence pair is annotated 
for relatedness in meaning and for the entailment relation between the two elements.

Actually, the real number of sentence pairs is : 9840

> The number of planned sentence pairs was 10,000 but at the end of the data set creation process 160 pairs had to be excluded.


Sources: 

http://clic.cimec.unitn.it/composes/sick.html

/extra/corpora/corpora-en/SICK/1_original/readme.txt

A SICK cure for the evaluation of compositional distributional semantic models
http://clic.cimec.unitn.it/marco/publications/marelli-etal-sick-lrec2014.pdf






The original SICK dataset is made of one file:

/extra/corpora/corpora-en/SICK/1_original/SICK.txt




For instance, the first two lines in 

SICK.txt

are :




pair_ID sentence_A  sentence_B  entailment_label    relatedness_score   entailment_AB   entailment_BA   sentence_A_original sentence_B_original sentence_A_dataset  sentence_B_dataset  SemEval_set

1   A group of kids is playing in a yard and an old man is standing in the background   A group of boys in a yard is playing and a man is standing in the background    NEUTRAL 4.5 A_neutral_B B_neutral_A A group of children playing in a yard, a man in the background. A group of children playing in a yard, a man in the background. FLICKR  FLICKR  TRAIN





The first line contains the variable names.

The second line is a line of data.

Each line of data corresponds to a pair of sentence.


Here is how we can understand the line of data:


1

> pair_ID: sentence pair ID


A group of kids is playing in a yard and an old man is standing in the background

> sentence_A: sentence A



A group of boys in a yard is playing and a man is standing in the background

> sentence_B: sentence B



NEUTRAL

> entailment_label: textual entailment gold label (NEUTRAL, ENTAILMENT, or CONTRADICTION)


4.5

> relatedness_score: semantic relatedness gold score (on a 1-5 continuous scale)



A_neutral_B

> entailment_AB: entailment for the A-B order (A_neutral_B, A_entails_B, or A_contradicts_B)



B_neutral_A

> entailment_BA: entailment for the B-A order (B_neutral_A, B_entails_A, or B_contradicts_A)



A group of children playing in a yard, a man in the background. 

> sentence_A_original: original sentence from which sentence A is derived



A group of children playing in a yard, a man in the background.

> sentence_B_original: original sentence from which sentence B is derived



FLICKR

> sentence_A_dataset: dataset from which the original sentence A was extracted (FLICKR vs. SEMEVAL)


FLICKR

> sentence_B_dataset: dataset from which the original sentence B was extracted (FLICKR vs. SEMEVAL)


TRAIN

> SemEval_set: set including the sentence pair in SemEval 2014 Task 1 (TRIAL, TRAIN, or TEST)




These explanations were found here:

/extra/corpora/corpora-en/SICK/1_original/readme.txt







-----------------------
Methodology : procedure
-----------------------


1) Extract the pairs of sentences from:

/extra/corpora/corpora-en/SICK/1_original/SICK.txt

and place them into individual files located here:

/extra/corpora/corpora-en/SICK/2_per_pair



Each file is named as follows: id_ pair_ID . entailment_label


For instance, the pair of the example above is saved in the file:


id_1.NEUTRAL


It is located here:

/extra/corpora/corpora-en/SICK/2_per_pair/id_1.NEUTRAL



Its content is :

A group of kids is playing in a yard and an old man is standing in the background
A group of boys in a yard is playing and a man is standing in the background





The dataset size:

- 9840 files
- 1.2 MB











2) Run the CoreNLP parsing 


Use this configuration:

/home/patrick.jeuniaux/Documents/dashboard/projects/SICK/SICK_config.cnf


Note: all paths below will have to be updated once the definite version of the code is available.



[IO]
prog_folder: Documents/dashboard/projects
data_folder: to_backup/SICK
start_folder:
ready_folder: %(data_folder)s/2_per_pair
processed_folder: %(data_folder)s/2_per_pair_DONE
ud_folder: %(data_folder)s/3_UD
log_file: %(data_folder)s/UD_parsing.log


[Safeguards]
included: SICK_parsing.py
excluded:
ask_ready: yes
existing_output_folder_blocks: no
existing_output_file_blocks: no


[UD_parsing]
server_url: http://localhost:9000
use_server: yes
max_text_char_length: 1000
skip_text_char_length: 5000
max_timeout: 300000
move_input_to_processed: yes
multiprocessing_method: between




Start the CoreNLP server:


```
cd ~/

export CORENLP="/home/patrick.jeuniaux/CoreNLP/2018-01-31/*"

java -cp "$CORENLP" -mx4g edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 30000

```


Run the Python script to parse the input for UD:


Note: the Python modules used by this script are here:

/home/patrick.jeuniaux/Documents/dashboard/projects/CoreNLP


```
cd ~/

export PYTHON=/home/patrick.jeuniaux/2Python/bin/python2
export SRC="/home/patrick.jeuniaux/Documents/dashboard/projects/SICK"

$PYTHON $SRC/SICK_parsing.py
```





The program was started on 2018-04-23 at 14:23 and ended at 15:32.

It took 1 hour, 9 minutes, and 27 seconds.




The corpus size:

- 9840 files
- 4.9 MB








-----------------------------
Methodology : output examples
-----------------------------

Most of the sentences that were parsed here were found in Schuster & Manning (2016). They do not originate from the SICK dataset.






---

1 Fred Fred NNP PERSON nsubj=2,nsubj:xsubj=4
2 started start VBD O ROOT=0
3 to to TO O mark=4
4 laugh laugh NN O xcomp=2
5 . . . O punct=2

---

1 The the DT O det=2
2 house house NN O ROOT=0
3 on on IN O case=5
4 the the DT O det=5
5 hill hill NN O nmod:on=2
6 . . . O punct=2

---

1 He he PRP O nsubj=2
2 brushed brush VBD O ROOT=0
3 his he PRP$ O nmod:poss=4
4 teeth tooth NNS O dobj=2
5 after after IN O mark=6
6 eating eat VBG O advcl:after=2
7 dinner dinner NN O dobj=6
8 . . . O punct=2

---

1 Apples apple NNS O ROOT=0
2 and and CC O cc=1
3 bananas banana NNS O conj:and=1
4 , , , O punct=1
5 or or CC O cc=1
6 oranges orange NNS O conj:or=1
7 . . . O punct=1

---

1 Sue sue VB O nsubj=5
2 and and CC O cc=1
3 Paul Paul NNP PERSON conj:and=1,nsubj=5
4 are be VBP O aux=5
5 running run VBG O ROOT=0
6 . . . O punct=5

---

1 The the DT O det=5
2 long long JJ O amod=5
3 and and CC O cc=2
4 wide wide JJ O conj:and=2,amod=5
5 river river NN TITLE ROOT=0
6 . . . O punct=5

---

1 The the DT O det=2
2 store store NN O nsubj=3,nsubj=5
3 buys buy VBZ O ROOT=0
4 and and CC O cc=3
5 sells sell VBZ O conj:and=3
6 cameras camera NNS O dobj=3
7 . . . O punct=3

---

1 She she PRP O nsubj=3,nsubj=5
2 was be VBD O aux=3
3 reading read VBG O ROOT=0
4 or or CC O cc=3
5 watching watch VBG O conj:or=3
6 a a DT O det=7
7 movie movie NN O dobj=3
8 . . . O punct=3

---

1 Sue sue VB O nsubj=2,nsubj:xsubj=4
2 wants want VBZ O ROOT=0
3 to to TO O mark=4
4 buy buy VB O xcomp=2
5 a a DT O det=6
6 hat hat NN O dobj=4
7 . . . O punct=2

---

1 Both both DT O det:qmod=4
2 of of IN O mwe=1
3 the the DT O det=4
4 girls girl NNS O nsubj=6
5 are be VBP O aux=6
6 reading read VBG O ROOT=0
7 . . . O punct=6

---

1 A a DT O det:qmod=4
2 bunch bunch NN O mwe=1
3 of of IN O mwe=1
4 people people NNS O nsubj=6
5 are be VBP O aux=6
6 coming come VBG O ROOT=0
7 . . . O punct=6

---

1 The the DT O det=2
2 house house NN O ROOT=0
3 in in IN O case=7
4 front front NN O mwe=3
5 of of IN O mwe=3
6 the the DT O det=7
7 hill hill NN O nmod:in_front_of=2
8 . . . O punct=2

---

1 I I PRP O nsubj=2,nsubj:xsubj=4
2 bike bike NN O ROOT=0
3 to to TO O mark=4
4 work work VB O xcomp=2
5 and and CC O cc=4
6 I I PRP O nsubj=7
7 bike bike NN O xcomp=2,conj:and=4
8 from from IN O case=9
9 work work NN O nmod:from=7
10 . . . O punct=2

---

1 I I PRP O nsubj=2
2 bike bike NN O ROOT=0,conj:and=2
3 to to TO O case=6
4 and and CC O cc=3
5 from from IN O conj:and=3
6 work work NN O nmod:to=2,nmod:from=2
7 . . . O punct=2

---

1 She she PRP O nsubj=2,nsubj=2
2 flew fly VBD O ROOT=0,conj:or=2
3 to to TO O case=4
4 Bali Bali NNP LOCATION nmod:to=2
5 or or CC O cc=2
6 to to TO O case=7
7 Turkey Turkey NNP COUNTRY nmod:to=2
8 . . . O punct=2

---

1 The the DT O det=2
2 boy boy NN O ROOT=0,nsubj=4
3 who who WP O ref=2
4 lived live VBD O acl:relcl=2
5 . . . O punct=2

---

1 Everybody everybody NN O nsubj=2,nsubj:xsubj=4
2 wants want VBZ O ROOT=0
3 to to TO O mark=4
4 buy buy VB O xcomp=2
5 a a DT O det=6
6 house house NN O dobj=4
7 . . . O punct=2

---

1 Everybody everybody NN O nsubj=2
2 wants want VBZ O ROOT=0
3 that that IN O mark=5
4 everybody everybody NN O nsubj=5
5 buys buy VBZ O ccomp=2
6 a a DT O det=7
7 house house NN O dobj=5
8 . . . O punct=2

---

1 Everybody everybody NN O compound=2
2 sleeps sleep NNS O ROOT=0
3 or or CC O cc=2
4 is be VBZ O cop=5
5 awake awake RB O conj:or=2
6 . . . O punct=2

---

1 Everybody everybody NN O compound=2
2 sleeps sleep NNS O nsubj=6
3 or or CC O cc=2
4 everybody everybody NN O conj:or=2,nsubj=6
5 is be VBZ O cop=6
6 awake awake RB O ROOT=0
7 . . . O punct=6

---

1 Sue sue VB O nsubj=5
2 and and CC O cc=1
3 Mary Mary NNP PERSON conj:and=1,nsubj=5
4 are be VBP O aux=5
5 carrying carry VBG O ROOT=0
6 a a DT O det=7
7 piano piano NN O dobj=5
8 . . . O punct=5

---

1 The the DT O det=4
2 quick quick JJ O amod=4
3 brown brown JJ O amod=4
4 fox fox NN O nsubj=5
5 jumps jump VBZ O ROOT=0
6 over over IN O case=9
7 the the DT O det=9
8 lazy lazy JJ O amod=9
9 dog dog NN O nmod:over=5
10 . . . O punct=5

---

1 Silvio Silvio NNP PERSON compound=2
2 Berlusconi Berlusconi NNP PERSON nsubj=4
3 has have VBZ O aux=4
4 met meet VBN O ROOT=0
5 the the DT O det=6
6 Pope Pope NNP TITLE dobj=4
7 in in IN O case=9
8 Vatican Vatican NNP LOCATION compound=9
9 City City NNP LOCATION nmod:in=4
10 . . . O punct=4

---

1 Sangla Sangla NNP LOCATION compound=2
2 Valley Valley NNP CITY ROOT=0
3 in in IN O case=5
4 Himachal Himachal NNP LOCATION compound=5
5 Pradesh Pradesh NNP LOCATION nmod:in=2
6 in in IN O case=7
7 India India NNP COUNTRY nmod:in=5
8 . . . O punct=2

















