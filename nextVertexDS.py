import config
class nextVertexDS:
    def __init__(self, _nextVert, _leastTime):
        self.nextVert = _nextVert
        self.leastTime = _leastTime

    def printData(self):
        print("Data = ",self.nextVert," and ",self.leastTime)


class NodePairOracle:
    def __init__(self,intervalInMins, intervalInkWh):
        maxkWh = config.maxkWh
        nodeOracleDict = {}
        for time in range(0,24*60+1,intervalInMins):
            kwhDict = {}
            timeInMins = float(time/60)
            for kWh in range(0,maxkWh+1,intervalInkWh):
                print(timeInMins,"----",kWh)
                test = nextVertexDS(1000000,1000000)
                testDict =[test.nextVert, test.leastTime] 
                kwhDict[int(kWh)] = testDict
            nodeOracleDict[int(timeInMins)]=kwhDict
        self.nodeOracleDict = nodeOracleDict

    def printData(self):
        print(self.nodeOracleDict)
            
                
                
                

        
        
        
        
