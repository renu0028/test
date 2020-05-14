from mrjob.job import MRJob
from mrjob.step import MRStep

class airportRoutes(MRJob):
    def steps(self):
        return [
                MRStep(mapper = self.mapper_getFlightRoutes,
                    reducer = self.reducer_listFlightRoutes)
        ]

    def mapper_getFlightRoutes(self, _, line):
        routesData = line.split(',')
        numOfRoutes = 0
        sourceAirport, destinationAirport = routesData[2], routesData[4]
        if (sourceAirport == "IND" and destinationAirport == "ATL"):
            numOfRoutes += 1
            yield "Possible routes from source A to destination B are", 1

    def reducer_listFlightRoutes(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    airportRoutes.run()
