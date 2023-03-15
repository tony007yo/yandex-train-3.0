M = int(input())
N = int(input())

def intersect_lines(line1, line2):
    return line1[0] <= line2[1] and line1[1] >= line2[0] 

def calc(N, M):
    if N == 0:
        return 0
    event = [tuple(map(int, input().split())), True]
    events = [event]
    count_of_false = 0
    for pos in range(1, N):
        event = [tuple(map(int, input().split())), True]
        for i in range(len(events)):
            if events[i][1] and intersect_lines(events[i][0], event[0]):
                events[i][1] = False
                count_of_false += 1

        events.append(event)
    return N - count_of_false

print(calc(N, M))