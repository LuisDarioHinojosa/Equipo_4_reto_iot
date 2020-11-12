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
    return f"2020-{randomStringNum(12)}-{randomStringNum(31)}"


def generateRandomHour():
    return f"{randomStringNum(24)}:{randomStringNum(60)}:{randomStringNum(60)}"


id_persons = [i for i in range(1, 7)]

for id in id_persons:
    rest = 6
    for i in range(2500):
        med = randint(60, 120)
        try:
            enterData.createHeartbeatRegister(
                float(med), "2020-10-15",  "12:01:12", "anemia", id, "root", "(phoskyGUP28)")
        except:
            print("Could not enter data")
            continue
    for i in range(2500):
        med = randint(60, 120)
        try:
            enterData.createOxygenRegister(
                float(med), "2020-10-15",  "12:01:12", "anemia", id, "root", "(phoskyGUP28)")
        except:
            print("Could not enter data")
            continue
    rest -= 1
    print(F"Remaining person registers left: {rest}")
