def find_busiest_period(data):
    # if len(data) == 1:
    #  return data[0][0]
    people = 0
    maxtime = 0
    maxpeople = 0
    # if len(data) == 1:
    #  return data[0][0]

    for ind in range(len(data)):
        # for ind, d in enumerate(data):
        t, n, status = data[ind]
        if status == 1:
            people += n
        else:
            people -= n

        if ind < len(data) - 1 and t == data[ind + 1][0]:
            continue

        # if ind == len(data) - 1 or t != data[ind+1][0]:
        if people > maxpeople:
            maxpeople = people
            maxtime = t
        print(people, maxpeople)

    return maxtime


def find_busiest_period(data):
    people = 0
    maxtime = 0
    maxpeople = 0

    for ind, d in enumerate(data):
        t, n, status = d
        if status == 1:
            people += n
        else:
            people -= n
        if ind == len(data) - 1 or t != data[ind + 1][0]:
            if people > maxpeople:
                maxpeople = people
                maxtime = t

    return maxtime





