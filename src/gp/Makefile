# User must set the following environment variables:
# QUESO_DIR
# GSL_INC
# BOOST_INC

all: gp

OBJECTS  =
OBJECTS += likelihood.o
OBJECTS += gp.o

CPPFLAGS=-I$(GSL_INC) -I$(BOOST_INC) -I$(QUESO_DIR)/include
CXXFLAGS=-mt_mpi -O3 -std=c++11 -mkl -xCORE-AVX2 -axMIC-AVX512 -fopenmp
LDFLAGS=-mkl -L$(QUESO_DIR)/lib

gp: $(OBJECTS)
	mpicxx -cxx=icpc $(LDFLAGS) $^ -o $@ -lqueso

%.o: %.C
	mpicxx -cxx=icpc -c $(CXXFLAGS) $(CPPFLAGS) $< -o $@

.PHONY: clean
clean:
	rm -f $(OBJECTS)
	rm -f gp
