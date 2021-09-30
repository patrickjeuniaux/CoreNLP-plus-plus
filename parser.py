# -*- coding: utf-8 -*-

"""
parser.py
---------
Module containing a Client class that wraps the client from nltk.parse.
Patrick Jeuniaux
University of Pisa
"""


import sys
# TEMP
# reload(sys)
# sys.setdefaultencoding("utf-8")


import json
# import requests

from collections import *


# to install:
#from nltk.parse.corenlp import *
import nltk


#################################################


class Client(nltk.parse.corenlp.CoreNLPDependencyParser):

    """Adaptation of elements of nltk.parse"""

    # http://www.nltk.org/_modules/nltk/parse/corenlp.html
    # http://www.nltk.org/_modules/nltk/parse/dependencygraph.html

    """The goal is to be able to output the same kind of data present in the DepCC corpus:

    Each line of depcc is composed of 10 columns, as follows::
    0) ID = word index
    1) FORM = word form
    2) LEMMA = lemma or stem of word form
    3) UPOSTAG = universal part-of-speech tag
    4) XPOSTAG = language-specific part-of-speech tag
    5) FEATS = list of morphological features
    6) HEAD = head of the current word, which is either a value of ID or zero
    7) DEPREL = universal dependency relation to the 'HEAD'
    8) DEPS = enhanced dependency graph in the form of head-deprel pairs
    9) NER = named entity tag"""

    # Overwrites methods of GenericCoreNLPParser.

    #################################################
    def api_call(self, data, properties=None, timeout=300000, max_text_char_length=50000):
        default_properties = {
            'outputFormat': 'json',
            'annotators': 'tokenize,ssplit,pos,lemma,ner,depparse',
            'ssplit.newlineIsSentenceBreak': 'always',
            "tokenize.options": "normalizeCurrency=false,invertible=true",
            'timeout': timeout,
            'maxCharLength': max_text_char_length,
        }

        # print default_properties

        if properties is None:
            used_properties = default_properties
        else:
            used_properties = properties

        # default_properties.update(properties or {})

        #data.encode(self.encoding)
        #data.decode("utf-8", errors='ignore').encode(self.encoding)
        #data.decode("utf-8", errors='replace').encode(self.encoding)
        #data.decode("ISO-8859-1").encode(self.encoding)
        #data.decode(self.encoding, errors='ignore').encode(self.encoding)

        response = self.session.post(
            self.url,
            params={
                'properties': json.dumps(used_properties),
            },
            data=data,
            timeout=timeout,
        )

        response.raise_for_status()

        return response.json()

    #################################################
    # Overwrites methods of CoreNLPDependencyParser.
    # WE DO NOT CARE ABOUT THIS ANYMORE
    def parse_text(self, text, *args, **kwargs):
        """Parse a piece of text.

        The text might contain several sentences which will be split by CoreNLP."""

        parsed_data = self.api_call(text, *args, **kwargs)

        # print "\n\n\n === Oh my God === \n\n\n"

        # import pprint
        # pprint.pprint(parsed_data)

        for parsed_sentence in parsed_data['sentences']:

            yield self.make_tree(parsed_sentence)

    #################################################
    # WE DO NOT CARE ABOUT THIS ANYMORE
    def make_tree(self, parsed_sentence):

        restructured_data = (' '.join(n_items[1:])
                             for n_items in sorted(self.transform(parsed_sentence)))

        return nltk.parse.dependencygraph.DependencyGraph(restructured_data, cell_separator=' ',)

    #################################################
    # WE DO NOT CARE ABOUT THIS ANYMORE
    def transform(self, parsed_sentence):

        # print sentence.keys()

        for dependency in parsed_sentence['basicDependencies']:

            dependent_index = dependency['dependent']
            token = parsed_sentence['tokens'][dependent_index - 1]

            # Return values that we don't know as '_'. Also, consider tag and ctag
            # to be equal.
            yield (
                dependent_index,
                '_',
                token['word'],
                token['lemma'],
                token['pos'],
                token['pos'],
                '_',
                str(dependency['governor']),
                dependency['dep'],
                '_',
                token['ner'],
            )

    #################################################
    # FOR DEBUGGING PURPOSES
    def parse_text_raw(self, text, *args, **kwargs):

        #text = text.decode('unicode_escape').encode('utf-8')
        #text = unicode(text, errors='ignore')
        text = unicode(text, errors='replace')

        parsed_data = self.api_call(text, *args, **kwargs)

        # print(parsed_data)

        return "Number of returned parsed sentences = " + str(len(parsed_data))

    #################################################
    # FOR DEBUGGING PURPOSES
    def parsed_sentence_inspection(self, parsed_sentence):

        import pprint

        print("")
        print ("-----=====-----\n" * 3)
        sentence = " ".join([word['originalText']
                             for word in parsed_sentence['tokens']])
        print(sentence)
        print ("\n\n")

        BASIC_DEP = sorted(
            parsed_sentence['basicDependencies'], key=lambda x: x['dependent'])

        ENHANCED_DEP = sorted(
            parsed_sentence['enhancedDependencies'], key=lambda x: x['dependent'])

        ENHANCED_DEP_PLUS = sorted(
            parsed_sentence['enhancedPlusPlusDependencies'], key=lambda x: x['dependent'])

        #ENHANCED_DEP = sorted(parsed_sentence['enhancedPlusPlusDependencies'], key=lambda x: x['dependent'])

        print ("\nBasic UD:\n---------\n")
        print ("\n".join([self.pretty_relation(X) for X in BASIC_DEP]))

        print ("\nEnhanced UD:\n------------\n")
        print ("\n".join([self.pretty_relation(X) for X in ENHANCED_DEP]))

        print ("\nEnhanced ++ UD:\n---------------\n")
        print ("\n".join([self.pretty_relation(X) for X in ENHANCED_DEP_PLUS]))

        print ("\n\n\n\n-----=====-----\n\n")
        pprint.pprint(parsed_sentence)

        print ("\n\n\n\n-----=====-----\n\n")

    #################################################
    # FOR DEBUGGING PURPOSES
    def pretty_relation(self, relation):

        head = relation['governorGloss'] + "-" + str(relation['governor'])

        link = " <=" + relation['dep'] + "= "

        dependent = relation['dependentGloss'] + \
            "-" + str(relation['dependent'])

        pretty_relation = dependent + link + head

        return pretty_relation

    #################################################
    # DEBUGGING

    def parse_text_rich2(self, text, *args, **kwargs):

        TEMP = text.split(" ")
        yield TEMP

    #################################################
    # FINAL
    def parse_text_rich(self, text, *args, **kwargs):
        """Parse a piece of text thanks to CoreNLP and returns a rich but concise representation close to the CONLL-U format.
        # http://universaldependencies.org/format.html"""

        # print "\n\n ===> \n" + text

        parsed_data = self.api_call(text, *args, **kwargs)

        for parsed_sentence in parsed_data['sentences']:

            # self.parsed_sentence_inspection(parsed_sentence)

            rich_representation = ('\t'.join(((str(item) for item in n_items)))
                                   for n_items in sorted(self.make_rich_representation(parsed_sentence)))

            yield rich_representation

    #################################################
    # FINAL
    def parse_text_rich_string(self, text, *args, **kwargs):

        SENTENCES = self.parse_text_rich(text, *args, **kwargs)

        RICH_STRING = ""

        for SENTENCE in SENTENCES:

            RICH_STRING += "\n".join(SENTENCE) + "\n"

        return RICH_STRING

    #################################################
    # FINAL
    def make_rich_representation(self, parsed_sentence):

        # This function returns a variant of the CoNLL-U format using the enhanced ++ universal dependencies
        # Schuster, S., & Manning, C. D. (2016). Enhanced English Universal Dependencies: An Improved Representation for Natural Language Understanding Tasks. In Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC 2016) (pp. 2371–2378). http://nlp.stanford.edu/~sebschu/pubs/schuster-manning-lrec2016.pdf

        # 1) collect the dependencies per dependent/child/token

        RICH = defaultdict(list)

        for DEPENDENCY in parsed_sentence['enhancedPlusPlusDependencies']:

            HEAD = DEPENDENCY["governor"]
            CHILD = DEPENDENCY["dependent"]
            DEP = DEPENDENCY["dep"]

            RICH[CHILD].append((DEP, HEAD))

        #import pprint
        # pprint.pprint(RICH)

        # 2) yield the information per dependent/child/token

        for TOKEN in parsed_sentence['tokens']:

            CHILD = TOKEN['index']

            RICH_DEP = ",". join([str(DEP) + "=" + str(HEAD)
                                  for DEP, HEAD in RICH[CHILD]])

            yield (
                CHILD,
                TOKEN['word'],
                TOKEN['lemma'],
                TOKEN['pos'],
                TOKEN['ner'],
                RICH_DEP,
            )
