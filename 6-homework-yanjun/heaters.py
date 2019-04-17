class Heater:

    def findRadius(self, houses, heaters):
        heaters.sort()
        houses.sort()
        radius = 0
        i = 0
        # 哨兵
        heaters = [-1] + heaters + [float('inf')]
        for house in houses:
            while house > heaters[i]:
                i = i + 1
            current_radius = min(house - heaters[i - 1], heaters[i] - house)
            radius = max(radius, current_radius)
        return radius


h = Heater()
result = h.findRadius([1, 2, 3, 4, 6], [1, 4])
print(result)

#ok