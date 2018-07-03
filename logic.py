import random

powerball_results = sorted(random.sample(range(1,69), 5))
powerball_special = random.sample(range(1,26), 1)

print("For the Powerball, pick: " + str(powerball_results) + " and the special number: " + str(powerball_special))

mega_results = sorted(random.sample(range(1,70), 5))
mega_special = random.sample(range(1,25), 1)

print("For Megamillions, pick: " + str(mega_results) + " and the special number: " + str(mega_special))