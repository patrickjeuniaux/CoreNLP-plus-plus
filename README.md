
# CoreNLP ++

Patrick Jeuniaux \
Brussels, \
2021-09-30


## About this project

I wrote most of this code in 2018 during my stay in Pisa, Italy, while I was a post-doctoral researcher working with Prof. Alessandro Lenci, in the Computational Linguistics Laboratory (https://colinglab.fileli.unipi.it/), Department of Philology, Literature, and Linguistics, University of Pisa.

Its purpose was to tackle the task of parsing a large corpus of texts using CoreNLP (https://stanfordnlp.github.io/CoreNLP/) to segment the text at the word level and provide linguistic annotations such as enhanced ++ universal dependencies.

The strategy that is adopted here to address the issue of size is to split the corpus in multiple files and then process them in parallel using multiprocessing.

The code contains a 'preprocessor' to first split a corpus in different text files. Then the rest of the code can be used to parse them. A 'config_reader' is used to specify parameters to run the code.

As shown in the scripts folder, this code has been used for the following corpora or projects:

- BNC
- FakeNews
- LAMBADA
- SICK
- SNLI
- ukWaC
- Wiki2009
- Wiki2018



## State of the code

The code contains some bits resulting from trials and errors, hasn't been cleaned and should probably be refactored. It also contains some working documents used at the time of working on the project that may be out of date. A proper documentation should be written.

Unfortunately I haven't had the time to do all that yet.

Feel free to inspect the project and use it as you see fit (but at your own perils).


## License

The code is distributed under the Unlicense (i.e., it belongs to the public domain).

https://unlicense.org/




## Communication


If using the code played a substantial role in your own project, please be kind enough to acknowledge this by simply citing the URL of the repository.

I imagine that projects such as this one already exist but at the time of writing it I did not find any that would suit my problem, so I engineered this solution. I would be grateful if someone would show me where I could find better code to accomplish the same task.

Please don't hesitate to write to me if you have questions regarding the code or suggestions for improvements.




## Output format

The output format I use through CoreNLP is a variant of CoNLL-U.

It is slightly more concise than CoNLL-U.

It also includes enhanced ++ universal dependencies (UD).

Enhanced ++ UD are described in this paper:

Schuster, S., & Manning, C. D. (2016). Enhanced English Universal Dependencies: An Improved Representation for Natural Language Understanding Tasks. In Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC 2016) (pp. 2371–2378). Retrieved from http://nlp.stanford.edu/~sebschu/pubs/schuster-manning-lrec2016.pdf



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




## Output examples

Most of the sentences that were parsed here were found in Schuster & Manning (2016).

---

The Autralian scientist discovered the star with the telescope.

	1   The the DT  O   det=3
	2   Autralian   autralian   JJ  MISC    amod=3
	3   scientist   scientist   NN  TITLE   nsubj=4
	4   discovered  discover    VBD O   ROOT=0
	5   the the DT  O   det=6
	6   star    star    NN  O   dobj=4
	7   with    with    IN  O   case=9
	8   the the DT  O   det=9
	9   telescope   telescope   NN  O   nmod:with=4
	10  .   .   .   O   punct=4

---

Fred started to laugh.

	1 Fred Fred NNP PERSON nsubj=2,nsubj:xsubj=4
	2 started start VBD O ROOT=0
	3 to to TO O mark=4
	4 laugh laugh NN O xcomp=2
	5 . . . O punct=2

---

The house on the hill.

	1 The the DT O det=2
	2 house house NN O ROOT=0
	3 on on IN O case=5
	4 the the DT O det=5
	5 hill hill NN O nmod:on=2
	6 . . . O punct=2

---

He brushed his teeth after eating dinner.

	1 He he PRP O nsubj=2
	2 brushed brush VBD O ROOT=0
	3 his he PRP$ O nmod:poss=4
	4 teeth tooth NNS O dobj=2
	5 after after IN O mark=6
	6 eating eat VBG O advcl:after=2
	7 dinner dinner NN O dobj=6
	8 . . . O punct=2

---

Apples and bananas, or oranges.

	1 Apples apple NNS O ROOT=0
	2 and and CC O cc=1
	3 bananas banana NNS O conj:and=1
	4 , , , O punct=1
	5 or or CC O cc=1
	6 oranges orange NNS O conj:or=1
	7 . . . O punct=1

---

Sue and Paul are running.

	1 Sue sue VB O nsubj=5
	2 and and CC O cc=1
	3 Paul Paul NNP PERSON conj:and=1,nsubj=5
	4 are be VBP O aux=5
	5 running run VBG O ROOT=0
	6 . . . O punct=5

---

The long and wide river.

	1 The the DT O det=5
	2 long long JJ O amod=5
	3 and and CC O cc=2
	4 wide wide JJ O conj:and=2,amod=5
	5 river river NN TITLE ROOT=0
	6 . . . O punct=5

---

The store buys and sells cameras.

	1 The the DT O det=2
	2 store store NN O nsubj=3,nsubj=5
	3 buys buy VBZ O ROOT=0
	4 and and CC O cc=3
	5 sells sell VBZ O conj:and=3
	6 cameras camera NNS O dobj=3
	7 . . . O punct=3

---

She was reading or watching a movie.

	1 She she PRP O nsubj=3,nsubj=5
	2 was be VBD O aux=3
	3 reading read VBG O ROOT=0
	4 or or CC O cc=3
	5 watching watch VBG O conj:or=3
	6 a a DT O det=7
	7 movie movie NN O dobj=3
	8 . . . O punct=3

---

Sue wants to buy a hat.

	1 Sue sue VB O nsubj=2,nsubj:xsubj=4
	2 wants want VBZ O ROOT=0
	3 to to TO O mark=4
	4 buy buy VB O xcomp=2
	5 a a DT O det=6
	6 hat hat NN O dobj=4
	7 . . . O punct=2

---

Both of the girls are reading.

	1 Both both DT O det:qmod=4
	2 of of IN O mwe=1
	3 the the DT O det=4
	4 girls girl NNS O nsubj=6
	5 are be VBP O aux=6
	6 reading read VBG O ROOT=0
	7 . . . O punct=6

---

A bunch of people are coming.

	1 A a DT O det:qmod=4
	2 bunch bunch NN O mwe=1
	3 of of IN O mwe=1
	4 people people NNS O nsubj=6
	5 are be VBP O aux=6
	6 coming come VBG O ROOT=0
	7 . . . O punct=6

---

The house in front of the hill.

	1 The the DT O det=2
	2 house house NN O ROOT=0
	3 in in IN O case=7
	4 front front NN O mwe=3
	5 of of IN O mwe=3
	6 the the DT O det=7
	7 hill hill NN O nmod:in_front_of=2
	8 . . . O punct=2

---

I bike to work and I bike from work.

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

I bike to and from work.

	1 I I PRP O nsubj=2
	2 bike bike NN O ROOT=0,conj:and=2
	3 to to TO O case=6
	4 and and CC O cc=3
	5 from from IN O conj:and=3
	6 work work NN O nmod:to=2,nmod:from=2
	7 . . . O punct=2

---

She flew to Bali or to Turkey.

	1 She she PRP O nsubj=2,nsubj=2
	2 flew fly VBD O ROOT=0,conj:or=2
	3 to to TO O case=4
	4 Bali Bali NNP LOCATION nmod:to=2
	5 or or CC O cc=2
	6 to to TO O case=7
	7 Turkey Turkey NNP COUNTRY nmod:to=2
	8 . . . O punct=2

---

The boy who lived.

	1 The the DT O det=2
	2 boy boy NN O ROOT=0,nsubj=4
	3 who who WP O ref=2
	4 lived live VBD O acl:relcl=2
	5 . . . O punct=2

---

Everybody wants to buy a house.

	1 Everybody everybody NN O nsubj=2,nsubj:xsubj=4
	2 wants want VBZ O ROOT=0
	3 to to TO O mark=4
	4 buy buy VB O xcomp=2
	5 a a DT O det=6
	6 house house NN O dobj=4
	7 . . . O punct=2

---

Everybody wants that everybody buys a house.

	1 Everybody everybody NN O nsubj=2
	2 wants want VBZ O ROOT=0
	3 that that IN O mark=5
	4 everybody everybody NN O nsubj=5
	5 buys buy VBZ O ccomp=2
	6 a a DT O det=7
	7 house house NN O dobj=5
	8 . . . O punct=2

---

Everybody sleeps or is awake.

	1 Everybody everybody NN O compound=2
	2 sleeps sleep NNS O ROOT=0
	3 or or CC O cc=2
	4 is be VBZ O cop=5
	5 awake awake RB O conj:or=2
	6 . . . O punct=2

---

Everybody sleeps or everybody is awake.

	1 Everybody everybody NN O compound=2
	2 sleeps sleep NNS O nsubj=6
	3 or or CC O cc=2
	4 everybody everybody NN O conj:or=2,nsubj=6
	5 is be VBZ O cop=6
	6 awake awake RB O ROOT=0
	7 . . . O punct=6

---

Sue and Mary are carrying a piano.

	1 Sue sue VB O nsubj=5
	2 and and CC O cc=1
	3 Mary Mary NNP PERSON conj:and=1,nsubj=5
	4 are be VBP O aux=5
	5 carrying carry VBG O ROOT=0
	6 a a DT O det=7
	7 piano piano NN O dobj=5
	8 . . . O punct=5

---

The quick brown fox jumps over the lazy dog.

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

Silvio Berlusconi has met the Pope in Vatican City.

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

Sangla Valley in Himachal Pradesh in India.

	1 Sangla Sangla NNP LOCATION compound=2
	2 Valley Valley NNP CITY ROOT=0
	3 in in IN O case=5
	4 Himachal Himachal NNP LOCATION compound=5
	5 Pradesh Pradesh NNP LOCATION nmod:in=2
	6 in in IN O case=7
	7 India India NNP COUNTRY nmod:in=5
	8 . . . O punct=2

