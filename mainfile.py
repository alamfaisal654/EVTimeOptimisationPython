from graph import graph
from nextVertexDS import *
import config
import pickle
import json

def main():
##    grap = graph()
##    grap.testTTF(8)
    nodeOracle = NodePairOracle(30,2)
##    json.dumps(nodeOracle.nodeOracleDict)
    nodeOracle.printData()
##    with open('result.json', 'w') as fp:
##        json.dump(nodeOracle.nodeOracleDict, fp)
    with open("AllShortestDists/test.pickle", "wb") as outfile:
        pickle.dump(nodeOracle, outfile)
    with open("AllShortestDists/test.pickle", "rb") as infile:
        test_dict_reconstructed = pickle.load(infile)
    test_dict_reconstructed.printData()
    
 
    
    

if __name__ == "__main__":
    main()
    
