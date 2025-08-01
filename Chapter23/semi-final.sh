#!/usr/bin/env bash
RES_DIR=saves/challengers

extra=''

for round in `seq 0 0`; do
    echo Starting round $round
    if test $round -eq 9; then
        extra="$RES_DIR/best_1*"
    fi
    filename=$RES_DIR/best_$(printf "%02d" "$round")* 
    ./play.py --mps -r 100 $(echo $filename) $extra > tournament/semi-$round.txt &
done

echo "Waiting for them to finish"

for job in `jobs -p`; do
    echo $job
    wait $job || echo "Job $job failed"
done
