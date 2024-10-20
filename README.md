# Traffic Light Manager

This project aims to create a new kind of Traffic light using sensors to manage and avoid the Traffic in a crossroad.

## SUMO_prototype1

This is the first sumo prototype of the traffic light.

### Installing

First, install the [SUMO API](https://sumo.dlr.de/docs/Installing/index.html) and the python library [traci](https://sumo.dlr.de/docs/TraCI.html). The SUMO API is used to launch the [simulation](SUMO_prototype1/sumo_prototype1_test.sumocfg) created by the sumo's utility [NetEdit](https://sumo.dlr.de/docs/Netedit/index.html).

**Dependencies** :

- Eclipse SUMO sumo Version 1.21.0
- Eclipse SUMO netedit Version 1.21.0
- python's library traci 1.21.0


After installing every dependencies just launch the python file "[traffic_light_test.py](traffic_light_test.py)" :

```bash
python3 traffic_light_test.py
```

This script uses the [SUMO_prototype1](SUMO_prototype1.py) class that launch automatically the prototype1. And then you can use its method check_inductive_loops() to get which traffic light is busy. So then knowing that input you can just change the state of the lights using taci lib ( example : *traci.trafficlight.setRedYellowGreenState(proto.traffic_light_id, "GGGrrrGGGrrr")* )


