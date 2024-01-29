import csv
from TTF import *
from edge import *
from Node import Node
from  powerpersegment import *
import config
class graph:
    def __init__(self):
        self.coordFile = "dataset/NY/NY.coordinate"
        self.distanceFile = "dataset/NY/EdgeDistances.csv"
        self.tpgrFile = "dataset/NY/NY.tpgr"
        self.nodes=[]
        self.edges = []
        self.parseCoordFile()
        distances = self.parseDistanceFiles()
        self.parseEdgeFileAndCreateTTF(distances)
##        print(self.nodes[2].node_id)

    def parseDistanceFiles(self):
        distances = []
        for i in range(self.numCoords):
            distances.append([])
        with open(self.distanceFile, "r") as f:
            reader = csv.reader(f,delimiter=' ')
            for row in reader:
                node_src = int(row[0])
                node_dest = int(row[1])
                src_lat = float(row[2])
                src_long = float(row[3])
                tgt_lat = float(row[4])
                tgt_long = float(row[5])
                distance = float(row[6])
                distances[node_src].append((node_dest,distance))
        return distances

    def parseEdgeFileAndCreateTTF(self, distances):
        with open(self.tpgrFile, "r") as f:
            reader = csv.reader(f,delimiter=' ')
            firstrow = True
            for row in reader:
##                print(row)
                points = []
                if firstrow:
                    firstrow = False
                    n_nodes = int(row[0])
                    n_edges = int(row[1])
                    self.numEdges = n_edges
                    n_points = int(row[2])
                    period = int(row[3])
                    config.maxTime = period
                    continue
                else:
                    src = int(row[0])
                    tgt = int(row[1])
                    sample_size = int(row[2])
                    base = 3
                    
                    for i in range(0,sample_size,2):
                        index = base + i
                        x = float(row[index])
                        y = float(row[index+1])
                        if x < 0 or x >= period:
                            print("TPGR file corrupted: x-value not in [0,period)")
                            exit(1)

                        if y<0:
                            print("TPGR file corrupted: y-value smaller than 0.")
                            exit(0)

                        if len(points)!=0 and points[-1][0]>x:
                            print("TPGR file corrupted: x-value smaller than the one before "+ x)

                        points.append((x,y))

                    ttf = TTF(points)
                    dist = self.getDistance(src, tgt, distances)
                    edge = Edge(self.nodes[src], self.nodes[tgt], ttf, dist)
                    self.nodes[src].addEdge(edge)
                    self.edges.append(edge)



    def getDistance( self, _src, _tgt, distances):
        linkVec = distances[_src]
        for tuple in linkVec:
            if(_tgt == tuple[0]):
                return tuple[1]
        print("Distance not available for "+_src+" and "+_tgt)
        exit(1)
                        

    def parseCoordFile(self):
        nodes = []
        with open(self.coordFile, "r") as f:
            reader = csv.reader(f,delimiter=' ')
            firstrow = True
            for row in reader:
                if firstrow:
                    firstrow = False
                    self.numCoords = int(row[0])
                    self.topleft_lat = float(row[1])
                    self.topleft_long = float(row[2])
                    self.botright_lat = float(row[3])
                    self.botright_long = float(row[4])
                else:
                    node_id = int(row[0])
                    node_lat = float(row[1])
                    node_long = float(row[2])
                    node = Node(node_id, node_lat, node_long)
                    nodes.append(node)
            self.nodes = nodes

    def testTTF(self, val):
        ttf = self.edges[val]
        arrival_time = 36000;
        e = self.edges[val]
        t = e.getTravelTime(arrival_time)
        print("Travel Time = ",t)
        dist = e.distance
        print("Distance =",dist)
        vel = e.getVelocity(arrival_time)
        print("Velocity=",vel)
        tod = e.getTimeOfDeparture(arrival_time)
        print("Time of dep=",tod)
        power = powerpersegment(e, arrival_time)
        print("power=",power)
        
        





##        
##//        ttf = edges[val]->getTTF();
##//        ttf->printPoints();
##
##        cout<<std::setprecision(15);
##
##//        edges[8]->getTTF()->printPoints();
##        Edge* e = edges[1];
##
##        unsigned int arrival_time = 36000;
##        double x = e->getTravelTime(arrival_time);
##        cout<<"Departure= "<<x<<endl;
##        powerpersegment *pps = new powerpersegment();
##        double distance = e->getDistance();
##        cout<<"Distance= "<<distance<<" "<<endl;
##        double travelTime = e->getTravelTime(arrival_time);
##        cout<<"TravelTime= "<<travelTime<<endl;
##        double velocity = e->getVelocity(arrival_time);
##        cout<<"Velocity= "<<velocity<<endl;
##        double energy = pps->EnergyConsumption(e, arrival_time);
##        cout<<"Energy= "<<energy<<" "<<endl;
##    }

    
                    
                    
                    

                
                    

                    
