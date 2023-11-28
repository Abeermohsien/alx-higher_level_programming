#!/usr/bin/python3
for k in range(10):
    for j in range(k, 10):
        if k < j:
            print("{:d}{:d}".format(k, j),
                    end="\n" if k == 8 and j == 9 else ", ")
