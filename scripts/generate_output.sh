#!/bin/bash

for entry in "../data/instances"/*
do
    echo "${entry##*/}"
    for heuristic in "insert" "swap" "triplet_shift"
    do
        for dertiminism in "d" "nd"
        do
            for solution in "fs" "bs"
            do
                poetry run python ../src/__init__.py "${entry##*/}" -h "${heuristic}" -"${dertiminism}" -"${solution}" -o history > ../outputs/demo/"${entry##*/}"__"${heuristic}"__"${dertiminism}"_"${solution}".txt
            done
        done
    done
done
