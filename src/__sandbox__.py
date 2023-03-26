import csv
import os.path
import src.environment as env


def sandbox():
    with open(os.path.join(env.ROOT_DIR + "/data/instances/lyon_200_2_3/visits.csv"), "r") as csvfile:
        areader = csv.reader(csvfile, delimiter=',')
        print(areader)
        for row in areader:
            print(', '.join(row))


if __name__ == '__main__':
    sandbox()
