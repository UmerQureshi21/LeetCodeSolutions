from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    cars = []
    stack = []
    for i, pos in enumerate(position):
        cars.append({"p":pos,"s":speed[i],"t": (target-pos)/speed[i]})
    cars.sort(key=lambda car: car["p"])
    def reverse(arr: List[dict]):
        for i in range (len(arr)//2):
            temp = arr[i]
            arr[i] = arr[len(arr) - i - 1]
            arr[len(arr) - i - 1] = temp
    reverse(cars)
    
    for i,car in enumerate(cars):
        if len(stack) == 0 or car["t"] > stack[-1]["t"]:
            stack.append(car)
    return len(stack)



print(carFleet(10,[1,4],[3,2]))