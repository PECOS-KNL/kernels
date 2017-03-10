#!/bin/bash
set -eu
set -o pipefail
set -x

# Uses only DDR
numactl --membind=0 ./gp   1 queso_input_1.txt 40000
numactl --membind=0 ./gp   2 queso_input_1.txt 40000
numactl --membind=0 ./gp   4 queso_input_1.txt 40000
numactl --membind=0 ./gp   8 queso_input_1.txt 40000
numactl --membind=0 ./gp  16 queso_input_1.txt 40000
numactl --membind=0 ./gp  32 queso_input_1.txt 40000
numactl --membind=0 ./gp  64 queso_input_1.txt 40000
numactl --membind=0 ./gp 128 queso_input_1.txt 40000
numactl --membind=0 ./gp 256 queso_input_1.txt 40000
