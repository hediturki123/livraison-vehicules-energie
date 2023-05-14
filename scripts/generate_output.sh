#!/bin/bash

mkdir -p ../outputs
mkdir -p ../outputs/demo

for entry in "../data/instances"/*
do
    for heuristic in "insert" "swap" "triplet_shift"
    do
        for dertiminism in "d" "nd"
        do
            for solution in "fs" "bs"
            do
                echo "Generating '${entry##*/}__${heuristic}__${dertiminism}_${solution}.txt'..."
                poetry run python ../src/__init__.py "${entry##*/}" -h "${heuristic}" -"${dertiminism}" -"${solution}" -o history > ../outputs/demo/"${entry##*/}"__"${heuristic}"__"${dertiminism}"_"${solution}".txt
            done
        done
    done
done
echo "Done!"
