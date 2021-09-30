-----------------
ukWaC_read_me.txt
-----------------



---------------
UD-parsed ukWaC
---------------





-------------
This document
-------------

This document is the 'read me' file for the UD-parsed ukWaC.




----------------------
Author of the document
----------------------

Patrick Jeuniaux
University of Pisa
2019-05-21






----------
The corpus
----------

This corpus contains more than 2 million articles (2,692,642 articles) from ukWaC that have been analyzed with CoreNLP.




The analysis covers:

- index
- word
- lemma
- POS
- named entity 
- UD dependencies 


Because we were especially interested by UD dependencies, we call this corpus the 'UD-parsed ukWaC'.




-----
ukWaC
-----

> ukWaC: a 2 billion word corpus constructed from the Web limiting the crawl to the .uk domain and using medium-frequency words from the BNC as seeds. 

Source: http://wacky.sslmit.unibo.it/doku.php?id=corpora




---------------
Files structure
---------------

/extra/corpora/corpora-en/ukWaC/

/extra/corpora/corpora-en/ukWaC/1_old_UD/

/extra/corpora/corpora-en/ukWaC/1_old_UD/ukwac1.xml
/extra/corpora/corpora-en/ukWaC/1_old_UD/ukwac2.xml
/extra/corpora/corpora-en/ukWaC/1_old_UD/ukwac3.xml
/extra/corpora/corpora-en/ukWaC/1_old_UD/ukwac4.xml
/extra/corpora/corpora-en/ukWaC/1_old_UD/ukwac5.xml


/extra/corpora/corpora-en/ukWaC/2_per_text/

/extra/corpora/corpora-en/ukWaC/2_per_text/ukwac1/
/extra/corpora/corpora-en/ukWaC/2_per_text/ukwac2/
/extra/corpora/corpora-en/ukWaC/2_per_text/ukwac3/
/extra/corpora/corpora-en/ukWaC/2_per_text/ukwac4/
/extra/corpora/corpora-en/ukWaC/2_per_text/ukwac5/


/extra/corpora/corpora-en/ukWaC/2_per_text_issues/

/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac1/
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac2/
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac3/
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac4/
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac5/


/extra/corpora/corpora-en/ukWaC/3_UD/

/extra/corpora/corpora-en/ukWaC/3_UD/ukwac1/
/extra/corpora/corpora-en/ukWaC/3_UD/ukwac2/
/extra/corpora/corpora-en/ukWaC/3_UD/ukwac3/
/extra/corpora/corpora-en/ukWaC/3_UD/ukwac4/
/extra/corpora/corpora-en/ukWaC/3_UD/ukwac5/





----------
Statistics
----------

/extra/corpora/corpora-en/ukWaC/1_old_UD/
5 files
51 GB

/extra/corpora/corpora-en/ukWaC/2_per_text/
2,692,642 files
12 GB

/extra/corpora/corpora-en/ukWaC/3_UD/
2,692,642 files
62 GB







-----------------------
Methodology : procedure
-----------------------



1. Preprocessing
----------------

Input: /extra/corpora/corpora-en/ukWaC/1_original/
Output: /extra/corpora/corpora-en/ukWaC/2_per_text/


The goal of this step is to extract the plain texts (aka 'refurbished texts') from the original UD parse contained in the XML files: 

/extra/corpora/corpora-en/ukWaC/1_old_UD/ukwac1.xml
/extra/corpora/corpora-en/ukWaC/1_old_UD/ukwac2.xml
/extra/corpora/corpora-en/ukWaC/1_old_UD/ukwac3.xml
/extra/corpora/corpora-en/ukWaC/1_old_UD/ukwac4.xml
/extra/corpora/corpora-en/ukWaC/1_old_UD/ukwac5.xml



These texts are placed in separate files in these folders:

/extra/corpora/corpora-en/ukWaC/2_per_text/ukwac1/
/extra/corpora/corpora-en/ukWaC/2_per_text/ukwac2/
/extra/corpora/corpora-en/ukWaC/2_per_text/ukwac3/
/extra/corpora/corpora-en/ukWaC/2_per_text/ukwac4/
/extra/corpora/corpora-en/ukWaC/2_per_text/ukwac5/




It may appear strange to proceed in this way.

It would have been more direct to parse the original ukWaC.

However it was no longer available.

Hence this preprocessing step.






Script: 2_preprocess_old_UD.py, to be provided


The preprocessing took 9 hours and 36 minutes.


It generated a corpus of this size:

2,692,642 articles
12,399,360,064 characters
11.8 GB





2. Parse the files with CoreNLP
-------------------------------

Input: /extra/corpora/corpora-en/ukWaC/2_per_text
Output: /extra/corpora/corpora-en/ukWaC/3_UD/




CoreNLP was downloaded and installed on the CoLingLab server
Source: https://stanfordnlp.github.io/CoreNLP/
Version: 2018-01-13


The CoreNLP server was used:

```
export CORENLP="/home/$USER/CoreNLP/2018-01-31/*"

java -cp "$CORENLP" -mx8g edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 600000
```


A Python script invoking NLTK functions was used as a client to feed the CoreNLP server with input and treat its output.

Script: 3_UD_reparsing.py
Source: homemade / TO DO: make it available


TOTAL duration of the parsing : 

It is hard to determine. Work was initiated on 2018-04-06 and the parsing was complete on 2018-05-05, so about a month later.

In between, the program had to be improved in order to address issues caused by very long tables that resisted UD parsing.

The strategy was to put aside the texts that contained lines that were too long (> 5000 characters) and to process at a later stage.


All texts would eventually be parsed, using the normal pipeline, except 18 texts.

In each of these 18 texts, the offending line was manually removed, before conducting the parsing. 

You will find these texts and their corrected versions here:

/extra/corpora/corpora-en/ukWaC/2_per_text_issues/

/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac1/4708 : 107.7 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac1/171137 : 163:5 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac1/172773 : 63.1 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac1/333451 : 36.7 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac1/373786 : 141.8 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac1/437002: 59.2 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac2/470465 : 62.6 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac2/534366 : 95.5 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac2/545208 : 93.3 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac3/57259 : 100.2 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac3/114685 : 163.2 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac3/150709 : 167 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac4/297847 : 94.8 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac4/492916 : 149.8 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac5/28147 : 128.1 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac5/28193 : 72.5 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac5/169256 : 61.2 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac5/312715 : 40.7 KB
/extra/corpora/corpora-en/ukWaC/2_per_text_issues/ukwac5/411391 : 128.1 KB



Eventually, all 2,692,642 files were parsed, leading to a corpus of 62 GB, available here:

/extra/corpora/corpora-en/ukWaC/3_UD/





---------------------------
Methodology : output format
---------------------------

The output format is a variant of CoNLL-U.

It is slightly more concise than CoNLL-U.

It also includes enhanced ++ universal dependencies (UD).

Enhanced ++ UD are described in this paper:

Schuster, S., & Manning, C. D. (2016). Enhanced English Universal Dependencies: An Improved Representation for Natural Language Understanding Tasks.


More information on universal dependencies: http://universaldependencies.org



The file format has one dependent (token/child) per line.



For each line, we have the following columns:

- index
- word
- lemma
- POS
- named entity 
- UD dependencies 



Note 1 :

Examples of named entities: 
PERSON, TITLE, LOCATION (or O if there is none)



Note 2 :

'UD dependencies' is a comma-separated list of RELATION_NAME=HEAD_INDEX pairs 

Example: nsubj=2,nsubj:xsubj=4






-----------------------------
Methodology : output examples
-----------------------------

Most of the sentences that were parsed here were found in Schuster & Manning (2016). None of these sentences come from ukWaC.



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



























