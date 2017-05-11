#!/bin/bash
set -eu
set -o pipefail
set -x

./gp   1 queso_input_1.txt 40000
./gp   2 queso_input_1.txt 40000
./gp   4 queso_input_1.txt 40000
./gp   8 queso_input_1.txt 40000
./gp  12 queso_input_1.txt 40000
./gp  16 queso_input_1.txt 40000
./gp  20 queso_input_1.txt 40000
./gp  24 queso_input_1.txt 40000
./gp  28 queso_input_1.txt 40000
./gp  32 queso_input_1.txt 40000
./gp  36 queso_input_1.txt 40000
./gp  40 queso_input_1.txt 40000
./gp  44 queso_input_1.txt 40000
./gp  48 queso_input_1.txt 40000
