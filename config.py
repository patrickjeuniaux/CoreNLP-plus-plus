"""
config.py
---------
Module containing a Config class used by factory.py.
Patrick Jeuniaux
University of Pisa
"""


import sys
import pprint

#######################################################################


import os

PROG_FOLDER = os.path.expanduser("~/Documents/repos/PPJMHJ/Config")

sys.path.append(PROG_FOLDER)

from config_reader import ConfigReader

#######################################################################


class Config(ConfigReader):

    """
    The class reads a configuration from file, and handles some basic parts of the execution of the script.
    """

    #######################################################################
    def __init__(self, cnf_file, char_width=36):

        super(Config, self).__init__(
            cnf_file, char_width)

        # ----------------
        # expected members
        # ----------------

        # members named in the cnf file:
        # ------------------------------

        # [IO]
        self.prog_folder = None
        self.data_folder = None
        self.start_folder = None
        self.ready_folder = None
        self.processed_folder = None
        self.ud_folder = None
        self.log_folder = None

        # [Safeguards]
        self.included = None
        self.excluded = None
        self.ask_ready = None
        self.existing_output_folder_blocks = None
        self.existing_output_file_blocks = None

        # [Management]
        # How to recognize a UD filename.
        # For instance:
        # File without extension:     ^([^.]+)$
        # Text file with extension      .txt : .*\.txt
        self.input_filename_regex = None

        # example : '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
        self.log_format = None

        # [UD_parsing]
        self.server_url = None
        self.use_server = None

        # how to delimit paragraph
        self.paragraph_delimiter = None

        # whether each paragraph is processed separately by CoreNLP
        self.parse_per_paragraph = None

        # whether the output of CoreNLP is tagged
        self.tag_parse = None

        # maximum number of character that can be sent to CoreNLP for processing
        self.max_text_char_length = None

        # if a text contains a line whose length in characters is larger than this length, skip the text
        self.skip_text_char_length = None

        # duration (in milliseconds) beyond which CoreNLP will issue a timeout error
        self.max_timeout = None

        self.move_input_to_processed = None
        self.multiprocessing_method = None

        # some useful constants
        # --------------------------

        self.mm_between = "between"
        self.mm_within = "within"

        self.char_width = char_width

        # a container of conversion functions
        # ------------------------------------

        self.str_conversion = {
            "prog_folder": self.complete_path,
            "data_folder": self.complete_path,
            "start_folder": self.complete_path,
            "ready_folder": self.complete_path,
            "processed_folder": self.complete_path,
            "ud_folder": self.complete_path,
            "log_folder": self.complete_path,
            "included": self.comma_separated_value_to_list,
            "excluded": self.comma_separated_value_to_list,
            "ask_ready": self.to_bool,
            "move_input_to_processed": self.to_bool,
            "use_server": self.to_bool,
            "existing_output_folder_blocks": self.to_bool,
            "existing_output_file_blocks": self.to_bool,
            "parse_per_paragraph": self.to_bool,
            "tag_parse": self.to_bool,
            "max_text_char_length": int,
            "skip_text_char_length": int,
            "max_timeout": int,
        }

        # ------------------------------

        self.start_reading_configuration()

        # ------------------------------

        # [IO]
        # ----

        self.set_attribute_list(['prog_folder',
                                 'data_folder',
                                 'start_folder',
                                 'ready_folder',
                                 'processed_folder',
                                 'ud_folder',
                                 'log_folder'])

        # I could not easily include log format in the configuration file so it is passed here as an argument
        self.set_attribute(attr="log_format", value=self.log_format)

        # [Safeguards]
        # ------------

        params = ['included', 'excluded']
        for param in params:
            self.set_attribute(attr=param, pretty="File(s) " + param)

        self.set_attribute_list(['ask_ready',
                                 'existing_output_folder_blocks',
                                 'existing_output_file_blocks'])

        # Check that calling script is authorized to run
        self.check_calling_script()

        # [Management]
        # ------------

        self.set_attribute_list([
            'log_format',
            'input_filename_regex',
        ])

        # [UD_parsing]
        # ------------

        pretty = "CoreNLP server URL"
        self.set_attribute(attr="server_url", pretty=pretty)

        self.set_attribute_list(['use_server',
                                 'paragraph_delimiter',
                                 'parse_per_paragraph',
                                 'tag_parse',
                                 'max_text_char_length',
                                 'skip_text_char_length',
                                 'max_timeout',
                                 'move_input_to_processed',
                                 'multiprocessing_method', ])

        #------------------

        self.finish_reading_configuration()



#######################################################################
if __name__ == "__main__":

    CONFIG = Config("config_test.cnf")

    # print CONFIG

    # print repr(CONFIG)
