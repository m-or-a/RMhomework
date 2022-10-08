class MedianFinder:
    def __init__(self):
        self.seq = []

    def add_num(self, num):
        self.seq.append(num)

    def find_median(self):
        self.seq.sort()
        l = len(self.seq)
        if l == 0:
            return 0
        elif l % 2 == 1:
            return self.seq[l//2]
        else:
            return (self.seq[l//2 - 1] + self.seq[l//2])/2
