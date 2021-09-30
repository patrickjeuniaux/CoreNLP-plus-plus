# -*- coding: utf-8 -*-

"""
preprocessor.py
---------------
Module that prepares the input to be used by factory.py.
Patrick Jeuniaux
University of Pisa


"""

#######################################################################

# external contributions

import sys
reload(sys)  # Python 2
sys.setdefaultencoding('utf8')

import os
# import shutil
# import codecs


import re

from time import time
from datetime import datetime

# to install:

from tqdm import tqdm as progress
from humanfriendly import format_timespan as ft
from humanfriendly import format_size as fs
from humanfriendly import format_number as fn


#######################################################################

# internal contributions

import config


#######################################################################
def init(config_file):

    global CONFIG
    global START_TIME

    # load the configuration
    try:
        CONFIG = config.Config(config_file)
    except Exception as e:
        print(e)
        print(" --- ABORT ---")
        sys.exit()

    msg = "\n\n" + timestamp() + " ---> START\n\n"

    print(msg)

    START_TIME = time()


#######################################################################

def clean_Wikipedia_dump():

    process_Wikipedia_extraction_folder(CONFIG.start_folder)


#######################################################################


def process_Wikipedia_extraction_folder(input_folder):

    # to keep track of corpus-level statistics (cs)

    cs = {'tna': 0,  # total nb articles
          'tnc': 0,  # total nb characters
          'tnb': 0,  # total nb bytes
          'la': "",  # largest article
          'mnc': 0,  # max nb characters
          'mnb': 0}  # max nb bytes

    output_folder = os.path.join(CONFIG.ready_folder)

    for root, dirs, files in os.walk(input_folder):

        # for file in files:
        for file in progress(files):

            # print file

            input_file = os.path.join(root, file)

            # print input_file

            output_sub = os.path.relpath(input_file, start=input_folder)
            output_subfolder = os.path.join(output_folder, output_sub)

            attend_output_folder(output_subfolder)

            # print input_file
            # print output_subfolder

            extractor = WikipediaExtractProcessor(
                input_file,
                output_subfolder)

            ds = extractor.extract()

            cs = update_corpus_statistics(cs, ds)

    display_stats(**cs)

#######################################################################


def update_corpus_statistics(cs, ds):
    """
    Updates corpus-level statistics (cs)
    using document-level statistics (ds).
    """

    cs['tna'] += ds['rna']
    cs['tnc'] += ds['rnc']
    cs['tnb'] += ds['rnb']

    if ds['mnc'] > cs['mnc']:
        cs['la'] = ds['la']

    cs['mnc'] = max(cs['mnc'], ds['mnc'])
    cs['mnb'] = max(cs['mnb'], ds['mnb'])

    return cs

#######################################################################


def attend_output_file(output_file):
    """
    Checks whether the output file exists
    and reacts accordingly.
    """
    if os.path.exists(output_file):

        if CONFIG.existing_output_file_blocks:

            sorry_cannot_overwrite(output_file, "file")


#######################################################################

def attend_output_folder(output_folder):
    """
    Checks whether the output folder exists
    and reacts accordingly.
    """

    if os.path.exists(output_folder):

        if CONFIG.existing_output_folder_blocks:

            sorry_cannot_overwrite(output_folder, "output")

    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


#######################################################################

def sorry_cannot_overwrite(path, path_type):
    """
    Informs the user that the folder or file
    cannot be overwritten, and stops the program.
    """

    print("\n\n---> ERROR !!!")
    print("\nThis " + path_type + " already exists and cannot be overwritten:")
    print("\n" + path)
    print("\nEither move this " + path_type + " to another location")
    print("\nor adapt your configuration file:")
    print("\n" + CONFIG.config_file)
    print("\n---> change this parameter: existing_output_" +
          path_type + "_blocks: no")
    print("\n--- ABORT ---")
    sys.exit()

#######################################################################


def timestamp():

    return '{:%Y-%m-%d %H:%M:%S}'.format(datetime.now())


#######################################################################
def display_stats(tna, tnc, tnb, la, mnc, mnb):

    print("\n\n" + timestamp() + " ---> END !\n\n")

    end_time = time()
    duration = end_time - START_TIME
    print("TOTAL duration of preprocessing : " + ft(duration))

    print("\nTOTAL number of articles : " + fn(tna))

    print("\nTOTAL number of characters in the corpus : " + fn(tnc))

    print("\nTOTAL size of the corpus : " + fs(tnb))

    print("\nLargest article : " + la)

    print("\n - Largest number of characters : " + fn(mnc))

    print("\n - Largest number of bytes : " + fs(mnb))

    print("\nEstimates for the total duration of UD parsing")
    print("----------------------------------------------")

    duration = tnb * (1 / 400)
    print("\n 400 b/s, one processor: " + ft(duration))

    duration = tnb * (1 / 700)
    print("\n 700 b/s, one processor: " + ft(duration))

    duration = tnb * (1 / (400 * 16))
    print("\n 400 b/s, 16 processors: " + ft(duration))

    duration = tnb * (1 / (700 * 8))
    print("\n 700 b/s, 8 processors: " + ft(duration))

    print("\n")


#######################################################################

def make_specific_sample_file(input_file, output_file, start_line):

    doc_end = r'</text>'

    print "--- START ---"

    with open(input_file, "r") as reader:

        writing = False

        with open(output_file, "w") as writer:

            for line in reader:

                if line:

                    content = line.strip()

                    if content == start_line:

                        print "--- START : DOC ---"

                        print line

                        writing = True

                    elif writing:

                        if content == doc_end:

                            print "--- END : DOC ---"

                            break

                        else:

                            writer.write(line)

    print "--- END ---"


#######################################################################


def make_sample_files_from_simple_folder(input_folder, output_folder, max_number_line=10000):

    filenames = sorted(os.listdir(input_folder))

    for filename in progress(filenames):

        input_file = os.path.join(input_folder, filename)

        if os.path.isfile(input_file):

            attend_output_folder(output_folder)

            make_sample_file(input_file, output_folder,
                             max_number_line)


#######################################################################

def make_sample_file(input_file, output_folder, max_number_line=10000):

    # with codecs.open(input_file, "rb", encoding="utf-8") as reader:
    with open(input_file, "r") as reader:

        filename = os.path.basename(input_file)

        output_file = os.path.join(output_folder, filename)

        # with codecs.open(output_file, "w", encoding=out_encoding) as writer:
        with open(output_file, "w") as writer:

            i = 0

            for line in reader:

                i += 1

                if i > max_number_line:
                    break

                if line:

                    line = to_utf8(line)

                    writer.write(line)


#######################################################################
def to_utf8(string):

    # https://docs.python.org/2/library/codecs.html#standard-encodings
    # https://docs.python.org/3/library/codecs.html#standard-encodings

    try:
        # UTF-8
        string = string.decode("utf-8")
    except:
        try:
            # Western Europe (cp1252)
            string = string.decode("windows-1252")
        except:
            try:
                # West Europe (latin_1)
                string = string.decode("iso-8859-1")
            except:
                pass

    string = string.encode("utf-8")

    return string


#######################################################################

def extract_plain_text_from_parse():
    """
    This function launches the plain text extraction of a linguistic parse.
    The goal is to recreate the original text that was used,
    putting each sentence on a separate line.

    The format of the parse is the one used by Gianluca Lebani
    when, apparently around 2013, he parsed the following corpora:
    - BNC
    - ukWac
    - Wikipedia

    Example of the parse:

    <text id="bnc:1">
    <s>
    FACTSHEET   factsheet   NN  1   5   DEP
    WHAT    what    WP  2   3   SBJ
    IS  be  VBZ 3   1   NMOD
    AIDS    AIDS    NP  4   0   ROOT
    ?   ?   SENT    5   0   ROOT
    </s>

    These lines are at the beginning of the parse for the BNC.

    The plain text extraction will retrieve the sentence:

    FACTSHEET WHAT IS AIDS ?

    """

    extract_plain_text_from_parse_folder(CONFIG.start_folder)


#######################################################################

def extract_plain_text_from_parse_folder(input_folder):

    # to keep track of corpus-level statistics (cs)

    cs = {'tna': 0,  # total nb articles
          'tnc': 0,  # total nb characters
          'tnb': 0,  # total nb bytes
          'la': "",  # largest article
          'mnc': 0,  # max nb characters
          'mnb': 0}  # max nb bytes

    filenames = sorted(os.listdir(input_folder))

    output_folder = CONFIG.ready_folder
    attend_output_folder(output_folder)

    for filename in progress(filenames):

        if not filename.endswith(".xml"):
            # if not filename.endswith("bnc.xml"):  # TEMP
            continue

        print("\n --> " + filename)

        input_file = os.path.join(input_folder, filename)

        sub_folder = strip_extension(filename)
        output_folder = os.path.join(CONFIG.ready_folder, sub_folder)

        attend_output_folder(output_folder)

        extractor = PlainTextParseExtractor(input_file, output_folder)
        ds = extractor.extract()

        cs = update_corpus_statistics(cs, ds)

    display_stats(**cs)


#######################################################################


def strip_extension(string):

    return os.path.splitext(string)[0]

#######################################################################


class CorpusReader(object):

    """
    CorpusReader
    This parent class is meant to be implemented by a child class.
    """

    def __init__(self, input_file, output_folder):

        self.input_file = input_file
        self.output_folder = output_folder

        self.writer = None
        self.docid = None
        self.title = None

        # to keep track of document-level statistics (ds)

        self.rna = 0  # running number articles
        self.nc = 0  # number characters in a document
        self.rnc = 0  # running number characters
        self.rnb = 0  # running number bytes
        self.la = ""  # largest article
        self.nb = 0  # number of bytes in a document
        self.mnc = 0  # max number characters
        self.mnb = 0  # max number bytes

        # within each folder, we save an index about the articles
        index_file = os.path.join(self.output_folder, "index.txt")

        attend_output_file(index_file)

        self.index = open(index_file, "w")
        #out_encoding = CONFIG.preproc_output_codec
        #self.index = codecs.open(index_file, "w", encoding=out_encoding)

        self.index.write("docid\ttitle")

        self.reader = open(self.input_file, "r")

        # print self.reader.read()

        # in_encoding = CONFIG.preproc_input_codec
        # self.reader = codecs.open(self.input_file, "r", encoding=in_encoding)

    def extract(self):

        # execute the operations by iterating over the object
        for _ in self:
            pass

        # for line in self:
        #     print(line)

        ds = {
            'rna': self.rna,
            'rnc': self.rnc,
            'rnb': self.rnb,
            'la': self.la,
            'mnc': self.mnc,
            'mnb': self.mnb,
        }

        return ds

    def __iter__(self):

        return self

    def next(self):

        return self.__next__()

    def __next__(self):

        # process_line is defined by the child class
        return self.process_line()

    ####################
    def close_doc(self):
        """
        Closes the current document by:
        - writing to the index its docid and title
        - closing the output writer for this document
        - updating and returning document-level statistics (ds)
        """

        # close the current document
        self.writer.close()

        # get the path to the output
        output_file = self.writer.name

        # write down its docid and title in the index
        index_line = "\n" + self.docid + "\t" + self.title

        self.index.write(index_line)

        # collect some stats about it
        # and update the running sums

        # articles
        #---------
        self.rna += 1

        # characters
        #-----------
        self.rnc += self.nc

        if self.nc > self.mnc:
            self.la = output_file

        self.mnc = max(self.mnc, self.nc)

        # reinitialization
        self.nc = 0

        # bytes
        #------
        # depending on the encoding, nb and nc are the same

        self.nb = os.path.getsize(output_file)

        self.rnb += self.nb

        self.mnb = max(self.mnb, self.nb)


#######################################################################
class PlainTextParseExtractor(CorpusReader):
    """
    Class to extract Plain Text from an old UD parse.

    Processing of the input file,
    considering all the documents within it.


    """

    def __init__(self, input_file, output_folder):

        super(PlainTextParseExtractor, self).__init__(
            input_file, output_folder)

        self.doc_start = r'<text id="(.*?)">'
        self.end_sentence = r'</s>'
        self.data_line = r'(.*?)(\t.*?){5}'
        self.sentence = ""

    def process_line(self):

        line = self.reader.readline()

        # if len(line) > 0:
        if line:

            line = to_utf8(line)

            result_doc_start = re.match(self.doc_start, line)

            if result_doc_start:

                # we have encountered a new file

                if self.writer is not None:
                    # The writer was therefore opened.
                    # We were processing a document.
                    # We need to close it.
                    self.close_doc()

                self.docid = str(self.rna + 1)

                self.title = result_doc_start.group(1)

                # for each new document, we'll save a file
                output_file = os.path.join(self.output_folder, self.docid)

                attend_output_file(output_file)

                self.writer = open(output_file, "w")

                # self.writer = codecs.open(
                #     output_file, "w", encoding=CONFIG.preproc_output_codec)

                self.sentence = ""

            elif re.match(self.end_sentence, line):

                # We separate sentences by a double newline.
                # This way, it will be easy to consider them as 'paragraph' by factory module.
                self.sentence += "\n\n"

                self.nc += 1
                self.writer.write(self.sentence)
                self.sentence = ""
            else:
                result_data_line = re.match(self.data_line, line)

                if result_data_line:

                    word = result_data_line.group(1)

                    self.sentence += word + " "
                    self.nc += len(word) + 1

            return line

        else:

            if self.writer is not None:
                # we are at the end of the input file.
                # close the last document
                self.close_doc()

            raise StopIteration


#######################################################################
class WikipediaExtractProcessor(CorpusReader):
    """
    Class to process the Clean Wikipedia Dump.

    Processing of the input file,
    considering all the documents within it.
    """

    def __init__(self, input_file, output_folder):

        super(WikipediaExtractProcessor, self).__init__(
            input_file, output_folder)

        self.doc_start = r'<doc id="(\d+\d*)" url="(.*?)" title="(.*?)">'
        self.XML_tag = r'<[^>]+>'

    def process_line(self):

        line = self.reader.readline()

        # if len(line) > 0:
        if line:

            line = to_utf8(line)

            result_doc_start = re.match(self.doc_start, line)

            if result_doc_start:

                # we have encountered a new file

                if self.writer is not None:
                    # The writer was therefore opened.
                    # We were processing a document.
                    # We need to close it.
                    self.close_doc()

                self.docid = result_doc_start.group(1)
                # self.url = result_doc_start.group(2)
                self.title = result_doc_start.group(3)

                # for each new document, we'll save a file
                output_file = os.path.join(self.output_folder, self.docid)

                attend_output_file(output_file)

                self.writer = open(output_file, "w")
                # self.writer = codecs.open(output_file, "w",encoding=CONFIG.preproc_output_codec)

            # Remove XML tags
            line = re.sub(self.XML_tag, "", line)
            self.writer.write(line)

            self.nc += len(line)

            return line

        else:

            if self.writer is not None:
                # we are at the end of the input file.
                # close the last document
                self.close_doc()

            raise StopIteration
