"""
config_reader.py
---------
Class which facilitates the reading of a configuration file.

It is meant to be implemented with details
particular to a specific configuration file.

Patrick Jeuniaux
University of Pisa
"""


import os
import sys
import pprint

# print script_caller
# print os.path.dirname(sys.argv[0])

# to install:
import configparser


class ConfigReader(object):

    """
    This class needs to be implemented by a child.
    It reads a configuration from file
    It handles some basic parts of the execution of the script.
    """

    #######################################################################
    def __init__(self, cnf_file, char_width=36):
        """
        Initializes a map to store parameters.

        Parameters:
        -----------
        cnf_file: string
            The path of the file to open and read.

            The file should be a standard configuration file accepted by ConfigParser class. It consists of sections, led by a [section] header (ignored by this class) and followed by name: value entries (name= value) is also accepted.

            Read more at
            https://docs.python.org/2/library/configparser.html
        """

        # ----------------
        # minimal members
        # ----------------

        self.cnf_file = cnf_file
        self.config_file = None
        self.config_parser = None
        self.config_data = None

        self.calling_script = None

        self.log_folder = None
        self.log_file = None
        self.log_format = None

        self.char_width = char_width

        self.ask_ready = True

        # a container of conversion functions
        # ------------------------------------

        self.str_conversion = {}

    #######################################################################
    def read(self):

        print "\n---------------------------------------"
        print "The __init__ method needs to be implemented"
        print "-------------------------------------------\n"

        self.start_reading_configuration()

        print "\n--------------------------------------"
        print "The read method needs to be implemented"
        print "---------------------------------------\n"

        self.finish_reading_configuration()

    #######################################################################
    def start_reading_configuration(self):

        # ------------------------------

        print("\n--- START reading configuration ---\n")

        # Load configuration parameters.
        #------------------------------------

        # Get the absolute path of the script that calls.
        calling_script = os.path.realpath(sys.argv[0])
        self.set_attribute(attr="calling_script", value=calling_script)

        # Determine the config path
        # check whether the path to the configuration is absolute
        if os.path.isabs(self.cnf_file):

            config_file = self.cnf_file

        else:
            # the configuration file is assumed to be in the same folder as the script calling the config module

            if os.path.isfile(self.calling_script):
                # if what is calling is a file

                # we assume that the configuration file is in the same folder
                # as the calling script

                script_folder = os.path.dirname(self.calling_script)

                config_file = os.path.join(script_folder, self.cnf_file)

            elif os.path.isdir(self.calling_script):

                # if the calling 'script' is actually a folder

                # this will happen if the module is called in interactive mode
                config_file = os.path.join(self.calling_script, self.cnf_file)

            else:
                # we have a problem...
                msg = "we cannot find the configuration file :\n" + self.cnf_file

                raise IOError(msg)

            # print self.calling_script
            # print self.cnf_file
            # print script_folder
            # print config_file

        pretty = "configuration file"
        self.set_attribute(attr="config_file",
                           value=config_file,
                           pretty=pretty)

        self.check_file_exists(attr="config_file", pretty=pretty)

        self.config_parser = configparser.ConfigParser()

        # By using ExtendedInterpolation, the syntax
        # for the dynamic setting of values is richer
        # https://wiki.python.org/moin/ConfigParserExamples
        # We are using variables such as ${section:variable} instead of %(variable)s
        # Warning: https://github.com/flakshack/pyPerfmon/issues/1

        self.config_parser._interpolation = configparser.ExtendedInterpolation()

        self.config_parser.read(self.config_file)

        self.read_config()

    #######################################################################
    def finish_reading_configuration(self):

        print("\n--- END reading configuration ---\n")

        if self.ask_ready:

            self.ask_user_whether_ready()

    #######################################################################
    def ask_user_whether_ready(self):

        script_filename = os.path.basename(self.calling_script)

        msg = "Are you ready to launch '" + script_filename + \
            "' with this configuration? (y/n)\n\n- Your answer: "

        answer = raw_input(msg)

        if answer.lower() not in ("y", "yes"):

            print("\n--- ABORT ---\n")
            sys.exit()

    #######################################################################
    def check_file_exists(self, attr, pretty=None):

        path = getattr(self, attr)

        if pretty is None:
            pretty = attr

        if not os.path.isfile(path):

            msg = path + " ERROR : " + pretty + " does not exist !!! "

            raise IOError(msg)

    #######################################################################
    def set_attribute_list(self, params_list):

        for param in params_list:
            self.set_attribute(attr=param)

    #######################################################################
    def set_attribute(self, attr, value=None, pretty=None, print_attr=True):
        """
        This function allows to set an attribute by providing the attribute name 'attr' as a string. Either the value can be provided directly. If it is not (value = None), it is search in config_data.
        """

        if value is None:

            if attr not in self.config_data:
                msg = "ERROR : '" + attr + "' is not part of the config file."
                raise Exception(msg)

            value = self.config_data[attr]

        setattr(self, attr, value)

        if print_attr:
            self.print_attribute(attr, pretty)

    #######################################################################
    def print_attribute(self, attr, pretty=None):

        value = getattr(self, attr)

        if pretty is None:
            pretty = attr.replace("_", " ")

        if isinstance(value, list):

            elem = value[0]

            self.print_pretty(pretty, elem)

            for elem in value[1:]:

                self.print_pretty("", elem)

        else:
            self.print_pretty(pretty, value)

    #######################################################################
    def print_pretty(self, pretty, value):

        msg = '{:>{}}  {}'.format(pretty + ': ',
                                  self.char_width,
                                  str(value))
        print(msg)

    #######################################################################
    def comma_separated_value_to_list(self, str):

        lst = [key_pair.strip() for key_pair in str.split(",")]

        return lst

    #######################################################################
    def to_bool(self, str):

        return str.lower() in ['true', '1', 'y', 'yes']

    #######################################################################
    def complete_path(self, path):
        """
        If a path is not absolute, it is relative.
        If it is relative,
        complete it by prepending it with the HOME of the user.
        """

        if os.path.isabs(path):

            return path

        else:

            home = os.path.expanduser("~")

            completed_path = os.path.join(home, path)

            return completed_path

    #######################################################################
    def read_config(self):
        """
        Returns:
        --------
        dict
            a map of the parameters specified.
            The dictionary is in the form:
                cnf parameter name (lowercased) -> parsed value specified in cnf file

        """

        params = {}

        for section in self.config_parser.sections():
            # print "[" + section + "]"
            for option in self.config_parser.options(section):
                # print option + ":"

                params[option] = self.config_parser.get(section, option)

                if option in self.str_conversion:
                    params[option] = self.str_conversion[option](
                        params[option])

        self.config_data = params
        # print params
        # return params

    #######################################################################
    def check_calling_script(self):

        script_filename = os.path.basename(self.calling_script)
        config_file = os.path.basename(self.config_file)

        if script_filename in self.excluded:
            print(script_filename + " is excluded in " + config_file)
            script_excluded = True
        else:
            script_excluded = False

        # if not script_filename in self.included:
        #     print(script_filename + " is not included in " + config_file)
        #     script_included = False
        # else:
        #     script_included = True

        # if script_excluded or not script_included:
        if script_excluded:
            print("--- ABORT ---")
            sys.exit()

        # set up the log file
        log_file = os.path.join(self.log_folder, script_filename + ".log")

        self.log_file = log_file

    #######################################################################
    def __repr__(self):
        return str(pprint.pprint(self.config_data))

    #######################################################################
    def __str__(self):

        # import json
        # return json.dumps(self.config_data)
        # for key, value in self.config_data.items():

        if self.config_data is not None:

            params = (key + " : " + str(value) for key,
                      value in self.config_data.items())

            return "\n".join(params)

        else:

            return "Config data is empty"


class ConfigTest(ConfigReader):

    """
    This is an example of implementation of ConfigReader
    """

    def __init__(self, cnf_file, char_width=36):

        super(ConfigTest, self).__init__(
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
        self.ask_ready = None  # overwrites 'True' from sup
        self.existing_output_folder_blocks = None
        self.existing_output_file_blocks = None

        # [UD_parsing]
        self.server_url = None
        self.use_server = None

        # How to recognize a filename.
        # For instance:
        # File without extension:     ^([^.]+)$
        # Text file with extension      .txt : .*\.txt
        self.input_filename_regex = None

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

        # a container of conversion functions
        # ------------------------------------

        self.str_conversion = {
            "prog_folder": self.complete_path,
            "data_folder": self.complete_path,
            "start_folder": self.complete_path,
            "ready_folder": self.complete_path,
            "processed_folder": self.complete_path,
            "ud_folder": self.complete_path,
            "log_file": self.complete_path,
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

    #######################################################################
    def read(self):

        self.start_reading_configuration()

        # [IO]
        # ----

        self.set_attribute_list(['prog_folder',
                                 'data_folder',
                                 'start_folder',
                                 'ready_folder',
                                 'processed_folder',
                                 'ud_folder',
                                 'log_folder'])

        # [Management]
        # ------------
        # Earlier, this line was useful, because
        # I could not easily include log format in the configuration file so it is passed here as an argument
        # self.set_attribute(attr="log_format", value=self.log_format)
        self.set_attribute(attr="log_format")

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

        # [UD_parsing]
        # ------------

        pretty = "CoreNLP server URL"
        self.set_attribute(attr="server_url", pretty=pretty)

        self.set_attribute_list(['use_server',
                                 'input_filename_regex',
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

    # Testing the class
    # -----------------

    empty_config = ConfigReader("config_test.cnf")

    empty_config.read()

    # print empty_config

    # Testing an example of an instance of the class
    # ----------------------------------------------

    example_config = ConfigTest("config_test.cnf")

    example_config.read()

    # print example_config
