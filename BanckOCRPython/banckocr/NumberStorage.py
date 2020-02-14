class NumberStorage(object):
    def __int__(self):
        self.ZERO = " _ | ||_|"
        self.ONE = "     |  |"
        self.TWO = " _  _||_ "
        self.THREE = " _  _| _|"
        self.FOUR = "   |_|  |"
        self.FIVE = " _ |_  _|"
        self.SIX = " _ |_ |_|"
        self.SEVEN = " _   |  |"
        self.EIGHT = " _ |_||_|"
        self.NINE = " _ |_| _|"
        self.DEFAULT_VALUE = '?'

    def verify_number(self, string_number):
        numbers = {self.ZERO: "0", self.ONE: "1", self.TWO: "2", self.THREE: "3", self.FOUR: "4", self.FIVE: "5",
                   self.SIX: "6", self.SEVEN: "7", self.EIGHT: "8", self.NINE: "9"}
        item = numbers.get(string_number, self.DEFAULT_VALUE)
        return item
