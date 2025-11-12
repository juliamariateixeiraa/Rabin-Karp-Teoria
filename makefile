SRCDIR_C := src/c
BINDIR   := bin
SCRIPTSDIR := scripts

CC       := gcc

CFLAGS   := -O3 -Wall -std=c11

C_EXECUTABLE := $(BINDIR)/rabin_karp_c_exp

C_SOURCES := $(SRCDIR_C)/rabin_karp.c $(SCRIPTSDIR)/run_experiments_c.c

.PHONY: all clean run

all: $(C_EXECUTABLE)

$(BINDIR):
	@mkdir -p $(BINDIR)

$(C_EXECUTABLE): $(BINDIR) $(C_SOURCES)
	@echo "Compilando Rabin-Karp em C..."
	$(CC) $(CFLAGS) $(C_SOURCES) -o $@ -lm

run: all
	@echo "Executando todos os experimentos (Python e C)..."
	python3 $(SCRIPTSDIR)/run_experiments.py

clean:
	@echo "Limpando arquivos gerados..."
	@rm -f $(C_EXECUTABLE)
	@rm -rf $(BINDIR)
	@rm -f data/*.csv