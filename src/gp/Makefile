# User must set the following environment variables:
# QUESO_DIR
# GSL_INC
# BOOST_INC

all: gp test

OBJECTS  =
OBJECTS += likelihood.o
OBJECTS += gp.o
OBJECTS += test.o

CPPFLAGS=-I$(GSL_INC) -I$(BOOST_INC) -I$(QUESO_DIR)/include
CXXFLAGS=-mt_mpi -O3 -std=c++11 -mkl -xCORE-AVX2 -axMIC-AVX512 -fopenmp
LDFLAGS=-mkl -L$(QUESO_DIR)/lib

gp: gp.o likelihood.o
	mpicxx -cxx=icpc $(LDFLAGS) $^ -o $@ -lqueso

test: test.o likelihood.o
	mpicxx -cxx=icpc $(LDFLAGS) $^ -o $@ -lqueso

%.o: %.C
	mpicxx -cxx=icpc -c $(CXXFLAGS) $(CPPFLAGS) $< -o $@

.PHONY: clean
clean:
	rm -f $(OBJECTS)
	rm -f gp
	rm -f test
