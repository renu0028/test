from mrjob.job import MRJob
from mrjob.step import MRStep

class airportTimeZone(MRJob):
    def steps(self):
        return [
                MRStep(mapper = self.mapper_getTimeZone,
                    reducer = self.reducer_getAirportName)
            ]

    def mapper_getTimeZone(self, _, line):
        data = [airportDataEntry.strip('"') for airportDataEntry in line.split(',')]
        TimeZone, Type  = data[9], data[12]
        if (TimeZone == "5.5" and Type == '"airport"'):
            airportName = data[1]
            yield airportName, 1

    def reducer_getAirportName(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    airportTimeZone.run()
