from collections import deque

def flights(*args):
    result = {}
    input_data = deque(args)

    while input_data:
        value = input_data.popleft()

        if value == "Finish":
            return result
        
        elif type(value) == str:
            passengers = input_data.popleft()

            if value in result.keys():
                result[value] += passengers
            else:
                result[value] = passengers

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))