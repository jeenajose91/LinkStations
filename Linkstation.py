# Program creates a function to get the most suitable link station. The class LinkStation uses the input points as
# class parameters and has 2 functions which returns the distance and power of a device with a linkstation.

import math


class LinkStation:

    # class defining functions for calculating distance and power for a given linkstation from a given device.

    def __init__(self,point):
        # init function defining the device location
        self.X = point[0]
        self.Y = point[1]

    def get_power(self,reach,distance):

        # defines the function to calculate power of a link station for a device
        if distance > reach:
            return 0
        else:
            return (reach - distance)**2

    def get_distance(self,ls):
        return math.sqrt((ls[0]-self.X)**2+(ls[1]-self.Y)**2)


def get_link_station(link_st_list,point):

    # function to get the most suitable link station

    linkstation = LinkStation(point)
    suitable_link_stn = link_st_list[0]
    power = 0
    for ls in link_st_list:
        distance = linkstation.get_distance(ls)
        ls_power = linkstation.get_power(ls[2],distance)
        if ls_power > power:
            power = ls_power
            suitable_link_stn = ls
    if power == 0:
        print("No link station within the reach for point ",point[0],point[1])
    else:
        print("Best link station for point %d and %d is %d,%d with power %f" %(point[0],point[1],suitable_link_stn[0],suitable_link_stn[1],power))

# defining link  station and point constants
link_st = [[0,0,10],
           [20,20,5],
           [10,0,12]]
points = [[0,0],
          [100,100],
          [15,10],
          [18,18]
          ]

# Calling the function recursively for finding Link Station for each point if exist.
for pt in points:
    get_link_station(link_st,pt)

