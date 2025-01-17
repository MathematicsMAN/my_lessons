def find_short(s):
    sp = s.split()
    smallest = len(sp[0])
    for w in range(1, len(sp)):
        a = len(sp[w])
        if a < smallest:
            smallest = a

    return smallest

print(find_short("bitcoin take over the world maybe who knows perhaps"))


def controller(events):
    state = 2 # 0 opening, 1 closing, 2 not moving
    currentOpen = 0
    output = ""
    pause = False
    for i in range(len(events)):
        if events[i] == "P":
            if currentOpen == 0 and 2:
                state = 0
            elif currentOpen == 5 and 2:
                state = 1
            else:
                pause = not pause
        elif events[i] == "O":
            state = 1-state
        if state == 0 and not pause:
            currentOpen = min(5, currentOpen+1)
        elif state == 1 and not pause:
            currentOpen = max(0, currentOpen-1)
        output += str(currentOpen)
    return output

print(controller('..P...O...'))

def sum_no_duplicates(l):
    s = set(l)
    es = sum(l) - sum(s)
    return sum(s) - es

print(sum_no_duplicates([1, 1, 2, 3]))