from random import randint


def randomStringNum(threshold):
    genereate = randint(1, threshold)
    if(genereate < 10):
        return f"0{genereate}"
    else:
        return str(genereate)


# Just dates within 2020
def generateRandomDate():
    return f"2020-{randomStringNum(12)}-{randomStringNum(31)}"


def generateRandomHour():
    return f"{randomStringNum(24)}:{randomStringNum(60)}:{randomStringNum(60)}"


# "20-10-15"
# 12:01:12
