#!/bin/bash
set -eu
set -o pipefail
set -x

./gp   1 queso_input_1.txt 40000
./gp   2 queso_input_1.txt 40000
./gp   4 queso_input_1.txt 40000
./gp   8 queso_input_1.txt 40000
./gp  16 queso_input_1.txt 40000
./gp  32 queso_input_1.txt 40000
./gp  64 queso_input_1.txt 40000
./gp 128 queso_input_1.txt 40000
./gp 256 queso_input_1.txt 40000
