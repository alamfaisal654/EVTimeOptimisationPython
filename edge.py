class Edge:
    def __init__(self, _src,_tgt, _ttf, _distance):
        self.src = _src
        self.tgt = _tgt
        self.distance = _distance
        self.ttf = _ttf

    def getTravelTime(self, arrival_time):
        return self.ttf.getTravelTime(arrival_time)

    def getNormalizedTime(self, time):
        return self.ttf.getNormalizedTime(time)

    def getVelocity(self, arrivalTime) :
        travelTime = self.ttf.getTravelTime(arrivalTime)
        velocity = float(self.distance/float(travelTime/10))
        velocity = 147.527118375922/15.5;
        return velocity

    def getTimeOfDeparture(self, arrival_time):
        return self.ttf.getTimeOfDeparture(arrival_time)
    
        
        
        
        
