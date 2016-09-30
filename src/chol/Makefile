all: chol

chol: chol.C
	mpicxx -cxx=icpc -mkl -xCORE-AVX2 -axMIC-AVX512 $< -o $@

clean:
	rm chol
