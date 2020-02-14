from banckocr.NumberStorage import NumberStorage


class FileScanner(object):

    def scan_file(self, file_path):
        f = open(file_path, "r")
        result_number = ""
        try:
            result_number = self.read_file_content(f)
        except ValueError:
            result_number = "something was wrong"
        finally:
            result_number

    def read_file_content(self, file):
        content = []
        number = ""
        DEFAULT_VALUE = "?"
        ERROR = " ILL"
        lines = file.readlines()
        for line in lines:
            content.append(line)
        if self.verify_size(content):
            number = self.split_number(content)
            number = number.concat(ERROR) if number.contains(DEFAULT_VALUE) else number
        return number

    def verify_size(self, content):
        is_valid = True
        SIZE = 27
        for item in content:
            if len(item) > SIZE:
                isValid = False
                break
        return is_valid;

    def split_number(self, content):
        number_storage = NumberStorage()
        number = ""
        temp = ""

        FIRST_OBJECT = 0
        SECOND_OBJECT = 1
        THIRD_OBJECT = 2
        INCREMENT = 3

        init = 0
        last = 3

        size = len(content[FIRST_OBJECT])

        while last <= size:
            temp = ""
            temp += content[FIRST_OBJECT][init:last]
            temp += content[SECOND_OBJECT][init:last]
            temp += content[THIRD_OBJECT][init:last]
            number += number_storage.verify_number(temp)
            init = last
            last += + INCREMENT
        return number
