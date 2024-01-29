import config

class TTF:
    def __init__(self, _points):
        self.points = _points
        lastTuple = self.points[-1]
        self.points.append((config.maxTime, lastTuple[1]))
##        self.printPoints()

    def printPoints(self):
        print(self.points)

    def getNormalizedTime(self, time):
        self.checkArrivalTime(time)
        time = time % config.maxTime;
        return int(time);

    def checkArrivalTime(self, arrival_time):
        if arrival_time<0:
            print("Arrival Time is negative")
            exit(1)
            
    def getTravelTime(self, arrival_time):
        self.checkArrivalTime(arrival_time)
        arrival_time = self.getNormalizedTime(arrival_time)
        for p in self.points:
            if p[0] <= arrival_time:
                prev_point = p
            else:
                next_point = p
                break
        slope = float(next_point[1] - prev_point[1])/(next_point[0] - prev_point[0])
        travel_time = prev_point[1] + float(slope * (arrival_time-prev_point[0]))
        return int(travel_time);

    def getTimeOfDeparture(self, arrival_time):
        travel_time = self.getTravelTime(arrival_time);
        departure_time = self.getNormalizedTime(arrival_time + travel_time)
        return departure_time
    
                
        



    
        
        
        
