import time
from SUMO_prototype1 import *


def traffic_light_test():

    proto = prototype1()
    proto.launch()

    # Début de la simulation
    try:
        for step in range(1000): 
            traci.simulationStep()  #Avance la simulation d'un pas

            last_traffic = proto.check_inductive_loops() 

            if last_traffic != None:
                if (last_traffic == "e1_0") or last_traffic == "e1_2" :
                    traci.trafficlight.setRedYellowGreenState(proto.traffic_light_id, "GGGrrrGGGrrr")

                if (last_traffic == "e1_1") or last_traffic == "e1_4" :
                    traci.trafficlight.setRedYellowGreenState(proto.traffic_light_id, "rrrGGGrrrGGG")
            time.sleep(0.01)
    finally:
        traci.close()  

if __name__ =='__main__':
    traffic_light_test()