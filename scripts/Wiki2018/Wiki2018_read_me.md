# Wikipedia 2018 UD-parsed corpus


## This document

This document is the 'read me' file for the Wikipedia 2018 UD-parse corpus.



## Author of the document

Patrick Jeuniaux
University of Pisa
2019-01-03





## This corpus

This 63 GB corpus contains about 5 million (5,574,817) Wikipedia articles (and about 2 billion words) that have been analyzed with CoreNLP.


The analysis covers:

- index
- word
- lemma
- POS
- named entity 
- UD dependencies 


Because we were especially interested by UD dependencies, we call this corpus a 'UD-parsed corpus'.







## Files structure

/extra/corpora/corpora-en/Wiki20180203/

/extra/corpora/corpora-en/Wiki20180203/Wiki2018_read_me.txt

/extra/corpora/corpora-en/Wiki20180203/Wiki20180203_plain_text.tar.gz
/extra/corpora/corpora-en/Wiki20180203/Wiki20180203_UDs.tar.gz


/extra/corpora/corpora-en/Wiki20180203/UDs/

/extra/corpora/corpora-en/Wiki20180203/UDs/AA/

/extra/corpora/corpora-en/Wiki20180203/UDs/AA/wiki_00/
/extra/corpora/corpora-en/Wiki20180203/UDs/AA/wiki_01/
/extra/corpora/corpora-en/Wiki20180203/UDs/AA/wiki_02/
...
/extra/corpora/corpora-en/Wiki20180203/UDs/AA/wiki_99/

/extra/corpora/corpora-en/Wiki20180203/UDs/AB/
/extra/corpora/corpora-en/Wiki20180203/UDs/AC/
...
/extra/corpora/corpora-en/Wiki20180203/UDs/ER/





## Methodology : procedure



### 1. Download the Wikipedia English dump


https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2

Date of the file: 2018-02-03
Size of the file: 14.7 GB


### 2. Install the necessary software


WikiExtractor.py

virtualenv

pip install tqdm, humanfriendly, multiprocessing_logging, configparser



### 3. Process the compressed file with 'Wiki extractor'

Input: enwiki-latest-pages-articles.xml.bz2

Script: WikiExtractor.py
Source: https://github.com/attardi/wikiextractor


We extracted 122 folders (AA, AB, AC ... ER) usually containing 100 text files (wiki_00, wiki_01, wiki_02 ... wiki_99) of about 1 MB each.

Number of folders produced: 122
Number of files produced: 12196
Size of the output: 12.7 GB








### 4. Prepare the files for CoreNLP

Script: 1_split_per_text.py
Source: homemade / TO DO: make it available

Each file produced by WikiExtractor.py contains several Wikipedia articles separated with an XML tag indicating its 'docid'.

We separated the articles in distinct files with the docid as a filename. XML tags were also removed from the files.

These articles are distributed in the 122 folders (following the same logic as above), and within these 122 folders, subfolders (wiki_00, wiki_01, wiki_02 ... wiki_99).

Number of folders and subfolders: 12,196
Number of files produced: 5,574,817 (about 5.5 millions)
Number of items: 5,574,817 files + 12,196 folders = 5,562,621 items
Size of the output: 12.29 GB

Note: these files are available on the server in the following 5 GB archive:

/extra/corpora/corpora-en/Wiki20180203/Wiki20180203_plain_text.tar.gz




### 5. Parse the files with CoreNLP

CoreNLP was downloaded and installed on the CoLingLab server
Source: https://stanfordnlp.github.io/CoreNLP/
Version: 2018-01-13


The CoreNLP server was used:

```
export CORENLP="/home/$USER/CoreNLP/2018-01-31/*"

java -cp "$CORENLP" -mx4g edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 600000
```


A Python script invoking NLTK functions was used as a client to feed the CoreNLP server with input and treat its output.

Script: 2_UD_parsing.py
Source: homemade / TO DO: make it available

Duration of processing: about 10 days
Size of the output: 63 GB
Number of words: 2,285,051,074
Number of items: 5,562,621 items


The corpus is located here:

/extra/corpora/corpora-en/Wiki20180203/UDs

It follows the same folder structure as the one described above.


Note: these files are also available on the server in the following 15.8 GB archive:

/extra/corpora/corpora-en/Wiki20180203/Wiki20180203_UDs.tar.gz




## Methodology : output format

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







## Methodology : output examples

See UD++CoreNLP.md










