class Checksum(object):
    def validate_account_checksum(self, number):
        iterator_value = 2
        result = 0
        firstValue = True
        ZERO_VALUE = 0
        DIVISOR_VALUE = 11
        ERROR = " ERR"

        for digit in number:
            if firstValue:
                result += digit
                firstValue = False
            else:
                result += (iterator_value * digit)
                iterator_value += 1
        if result % DIVISOR_VALUE == ZERO_VALUE:
            return result
        return result + ERROR