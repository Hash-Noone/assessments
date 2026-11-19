def min_servers(jobs):
    new_list_1 = sorted([job [0] for job in jobs])
    new_list_2 = sorted([job [1] for job in jobs])
    i = 0
    j = 0
    while i < len(new_list_1):
        if new_list_1[i] >= new_list_2[j]:
            j += 1
        i += 1
    return i - j


jobs = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 8],
    [8, 9],
    [9, 10],
    [10, 11],
    [11, 12],
    [12, 13],
    [13, 14],
    [14, 15],
    [15, 16],
    [16, 17],
    [17, 18],
    [18, 19],
    [19, 20],
    [20, 21],
    [21, 22],
    [22, 23],
    [23, 24],
    [24, 25],
    [25, 26],
    [26, 27],
    [27, 28],
    [28, 29],
    [29, 30],
    [30, 31]
]

print(min_servers(jobs))

# I sorted the server start time and server end time while they were saved in different arrays
# I tracked them with seperate indices
# I always move the start server while i only move the end server when a start can take over from it
# so to get the maximum server we need to just know the difference between the server started
# minus the remaining end times not used
# Time complexity 0(nlogn)
# Auxillary Space complexity 0(n)
