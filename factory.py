# -*- coding: utf-8 -*-

"""
factory.py
----------
Most general module responsible for handling I/O and parser.py.
Patrick Jeuniaux
University of Pisa
"""

#######################################################################

# external contributions

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import datetime
import re
import shutil
# import tqdm
import time
import traceback
import multiprocessing
from multiprocessing import Process
from multiprocessing.pool import Pool as PoolParent
import logging

# to install:
import multiprocessing_logging

from humanfriendly import format_timespan as ft
from humanfriendly import format_size as fs
from humanfriendly import format_number as fn

#######################################################################

# internal contributions

import parser
import config


#######################################################################
def init(config_file):

    global CONFIG
    global DEP_PARSER
    global POOL
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

    START_TIME = time.time()

    if os.path.isfile(CONFIG.log_file):
        os.remove(CONFIG.log_file)

    logging.basicConfig(format=CONFIG.log_format, filename=CONFIG.log_file,
                        filemode='a', level=logging.INFO)

    multiprocessing_logging.install_mp_handler()

    if CONFIG.use_server:

        DEP_PARSER = parser.Client(url=CONFIG.server_url)


#######################################################################
def run():

    if CONFIG.multiprocessing_method == CONFIG.mm_between:

        #POOL = multiprocessing.Pool(processes=8)
        POOL = multiprocessing.Pool()

        POOL.imap(handle_file, file_generator(), chunksize=1000)

        POOL.close()
        POOL.join()

    elif CONFIG.multiprocessing_method == CONFIG.mm_within:

        for file in file_generator():
            handle_file(file)

    finish()


#######################################################################
def file_generator():

    input_folder = CONFIG.ready_folder

    if CONFIG.input_filename_regex == "" or CONFIG.input_filename_regex is None:

        return (os.path.join(root, file) for root, dirs, files in os.walk(input_folder) for file in files)

    else:

        import re

        # ^([^.]+)$ for files without extension
        # .*\.txt for files with .txt

        return (os.path.join(root, file) for root, dirs, files in os.walk(input_folder) for file in files if re.match(CONFIG.input_filename_regex, file))

    # return (os.path.join(root, file) for root, dirs, files in os.walk(input_folder) for file in files if not file.endswith(".txt"))

    # return (os.path.join(root, file) for root, dirs, files in os.walk(input_folder) for file in files if file == "307")

    # 332 307

#######################################################################


def process_file(input_file, output_file):

    with open(input_file, 'r') as reader:

        with open(output_file, 'w') as writer:

            if not CONFIG.use_server:
                msg = "\n --- debugging mode ---\n\n Running script with configuration: \n\n  use_server = False \n\n --- \n\n "
                writer.write(msg)

            text = reader.read()

            if CONFIG.multiprocessing_method == CONFIG.mm_within:

                process_text_within_method(text, writer)

            elif CONFIG.multiprocessing_method == CONFIG.mm_between:

                process_text_between_method(text, writer)

            # This section is normally never reached
            else:
                writer.write(text)


#######################################################################
def process_text_between_method(text, writer):

    paragraphs = paragraphs_splitter(text)

    if CONFIG.skip_text_char_length > 0:
        assess_paragraphs_lengths(paragraphs, CONFIG.skip_text_char_length)

    if CONFIG.parse_per_paragraph:
        parts = paragraphs
    else:
        parts = char_splice_gen(CONFIG.max_text_char_length, paragraphs)

    for idx, part in enumerate(parts):

        if CONFIG.use_server:

            result = parse_to_str(part)

        else:

            result = debug_mode_str(part)

        if CONFIG.tag_parse:
            writer.write('\n<p id="' + str(idx) + '">\n\n')

        writer.write(result)

        if CONFIG.tag_parse:
            writer.write('</p>\n')


#######################################################################
def process_text_within_method(text, writer):

    paragraphs = paragraphs_splitter(text)

    if CONFIG.skip_text_char_length > 0:
        assess_paragraphs_lengths(paragraphs, CONFIG.skip_text_char_length)

    if CONFIG.parse_per_paragraph:
        parts = paragraphs
    else:
        parts = char_splice_gen(CONFIG.max_text_char_length, paragraphs)

    POOL = multiprocessing.Pool()

    if CONFIG.use_server:

        parse_func = parse_to_str

    else:
        parse_func = debug_mode_str

    results = POOL.imap(parse_func, parts, chunksize=1000)

    POOL.close()

    POOL.join()

    for idx, result in enumerate(results):

        if CONFIG.tag_parse:
            writer.write('<p id = "' + str(idx) + '">')

        writer.write(result)

        if CONFIG.tag_parse:
            writer.write('< /p >')


#######################################################################
def parse_to_str(text):
    """
    Call the CoreNLP parser and turn the results (that are provided by a generator) into a string.
    """

    # This might be suboptimal because it is the same for all texts in the corpus.
    # For instance, this could vary in function of the size of the texts...
    timeout = CONFIG.max_timeout
    max_text_char_length = CONFIG.max_text_char_length

    results = DEP_PARSER.parse_text_rich(text,
                                         timeout=timeout,
                                         max_text_char_length=max_text_char_length)

    my_str = ""

    for sentence in results:

        for word in sentence:

            my_str += word + "\n"

        my_str += "\n"

    return my_str


#######################################################################
def debug_mode_str(text):
    return "\n\ndebugging : text --> " + text


#######################################################################
# https://stackoverflow.com/questions/14679836/splitting-up-a-python-list-in-chunks-based-on-length-of-items
def char_splice_gen(max_chars, string_list):
    """
    Return a string of slices delimited by new lines based on maxchars string-length boundary.
    """

    nb_new_lines = 2

    new_lines = "\n" * nb_new_lines

    running_count = 0  # start at 0
    tmp_slice = ""  # tmp list where we append string
    for item in string_list:
        running_count += nb_new_lines + len(item)
        if running_count <= max_chars:

            tmp_slice += new_lines + item
        else:
            yield tmp_slice
            tmp_slice = item
            running_count = nb_new_lines + len(item)
    yield(tmp_slice)


#######################################################################
def paragraphs_splitter(text):

    if CONFIG.paragraph_delimiter == '' or CONFIG.paragraph_delimiter is None:
        parag_regex = '\s{2,}'
    else:
        parag_regex = CONFIG.paragraph_delimiter

    #paragraphs = re.split(parag_regex, text)

    paragraphs = [paragraph for paragraph in re.split(
        parag_regex, text) if paragraph.strip() != '']

    return paragraphs


#######################################################################
def assess_paragraphs_lengths(paragraphs, max_size):

    for _, paragraph in enumerate(paragraphs):

        size = len(paragraph)

        if size > max_size:

            raise LineTooLongException(size, max_size)


#######################################################################
class LineTooLongException(Exception):
    def __init__(self, size, max_size):
        self.size = str(size)
        self.max_size = str(max_size)

    def msg(self):

        msg = "LineTooLongException - the line of a text is too long" + "\n" + \
            "The file is skipped because of a line of size " + \
            self.size + " ( > max " + self.max_size + ")."

        return msg

    def __str__(self):

        return self.msg()


#######################################################################
def timestamp():

    return '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

#######################################################################


def handle_file(input_file):

    try:

        start_time = time.time()

        process_name = multiprocessing.current_process().name

        input_filename = os.path.basename(input_file)

        subpath = os.path.relpath(input_file, start=CONFIG.ready_folder)

        output_file = os.path.join(CONFIG.ud_folder, subpath)
        output_folder = os.path.dirname(output_file)
        attend_output_folder(output_folder)

        if CONFIG.move_input_to_processed:
            processed_file = os.path.join(CONFIG.processed_folder, subpath)
            processed_folder = os.path.dirname(processed_file)
            attend_output_folder(processed_folder)

        # print(timestamp() + " --- " + process_name +
        #       " -> " + input_filename + " : " + input_file)

        # Process file
        process_file(input_file, output_file)

        treated_file = input_file

        if CONFIG.move_input_to_processed:
            # Move the input file to the 'processed' folder.
            shutil.copy(input_file, processed_file)

            os.remove(input_file)

            treated_file = processed_file

        end_time = time.time()

        # duration in seconds
        duration = end_time - start_time

        # size in bytes
        size = os.path.getsize(treated_file)

        # rate in bytes per seconds
        if duration > 0:
            rate = size / duration
        else:
            rate = "NA"

        msg = timestamp() + ", " + process_name + \
            " --> " + treated_file + \
            " (" + fs(size) + ", " + ft(duration) + ", " + fn(rate) + " b/s)"

        print(msg)

    except Exception as exception:
        log_exception(exception, input_file)


#######################################################################
def attend_output_folder(output_folder):

     # If do not exist, create folders recursively
    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except Exception:
            # It has been created in the meantime by another process.
            # It therefore generates an exception.
            # Not a big deal.
            pass

#######################################################################


def log_exception(exception, input_file):

    # print(exception)
    exception_type = type(exception).__name__

    if exception_type == "LineTooLongException":

        msg = "\n\n" + exception_type + " : " + input_file + "\n" + exception.msg()

    else:

        process_name = multiprocessing.current_process().name
        my_type, value, traces = sys.exc_info()
        lines = traceback.format_exception(my_type, value, traces)

        i = 0
        my_str = ""
        for line in lines:
            # my_str += "\n" + "\t" * i + " --> " + line.strip()
            my_str += "\n" + " " + str(i) + " --> " + line.strip()
            i += 1

        msg = "\n\n" + process_name + " ::: " + \
            exception_type + " : " + input_file + my_str

    #-----------------------------

    print(msg)
    logging.info(msg)

    #-----------------------------

    if exception_type == "ConnectionError":
        print(" --- ABORT ---")

        global POOL
        POOL.terminate()
        POOL.close()
        POOL.join()

        finish()


#######################################################################
def finish():

    msg = "\n\n" + timestamp() + " ---> END !\n\n"

    print(msg)
    # logging.info(msg)

    end_time = time.time()

    duration = end_time - START_TIME

    msg = "TOTAL duration : " + ft(duration)

    print(msg)
    # logging.info(msg)

#######################################################################


def clean_input_folder():

    input_folder = CONFIG.ready_folder

    remove_empty_folders(input_folder, False)


#######################################################################

# https://www.jacobtomlinson.co.uk/2014/02/16/python-script-recursively-remove-empty-folders-directories/


def remove_empty_folders(root_path, remove_root=True):

    # If this is not a directory
    # Leave
    if not os.path.isdir(root_path):
        return

    # This is a directory
    # List the names of its objects
    objs = os.listdir(root_path)
    for obj in objs:

        path = os.path.join(root_path, obj)

        # If this is a directory, try to remove it
        if os.path.isdir(path):
            remove_empty_folders(path)

    # List the content of the directory again
    objs = os.listdir(root_path)

    # Remove it if it is empty and we can remove it
    if len(objs) == 0 and remove_root:
        os.rmdir(root_path)
        print "Remove: " + root_path
