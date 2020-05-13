from mrjob.job import MRJob
from mrjob.step import MRStep

class airportData(MRJob):
    def steps(self):
        return [
                MRStep(mapper = self.mapper_getDST,
                    reducer = self.reducer_listAirports)
        ]

    def mapper_getDST(self, _, line):
        data = [airportDataEntry.strip('"') for airportDataEntry in line.split(',')]
        DST, Type = data[10], data[12]
        if (DST == '"S"' and Type == '"airport"'):
            airportName = data[1]
            yield airportName, 1

    def reducer_listAirports(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    airportData.run()
