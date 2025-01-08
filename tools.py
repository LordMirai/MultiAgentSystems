import datetime
import os
import random

from faker import Faker

fake = Faker()


class Tools:
    @staticmethod
    def parse(text):
        """
        Parse the text for commands.
        The format is <<COMMAND>> <args>


        :param text:  str - the text to parse
        :return: str - the result of the command or False if the text is not a valid command
        """
        text = text.strip()
        if text == "":
            return False

        print("Parsing: ", text)
        args = text.split(" ")
        cmd = args[0].upper()

        args_no_case = text.lower().split(" ")[1:]  # remove the command from the args
        args = args[1:]

        if cmd == "<<EXIT>>":
            print("Exiting...")
            exit(0)
        elif cmd == "<<SEARCH>>":
            hit, line, content = Tools.file_search(" ".join(args_no_case))
            if not hit:
                return "Not found"
            else:
                return f"Found in {hit} at line {line}: {content}"
        elif cmd == "<<RANDCOLNUM>>":
            return Tools.rand_col_number()
        elif cmd == "<<DATETIME>>":
            return Tools.get_date_time()
        elif cmd == "<<WRITE>>":
            return Tools.write_to_file(" ".join(args))
        elif cmd == "<<WRITEPLACEHOLDER>>":
            return Tools.write_to_file(True)
        elif cmd == "<<READLINE>>":
            return Tools.read_line(args[0])
        else:
            # input is not a valid command
            return False

    @staticmethod
    def file_search(contents: str) -> tuple:
        """
        Iterate through all files in the 'files' directory and search for the contents.
        :param contents:  str - the contents to search for (usually a word, but can be a phrase)
        :return:  tuple - (str, int, str) - the file path, the line number, and the line where the contents were found.
        If not found, return False, None, None
        """
        print("Searching for: ", contents)
        for root, _, files in os.walk('files'):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for index, line in enumerate(lines):
                        if contents in line.lower():
                            return file_path, index, line
        return False, None, None

    @staticmethod
    def rand_col_number():
        """
        Get a random color and number. Employ the Faker library.
        :return:
        """
        return f"Color/Number result -- {fake.color_name()} - {random.randint(1, 100)}"

    @staticmethod
    def get_date_time():
        """
        Get the current date and time. Formatted as 'DD-MM-YYYY HH:MM:SS'
        :return:  str - the current date and time
        """
        return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    @staticmethod
    def write_to_file(text):
        """
        Select a random file name and write the text to it.
        :param text: str - the text to write; if True, write placeholder text
        :return:
        """
        if not os.path.exists('output_files'):
            os.makedirs('output_files')

        if text is True:
            count = random.randint(10, 100)
            text = " ".join(fake.texts(nb_texts=count))

        file_name = fake.file_name(extension='txt')
        with open(f'output_files/{file_name}', 'w') as file:
            file.write(text)
        return f"Written to {file_name}.txt"

    @staticmethod
    def read_line(line_number):
        """
        Read a line from a random file. Select a random file from the 'files' directory.
        :param line_number:  str - the line number to read
        :return:
        """
        file = random.choice(os.listdir('files'))
        with open(f'files/{file}', 'r') as f:
            lines = f.readlines()
            try:
                return f"This is what was retrieved: '{lines[int(line_number)]}';"
            except IndexError:
                return "Line not found"
            except ValueError:
                return "Invalid line number"
            except Exception as e:
                return str(e)
