#!/bin/bash
set -eu
set -o pipefail
set -x

./test   1 queso_input_1.txt 20000
./test   2 queso_input_1.txt 20000
./test   4 queso_input_1.txt 20000
./test   8 queso_input_1.txt 20000
./test  16 queso_input_1.txt 20000
./test  32 queso_input_1.txt 20000
./test  64 queso_input_1.txt 20000
./test 128 queso_input_1.txt 20000
./test 256 queso_input_1.txt 20000
