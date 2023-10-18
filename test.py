level = int(input("Enter level: "))


conditions = [level > 0 and level <= 15, level > 15 and level <= 40, level > 40 and level <= 100]
results = [True if cond else False for cond in conditions]

for i, condition_result in enumerate(results):
    if results[i] == True:
        match i:
            case 0:
                print("level is between 0 and 15")
                break
            case 1:
                print("level is between 16 and 40")
                break
            case 2:
                print("level is over 40")
                break