


def nextClosestTime(time):
    h, m = time.split(":")
    curr = int(h) * 60 + int(m)
    for i in range(curr + 1, curr + 24 * 60 + 1):
        t = i % 1440
        h, m = t // 60, t % 60
        result = "{:02d}:{:02d}".format(h, m)
        if set(result) <= set(time):
            return result



nextClosestTime("11:23")