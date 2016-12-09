# User must set the following environment variables:
# QUESO_DIR
# GSL_INC
# BOOST_INC

all: gp

OBJECTS  =
OBJECTS += likelihood.o
OBJECTS += gp.o

gp: $(OBJECTS)
	mpicxx -cxx=icpc -std=c++11 -mkl -L$(QUESO_DIR)/lib $^ -o $@ -lqueso

%.o: %.C
	mpicxx -cxx=icpc -c -std=c++11 -mkl -xCORE-AVX2 -axMIC-AVX512 -I$(GSL_INC) -I$(BOOST_INC) -I$(QUESO_DIR)/include $< -o $@

.PHONY: clean
clean:
	rm -f $(OBJECTS)
	rm -f gp
