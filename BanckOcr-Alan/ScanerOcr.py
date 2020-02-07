class ScanerOcr(object):

    def __init__(self) -> object:
        self.numbers = ""
        self.lines = None

    def scan_document(self, account):
        file = open(account, 'r')
        self.lines = file.read()
        file.close()
        self.lines =  self.lines.splitlines()
        print( self.lines)

    def getNumbers(self):
        numbersAccount = "";
        indexEnd = 0;
        lenghtLine = 0;
        LINES = self.lines.lenght()
        decode_number = DecodeNumber()







def main():
    sca = ScanerOcr()
    sca.scan_document("Account.txt")


if __name__ == '__main__':
    main()
