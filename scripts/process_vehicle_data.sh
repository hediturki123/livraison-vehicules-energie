#!/bin/bash

mkdir -p ../outputs
mkdir -p ../outputs/vehicle_data

if [[ -n $1 ]]; then
  instance_group=$1
  for charge_speed in "slow" "medium" "fast"; do
    charges_output_file="../outputs/vehicle_data/lyon_${instance_group}_${charge_speed}__charges.txt"
    vehicles_output_file="../outputs/vehicle_data/lyon_${instance_group}_${charge_speed}__vehicles.txt"
    cp /dev/null "$charges_output_file"
    cp /dev/null "$vehicles_output_file"
    echo "Calculating for 'lyon_${instance_group}' with $charge_speed charge speed..."
    for instance in "../data/instances/lyon_${instance_group}"*; do
      for heuristic in "swap" "insert" "triplet_shift"; do
        # Exécution d'une instance
        result=$(poetry run python ../src/__init__.py "${instance##*/}" -h "$heuristic" -s "$charge_speed")
        # Nombre de charges effectuées
        echo "$result" | wc -l | xargs >> "$charges_output_file"
        # Nombre de véhicules utilisés
        echo "$result" | grep -o "C" | wc -l | xargs >> "$vehicles_output_file"
      done
    done
    # Calcul du nombre de charges effectuées en moyenne
    awk '{s+=$1}END{print "\n",s/NR}' RS="\n" "$charges_output_file" >> "$charges_output_file"
    # Calcul du nombre de véhicules utilisés en moyenne
    awk '{s+=$1}END{print "\n",s/NR}' RS="\n" "$vehicles_output_file" >> "$vehicles_output_file"
  done
fi
echo "Done!"