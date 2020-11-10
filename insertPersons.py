import enterData
from random import randint

id_persons = [i for i in range(1, 7)]

for id in id_persons:
    for i in range(2500):
        med = randint(60, 120)
        enterData.createHeartbeatRegister(float(
            med), "20-10-15", "08:00:00", "ya colgo los tenis", id, "root", "(phoskyGUP28)")
    for i in range(2500):
        med = randint(60, 120)
        enterData.createOxygenRegister(float(med), "20-10-15",
                                       "12:01:12", "anemia", id, "root", "(phoskyGUP28)")
