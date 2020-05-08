# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.
# (x2 - x1)(y3 - y1) - (x3 - x1) (y2- y1)

import numpy as np
def main():
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    # coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    # coordinates = [[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]
    # coordinates = [[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]

    if(len(coordinates) == 1):
        print(True)

    for i in range(len(coordinates)-2):
        if ((coordinates[i+1][0] -coordinates[i][0])*(coordinates[i+2][1] -coordinates[i][1])) - ((coordinates[i+2][0] -coordinates[i][0])*(coordinates[i+1][1] -coordinates[i][1])):
            print(False)

    print(True)
if __name__ == "__main__":
    main()
