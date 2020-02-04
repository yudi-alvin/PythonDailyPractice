"""
This problem was asked by Snapchat.
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
----------------------same as the railway arrival and dept problem-----
"""
arr=[(30, 75), (0, 50), (60, 150)]
start_times = [(t[0], 1) for t in arr]  # [(30, 1), (0, 1), (60, 1)]
end_times = [(t[1], -1) for t in arr]  # [(75, -1), (50, -1), (150, -1)]
room_allocation = [t[1] for t in sorted(start_times + end_times, key=lambda t: t[0])]  # (0, 1),(30, 1),(50, -1),(60, 1),(75, -1),(150, -1)
                                                                                        #1,1,-1,1,-1,-1
rooms, max_rooms = 0, 0
for event in room_allocation:
    rooms += event  # occupied or released
    max_rooms = max(max_rooms, rooms)
assert(rooms == 0)

print(max_rooms)