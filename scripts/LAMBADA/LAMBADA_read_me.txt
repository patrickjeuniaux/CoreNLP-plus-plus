-------------------
LAMBADA_read_me.txt
-------------------




-------------------------
UD-parsed LAMBADA dataset
-------------------------





-------------
This document
-------------

This document is the 'read me' file for the UD-parsed LAMBADA dataset.





-----------------------
Authors of the document
-----------------------

Patrick Jeuniaux
University of Pisa
2018-05-14




----------
The corpus
----------


This 5.2 GB corpus contains 2665 files from the LAMBADA dataset, analyzed with CoreNLP.


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

/extra/corpora/corpora-en/LAMBADA


/extra/corpora/corpora-en/LAMBADA/LAMBADA_read_me.txt




/extra/corpora/corpora-en/LAMBADA/0_rejected/

/extra/corpora/corpora-en/LAMBADA/0_rejected/readme.txt
/extra/corpora/corpora-en/LAMBADA/0_rejected/rejected_plain_text.txt





/extra/corpora/corpora-en/LAMBADA/1_original/

/extra/corpora/corpora-en/LAMBADA/1_original/lambada_control_test_data_plain_text.txt
/extra/corpora/corpora-en/LAMBADA/1_original/lambada_development_plain_text.txt
/extra/corpora/corpora-en/LAMBADA/1_original/lambada_test_plain_text.txt
/extra/corpora/corpora-en/LAMBADA/1_original/lambada-vocab-2.txt
/extra/corpora/corpora-en/LAMBADA/1_original/readme-up.txt

/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/

/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Adventure/
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Fantasy
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Historical
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Horror
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Humor
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Literature
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Mystery
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/New_Adult
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Other
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Romance
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Science_fiction
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Teen
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Themes
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Thriller
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Vampires
/extra/corpora/corpora-en/LAMBADA/1_original/train-novels/Young_Adult






/extra/corpora/corpora-en/LAMBADA/2_UD/

/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels
/extra/corpora/corpora-en/LAMBADA/2_UD/lambada_control_test_data_plain_text.txt
/extra/corpora/corpora-en/LAMBADA/2_UD/lambada_development_plain_text.txt
/extra/corpora/corpora-en/LAMBADA/2_UD/lambada_test_plain_text.txt


/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/

/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Adventure
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Fantasy
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Historical
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Horror
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Humor
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Literature
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Mystery
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/New_Adult
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Other
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Romance
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Science_fiction
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Teen
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Themes
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Thriller
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Vampires
/extra/corpora/corpora-en/LAMBADA/2_UD/train-novels/Young_Adult






----------
Statistics
----------

/extra/corpora/corpora-en/LAMBADA/0_rejected/
2 files (4.5 MB) 

/extra/corpora/corpora-en/LAMBADA/1_original/
2665 files (939 MB) 

+ 2 files that were ignored from the parsing:
lambada-vocab-2.txt
readme-up.txt


/extra/corpora/corpora-en/LAMBADA/2_UD/
2665 files (5.2 GB)






-------------------
The LAMBADA dataset
-------------------

> The LAMBADA dataset is a dataset to evaluate the capabilities of computational models for text understanding by means of a word prediction task. LAMBADA is a collection of narrative passages sharing the characteristic that human subjects are able to guess their last word if they are exposed to the whole passage, but not if they only see the last sentence preceding the target word. To succeed on LAMBADA, computational models cannot simply rely on local context, but must be able to keep track of information in the broader discourse. We show that LAMBADA exemplifies a wide range of linguistic phenomena, and that none of several state-of-the-art language models reaches accuracy above 1% on this novel benchmark.

Source: http://clic.cimec.unitn.it/lambada/


The original LAMBADA dataset is available in these two folders:

/extra/corpora/corpora-en/LAMBADA/0_rejected/
/extra/corpora/corpora-en/LAMBADA/1_original/







-----------------------
Methodology : procedure
-----------------------


1) Run the CoreNLP parsing 


Use this configuration:

/home/patrick.jeuniaux/Documents/dashboard/projects/LAMBADA/LAMBADA_config.cnf


Note: all paths below will have to be updated once the definite version of the code is available.



[IO]
prog_folder: Documents/dashboard/projects
data_folder: Documents/data/LAMBADA
start_folder:
ready_folder: %(data_folder)s/1_original
processed_folder: %(data_folder)s/1_original_DONE
ud_folder: %(data_folder)s/2_UD
log_file: %(data_folder)s/UD_parsing.log

[Safeguards]
included:1_UD_parsing.py
excluded:
ask_ready: yes
existing_output_folder_blocks: yes
existing_output_file_blocks: yes


[UD_parsing]
server_url: http://localhost:9000
use_server: yes
input_filename_regex: .*\.txt
paragraph_delimiter: \n
parse_per_paragraph: yes
tag_parse: yes
max_text_char_length: 100000
skip_text_char_length: 0
max_timeout: 300000
move_input_to_processed: yes
multiprocessing_method: between




Start the CoreNLP server:


```
cd ~/

export CORENLP="/home/patrick.jeuniaux/CoreNLP/2018-01-31/*"

java -cp "$CORENLP" -mx8g edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 300000

```


Run the Python script to parse the input for UD:


Note: the Python modules used by this script are here:

/home/patrick.jeuniaux/Documents/dashboard/projects/CoreNLP


```
cd ~/

export PYTHON=/home/patrick.jeuniaux/2Python/bin/python2
export SRC="/home/patrick.jeuniaux/Documents/dashboard/projects/LAMBADA"

$PYTHON $SRC/1_UD_parsing.py
```





The program was started on 2018-05-07 and ended on 2018-05-12.

It took about 6 days.




The corpus size:

- 2665 files
- 5.2 GB



Notice that, contrary to other similar parsing exercises, each line in the input (1_original) corresponds in the output (2_UD) to an XML tag of the type <p id=ID> ... </p> where ID stands for the line number (starting at 0), and ... to the UD parse of one or several sentences.

So :

- line 1 in input --> <p id="0"> ... </p>  in output
- line 2 in input --> <p id="1"> ... </p>  in output
- line 3 in input --> <p id="2"> ... </p>  in output

etc.








-----------------------------
Methodology : output examples
-----------------------------

Most of the sentences that were parsed here were found in Schuster & Manning (2016). They do not originate from the LAMBADA dataset.






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

















