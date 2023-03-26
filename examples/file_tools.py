'''
Reading and writing files example

@author: Vassilissa Lehoux
'''

import numpy as np
import csv
import os

def with_numpy_txt():
    """
    Saving and loading an array
    """
    myarray = np.array([[1,2,3], [4, 5, 6]])
    print("Saved to text file", myarray)
    apath = "."  # a path to the file
    afilename = "test_file.txt"
    np.savetxt(os.path.join(apath, afilename), myarray, delimiter=",")
    with open(os.path.join(apath, afilename), "r") as txtfile:
        copy_array = np.loadtxt(txtfile, delimiter=",").astype(np.int64)
        print("Loaded from text file", copy_array)

def with_csv():
    """
    Saving and loading a csv file
    """
    apath = "."  # a path to the file
    afilename = "test_file.csv"
    header = ["col1", "col2", "col3"]
    row1 = [1, 25, "a"]
    row2 = [23.1, 2, "b"]
    # Writing the file
    with open(os.path.join(apath, afilename), "w") as csvfile:
        awriter = csv.writer(csvfile, delimiter=',')
        awriter.writerow(header)
        awriter.writerow(row1)
        awriter.writerow(row2)

    with open(os.path.join(apath, afilename), "r") as csvfile:
        areader = csv.reader(csvfile, delimiter=',')
        for row in areader:
            print(', '.join(row))


if __name__ == '__main__':
    with_numpy_txt()
    with_csv()
