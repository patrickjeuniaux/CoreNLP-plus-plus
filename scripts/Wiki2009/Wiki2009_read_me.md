# Wikipedia 2009 UD-parsed corpus

Wiki2009_read_me.md







## This document

This document is the 'read me' file for the Wikipedia 2009 UD-parse corpus.






## Author of the document

Patrick Jeuniaux
University of Pisa
2018-06-14






## The corpus


This 28 GB corpus contains about 2.6 million Wikipedia articles (2,694,786 files) that have been analyzed with CoreNLP.


The analysis covers:

- index
- word
- lemma
- POS
- named entity
- UD dependencies


Because we were especially interested by UD dependencies, we call this corpus a 'UD-parsed corpus'.








## Files structure


/extra/corpora/corpora-en/Wiki2009/

/extra/corpora/corpora-en/Wiki2009/Wiki2009_read_me.md


/extra/corpora/corpora-en/Wiki2009/1_old_UD/

/extra/corpora/corpora-en/Wiki2009/1_old_UD/one_file/
/extra/corpora/corpora-en/Wiki2009/1_old_UD/one_file/wiki.xml

/extra/corpora/corpora-en/Wiki2009/1_old_UD/four_files/
/extra/corpora/corpora-en/Wiki2009/1_old_UD/four_files/wikipedia-1.xml
/extra/corpora/corpora-en/Wiki2009/1_old_UD/four_files/wikipedia-2.xml
/extra/corpora/corpora-en/Wiki2009/1_old_UD/four_files/wikipedia-3.xml
/extra/corpora/corpora-en/Wiki2009/1_old_UD/four_files/wikipedia-4.xml


/extra/corpora/corpora-en/Wiki2009/2_per_text/
/extra/corpora/corpora-en/Wiki2009/2_per_text/wiki/


/extra/corpora/corpora-en/Wiki2009/3_UD/
/extra/corpora/corpora-en/Wiki2009/3_UD/wiki/

/extra/corpora/corpora-en/Wiki2009/Wiki2009_per_text.tar.gz
/extra/corpora/corpora-en/Wiki2009/Wiki2009_UD.tar.gz



## History of the corpus

1) In November 2009, a dump of Wikipedia English was downloaded.

This dump is no longer available due to a server crash in 2013.


2) In 2013, Gianluca Lebani used the Malt parser to UD parse the corpus

The result of this parse can be found in

/extra/corpora/corpora-en/Wiki2009/1_old_UD/

either in one XML file or in four XML files


3) In 2018, Patrick Jeuniaux reused the UD parse of Gianluca Lebani.

The plain text was recovered from the UD parse and put here:

/extra/corpora/corpora-en/Wiki2009/2_per_text/

Then that plain text was UD parsed with CoreNLP and put here:

/extra/corpora/corpora-en/Wiki2009/3_UD/






## Some statistics


/extra/corpora/corpora-en/Wiki2009/1_old_UD/one_file/
1 file
23 GB

/extra/corpora/corpora-en/Wiki2009/2_per_text/
2,694,786 files
5,390,702,284 characters
5.2 GB

/extra/corpora/corpora-en/Wiki2009/3_UD/
2,694,786 files
28 GB








## Methodology



### Procedure

The procedure was applied twice.

- Once in April, May 2018 on the "four files" version of the corpus.
- Once in June 2018 on the "one file" version of the corpus,

Both outcomes are identical in terms of number of files and size (GB).

Only the outcome of the last version ("one file") was kept.




#### 1. Preprocessing

Script: to be provided

Input: /extra/corpora/corpora-en/Wiki2009/1_old_UD/
Output: /extra/corpora/corpora-en/Wiki2009/2_per_text/


The goal of this step is to extract the plain texts (aka 'refurbished texts') from the original UD parse contained in the XML file:

/extra/corpora/corpora-en/Wiki2009/1_old_UD/wiki.xml



The preprocessing took :
- Four files: 4 hours and 32 minutes on 2018-04-24
- One file: 4 hours and 8 minutes on 2018-06-04



The program generated 2,694,786 files which can be found here:

/extra/corpora/corpora-en/Wiki2009/2_per_text/

(5.2 GB)


But you can get them in compressed form:

/extra/corpora/corpora-en/Wiki2009/Wiki2009_per_text.tar.gz

(2.1 GB)







#### 2. Parse the files with CoreNLP

Script: to be provided. It uses NLTK and CoreNLP.

Input: /extra/corpora/corpora-en/Wiki2009/2_per_text
Output: /extra/corpora/corpora-en/Wiki2009/3_UD



CoreNLP was downloaded and installed on the CoLingLab server
Source: https://stanfordnlp.github.io/CoreNLP/
Version: 2018-01-13



The CoreNLP server was used:

```
export CORENLP="/home/$USER/CoreNLP/2018-01-31/*"

java -cp "$CORENLP" -mx8g edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 300000
```




The preprocessing took :

- Four files: about 9 days (2018-04-24 --- 2018-05-02)
- One file: 6 days 16 hours (2018-06-05 --- 2018-06-12)


The first time (Four files), the program was interrupted several times to address issues of speed and memory, leading to the realization that a special procedure had to be put in place to take care of texts having lines greater than 5000 characters.

The second time (One file), the program was run in a smoother fashion, in three phases, the last two phases being devoted to process the files containing a line greater than 5000 characters.





The program generated 2,694,786 files which can be found here:

/extra/corpora/corpora-en/Wiki2009/3_UD/

(28 GB)



But you can get them in compressed form:

/extra/corpora/corpora-en/Wiki2009/Wiki2009_UD.tar.gz

(6.5 GB)











### Output format


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







#### Output examples


Most of the sentences that were parsed here were found in Schuster & Manning (2016). None of these sentences are from Wikipedia.



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








































