# https://www.algoexpert.io/questions/Valid%20Starting%20City

# First attempt

# distances[i] is the distance from city i to city i+1 (to the city 0 for the last city)
# fuel[i] is the quantity of available fuel in city i
# mpg is the distance traveled per unit of fuel
# starting with 0 fuel

# exactly enough fuel to travel all cities

def validStartingCity(distances, fuel, mpg):
    # converting the quantity of fuel available in each city into distance travelable
    distances_per_city = [n * mpg for n in fuel]
    print(distances_per_city)

    fuel_output = []

    # mesuring surplus or deficit of distance travelable given for each city
    for i in range(len(distances)):
        distance = distances_per_city[i] - distances[i]
        fuel_output.append(distance)
    
    print(fuel_output)

    # looping through each city starting from index 0
    for i in range(len(fuel_output)):
        start = i
        fuel_reserve = 0
        print(f"start : {i}")

        # recreating the list starting from index start
        list_from_start = [
            fuel_output[(start + h) % len(fuel_output)] for h in range(len(fuel_output))]
        
        # looping through the circuit of cities starting from index "start"
        for j in list_from_start:
            fuel_reserve += j
            # if the fuel reserve becomes negative, stops the loop
            if fuel_reserve < 0:
                print(f"stop : {j}")
                break
        # if the loop stopped, this becomes True and we can move to the next starting position
        if fuel_reserve < 0:
            continue
        # if the loop go through entirely, fuel_reserve is at 0 without going negative at any point
        # and breaking the previous loop
        else:
            return i

# Clean version
def validStartingCity(distances, fuel, mpg):
    distances_per_city = [n * mpg for n in fuel]
    fuel_output = []

    for i in range(len(distances)):
        distance = distances_per_city[i] - distances[i]
        fuel_output.append(distance)

    for i in range(len(fuel_output)):
        start = i
        fuel_reserve = 0
        list_from_start = [
            fuel_output[(start + h) % len(fuel_output)] for h in range(len(fuel_output))]
        
        for j in list_from_start:
            fuel_reserve += j
            if fuel_reserve < 0:
                break

        if fuel_reserve < 0:
            continue
        else:
            return i
