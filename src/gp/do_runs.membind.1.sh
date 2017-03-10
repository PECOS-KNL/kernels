#!/bin/bash
set -eu
set -o pipefail
set -x

# Uses only HBM
numactl --membind=1 ./gp  16 queso_input_1.txt 40000
numactl --membind=1 ./gp  32 queso_input_1.txt 40000
numactl --membind=1 ./gp  64 queso_input_1.txt 40000
numactl --membind=1 ./gp 128 queso_input_1.txt 40000
numactl --membind=1 ./gp 256 queso_input_1.txt 40000
