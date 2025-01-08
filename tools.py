import datetime
import os
import random
from faker import Faker


class Tools:
    @staticmethod
    def parse(text):
        text = text.strip()
        if text == "":
            return False, [], []

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
        elif cmd == "<<READLINE>>":
            return Tools.read_line(args[0])
        else:
            # assume it's not a command
            return False

    @staticmethod
    def file_search(contents: str) -> tuple:
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
        fake = Faker()
        return f"Color/Number result -- {fake.color_name()} - {random.randint(1, 100)}"

    @staticmethod
    def get_date_time():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def write_to_file(text):
        fake = Faker()
        file_name = fake.file_name()
        with open(f'output_files/{file_name}.txt', 'w') as file:
            file.write(text)
        return f"Written to {file_name}.txt"

    @staticmethod
    def read_line(line_number):
        # select random file from files/ to read from
        file = random.choice(os.listdir('files'))
        with open(f'files/{file}', 'r') as f:
            lines = f.readlines()
            try:
                return lines[int(line_number)]
            except IndexError:
                return "Line not found"
            except ValueError:
                return "Invalid line number"
            except Exception as e:
                return str(e)
