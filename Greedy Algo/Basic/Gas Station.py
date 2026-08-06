gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
def gas_station(gas,cost):
    start=0
    tank=0
    total=0
    for i in range(len(gas)):
        gain=gas[i]-cost[i]
        tank+=gain
        total+=gain
        if tank<0:
            start=i+1
            tank=0
    if total<0:
        return False
    return start
print(gas_station(gas,cost))