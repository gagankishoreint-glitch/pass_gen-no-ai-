#rolling-dice animation

#!/bin/bash

output=("⚀" "⚁" "⚂" "⚃" "⚄" "⚅")

for i in {1..10}
do 
    roll=$(( RANDOM % 6 ))
    printf "\r....rolling-wobbling....  ${output[$roll]}"
    sleep 0.8
done

#result=$((RANDOM % 6 + 1))
#printf "\rFinal Roll: ${faces[$((result-1))]} ($result)\n"
# this is just the animation alg works on smg else 
