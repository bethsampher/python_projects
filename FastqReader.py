class FastqReader(object):

    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        self.data = open(self.name)
        return self

    def __exit__(self, *args):
        self.data.close()


    def read(self):
            name = self.data.readline().strip()
            if not name:
                return None
            sequence = self.data.readline().strip()
            self.data.readline()
            phred = self.data.readline().strip()
            return Read(name, sequence, phred)

class Read(object):

    def __init__(self, name, sequence, phred):
        self.name = name
        self.sequence = sequence
        self.phred = phred

    def phred_calculator(self):
        total_error = 0
        for value in self.phred:
            phred_score = float(ord(value) - 33)
            p_error = 10**(-phred_score / 10)
            total_error += p_error
        return total_error


