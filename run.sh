#!/bin/bash

python mptcp_test.py \
    --bw 1 \
    --queue 100 \
    --workload one_to_several \
    --topology ft10 \
    --time 60 \
    --iperf ~/iperf-patched/src/iperf \
    $qmon 

# plot RTT
python plot_ping.py -k 10 -w one_to_several -f results/ft10/one_to_several/*/client_ping* -o plots/ft10-one_to_several-rtt.png
# plot throughput
python plot_hist.py -k 10 -w one_to_several -t 60 -f results/ft10/one_to_several/*/client_iperf* results/ft10/one_to_several/max_throughput.txt -o plots/ft10-one_to_several-throughput.png
# plot link util
python plot_link_util.py -k 10 -w one_to_several -f results/ft10/one_to_several/*/link_util* -o plots/ft10-one_to_several-link_util.png


python mptcp_test.py \
    --bw 1 \
    --queue 100 \
    --workload sparse \
    --topology ft12 \
    --time 60 \
    --iperf ~/iperf-patched/src/iperf \
    $qmon 

# plot RTT
python plot_ping.py -k 12 -w sparse -f results/ft12/sparse/*/client_ping* -o plots/ft12-sparse-rtt.png
# plot throughput
python plot_hist.py -k 12 -w sparse -t 60 -f results/ft12/sparse/*/client_iperf* results/ft12/sparse/max_throughput.txt -o plots/ft12-sparse-throughput.png
# plot link util
python plot_link_util.py -k 12 -w sparse -f results/ft12/sparse/*/link_util* -o plots/ft12-sparse-link_util.png

python mptcp_test.py \
    --bw 1 \
    --queue 100 \
    --workload one_to_several \
    --topology ft12 \
    --time 60 \
    --iperf ~/iperf-patched/src/iperf \
    $qmon 

# plot RTT
python plot_ping.py -k 12 -w one_to_several -f results/ft12/one_to_several/*/client_ping* -o plots/ft12-one_to_several-rtt.png
# plot throughput
python plot_hist.py -k 12 -w one_to_several -t 60 -f results/ft12/one_to_several/*/client_iperf* results/ft12/one_to_several/max_throughput.txt -o plots/ft12-one_to_several-throughput.png
# plot link util
python plot_link_util.py -k 12 -w one_to_several -f results/ft12/one_to_several/*/link_util* -o plots/ft12-one_to_several-link_util.png


wl_to_run=('one_to_several' 'sparse')

for workload in ${wl_to_run[*]}
do
  # plot cpu utilization
  python plot_cpu.py -w $workload -f results/ft*/$workload/flows*/cpu_utilization.txt -o plots/cpu_util-$workload.png
done
