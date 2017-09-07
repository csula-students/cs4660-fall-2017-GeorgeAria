"""Files tests simple file read related operations"""

class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        # self = this(in Java)
        filez = open(file_path)
        self.numbers = []
        for line in filez:
            numberline = line.split()
            numbers = [int(n) for n in numberline]
            self.numbers.append(numbers)
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        """

    def get_mean(self, line_number):
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
        mean = 0.0
        for i in range(len(self.numbers[line_number])):
            mean += self.numbers[line_number][i]
        mean /= len(self.numbers[line_number])
        return mean

    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
        max300 = 0.0
        for i in range(len(self.numbers[line_number])):
            if self.numbers[line_number][i] > max300:
                max300 = self.numbers[line_number][i]
        return max300

    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
        min300 = self.numbers[line_number][0]
        for i in range(len(self.numbers[line_number])):
            if self.numbers[line_number][i] < min300:
                min300 = self.numbers[line_number][i]
        return min300

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
        sums = 0.0
        for i in range(len(self.numbers[line_number])):
            sums += self.numbers[line_number][i]
        return sums
