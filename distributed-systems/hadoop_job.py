from mrjob.job import MRJob

class RFMLJob(MRJob):
    def mapper(self, _, line):
        fields = line.split(',')
        if fields[1].isdigit():
            yield fields[0], int(fields[1])

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    RFMLJob.run()
