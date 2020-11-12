import enterData
from random import randint

# "2020-10-15"
# "12:01:12"


def randomStringNum(threshold):
    genereate = randint(1, threshold)
    if(genereate < 10):
        return f"0{genereate}"
    else:
        return str(genereate)


# Just dates within 2020
def generateRandomDate():
    return f"2020-{randomStringNum(11)}-{randomStringNum(29)}"


def generateRandomHour():
    return f"{randomStringNum(23)}:{randomStringNum(59)}:{randomStringNum(59)}"


id_persons = [i for i in range(1, 7)]
rest = 6
for id in id_persons:
    for i in range(2500):
        med = randint(60, 120)
        try:
            enterData.createHeartbeatRegister(
                float(med), f"{generateRandomDate()}",  f"{generateRandomHour()}", "anemia", id, "root", "(phoskyGUP28)")
        except Exception as e:
            print(e)
            continue
    for i in range(2500):
        med = randint(60, 120)
        try:
            enterData.createOxygenRegister(
                float(med), f"{generateRandomDate()}",   f"{generateRandomHour()}", "anemia", id, "root", "(phoskyGUP28)")
        except Exception as e:
            print(e)
            continue
    rest -= 1
    print(F"Remaining person registers left: {rest}")
