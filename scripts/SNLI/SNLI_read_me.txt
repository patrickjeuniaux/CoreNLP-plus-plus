----------------
SNLI_read_me.txt
----------------




---------------------
UD-parsed SNLI corpus
---------------------





-------------
This document
-------------

This document is the 'read me' file for the UD-parsed Stanford Natural Language Inference (SNLI) Corpus.





-----------------------
Authors of the document
-----------------------

Patrick Jeuniaux & Ludovica Pannitto
University of Pisa
2018-05-13




----------
The corpus
----------


This 332 MB corpus contains 569033 sentence pairs from the SNLI corpus, analyzed with CoreNLP.


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

/extra/corpora/corpora-en/SNLI

/extra/corpora/corpora-en/SNLI/SNLI_read_me.txt

/extra/corpora/corpora-en/SNLI/1_original
/extra/corpora/corpora-en/SNLI/1_original/snli_1.0.zip
/extra/corpora/corpora-en/SNLI/1_original/README.txt

/extra/corpora/corpora-en/SNLI/2_per_pair
/extra/corpora/corpora-en/SNLI/2_per_pair/dev
/extra/corpora/corpora-en/SNLI/2_per_pair/test
/extra/corpora/corpora-en/SNLI/2_per_pair/train

/extra/corpora/corpora-en/SNLI/3_UD/
/extra/corpora/corpora-en/SNLI/3_UD/dev
/extra/corpora/corpora-en/SNLI/3_UD/test
/extra/corpora/corpora-en/SNLI/3_UD/train




---------------
The SNLI corpus
---------------

> The SNLI corpus (version 1.0) is a collection of 570k human-written English sentence pairs manually labeled for balanced classification with the labels entailment, contradiction, and neutral, supporting the task of natural language inference (NLI), also known as recognizing textual entailment (RTE).

Source: https://nlp.stanford.edu/projects/snli/


The original SNLI corpus is composed of three files (train, dev, test), containing pairs of sentences.

snli_1.0_dev.txt
snli_1.0_test.txt
snli_1.0_train.txt


These files are available here:

/extra/corpora/corpora-en/SNLI/1_original/snli_1.0.zip


For instance, the first two lines in 

snli_1.0_test.txt 

are :


gold_label  sentence1_binary_parse  sentence2_binary_parse  sentence1_parse sentence2_parse sentence1   sentence2   captionID   pairID  label1  label2  label3  label4  label5

neutral ( ( This ( church choir ) ) ( ( ( sings ( to ( the masses ) ) ) ( as ( they ( ( sing ( joyous songs ) ) ( from ( ( the book ) ( at ( a church ) ) ) ) ) ) ) ) . ) ) ( ( The church ) ( ( has ( cracks ( in ( the ceiling ) ) ) ) . ) )  (ROOT (S (NP (DT This) (NN church) (NN choir)) (VP (VBZ sings) (PP (TO to) (NP (DT the) (NNS masses))) (SBAR (IN as) (S (NP (PRP they)) (VP (VBP sing) (NP (JJ joyous) (NNS songs)) (PP (IN from) (NP (NP (DT the) (NN book)) (PP (IN at) (NP (DT a) (NN church))))))))) (. .)))    (ROOT (S (NP (DT The) (NN church)) (VP (VBZ has) (NP (NP (NNS cracks)) (PP (IN in) (NP (DT the) (NN ceiling))))) (. .)))    This church choir sings to the masses as they sing joyous songs from the book at a church.  The church has cracks in the ceiling.   2677109430.jpg#1    2677109430.jpg#1r1n neutral contradiction   contradiction   neutral neutral


The first line contains the variable names.

The second line is a line of data.

Each line of data corresponds to a pair of sentence.


Here is how we can understand the line of data:


neutral 

> gold_label: This is the label chosen by the majority of annotators. Where no majority exists, this is '-', and the pair should not be included when evaluating hard classification accuracy.



( ( This ( church choir ) ) ( ( ( sings ( to ( the masses ) ) ) ( as ( they ( ( sing ( joyous songs ) ) ( from ( ( the book ) ( at ( a church ) ) ) ) ) ) ) ) . ) )

> sentence1_binary_parse : The same parse as in sentence1_parse, but formatted for use in tree-structured neural networks with no unary nodes and no labels.



( ( The church ) ( ( has ( cracks ( in ( the ceiling ) ) ) ) . ) )

> sentence2_binary_parse : Same thing for sentence 2.




(ROOT (S (NP (DT This) (NN church) (NN choir)) (VP (VBZ sings) (PP (TO to) (NP (DT the) (NNS masses))) (SBAR (IN as) (S (NP (PRP they)) (VP (VBP sing) (NP (JJ joyous) (NNS songs)) (PP (IN from) (NP (NP (DT the) (NN book)) (PP (IN at) (NP (DT a) (NN church))))))))) (. .)))

> sentence1_parse: The parse produced by the Stanford Parser (3.5.2, case insensitive PCFG, trained on the standard training set augmented with the parsed Brown Corpus) in Penn Treebank format.




(ROOT (S (NP (DT The) (NN church)) (VP (VBZ has) (NP (NP (NNS cracks)) (PP (IN in) (NP (DT the) (NN ceiling))))) (. .)))

> sentence2_parse: Same thing for sentence 2.




This church choir sings to the masses as they sing joyous songs from the book at a church.  

> sentence1: The premise caption that was supplied to the author of the pair.



The church has cracks in the ceiling.

> sentence2: The hypothesis caption that was written by the author of the pair.



2677109430.jpg#1

> captionID: A unique identifier for each sentence1 from the original Flickr30k example.



2677109430.jpg#1r1n

> pairID: A unique identifier for each sentence1--sentence2 pair.



neutral contradiction   contradiction   neutral neutral

> label1  label2  label3  label4  label5 : annotator_labels : These are all of the individual labels from annotators in phases 1 and 2. The first label comes from the phase 1 author, and is the only label for examples that did not undergo phase 2 annotation. In a few cases, the one of the phase 2 labels may be blank, indicating that an annotator saw the example but could not annotate it.




These explanations were found here:

/extra/corpora/corpora-en/SNLI/1_original/README.txt






-----------------------
Methodology : procedure
-----------------------


1) Extract the pairs of sentences from:

snli_1.0_dev.txt
snli_1.0_test.txt
snli_1.0_train.txt

and placed them into individual files located here:

/extra/corpora/corpora-en/SNLI/2_per_pair

in their respective subfolders:

/extra/corpora/corpora-en/SNLI/2_per_pair/dev
/extra/corpora/corpora-en/SNLI/2_per_pair/test
/extra/corpora/corpora-en/SNLI/2_per_pair/train



Each file is named according to the id of the pair.

There is a file for each consistent line (i.e., gold label different from "-"). It is named as follows: gold_label _ pairID


For instance, the pair of the example above is saved in the file:


neutral_2677109430.jpg#1r1n


It is located here:

/extra/corpora/corpora-en/SNLI/2_per_pair/test/neutral_2677109430.jpg#1r1n



Its content is :

This church choir sings to the masses as they sing joyous songs from the book at a church.
The church has cracks in the ceiling.



The corpus size:

- 569033 files
- 82 MB











2) Run the CoreNLP parsing 


Use this configuration:

/home/patrick.jeuniaux/Documents/dashboard/projects/SNLI/SNLI_config.cnf


Note: all paths below will have to be updated once the definite version of the code is available.



[IO]
prog_folder: Documents/dashboard/projects
data_folder: to_backup/SNLI
start_folder:
ready_folder: %(data_folder)s/2_per_pair
processed_folder: %(data_folder)s/2_per_pair_DONE
ud_folder: %(data_folder)s/3_UD
log_file: %(data_folder)s/UD_parsing.log


[Safeguards]
included: SNLI_parsing.py
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
export SRC="/home/patrick.jeuniaux/Documents/dashboard/projects/SNLI"

$PYTHON $SRC/SNLI_parsing.py
```





The program was started on 2018-04-20 at 19:02 and ended at 22:02.

It took 3 hours and 31.89 seconds.




The corpus size:

- 569033 files
- 332 MB








-----------------------------
Methodology : output examples
-----------------------------

Most of the sentences that were parsed here were found in Schuster & Manning (2016). They do not originate from the SNLI corpus.






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

















