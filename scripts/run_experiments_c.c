#define _POSIX_C_SOURCE 199309L
#define MAX_TEXT_SIZE 500001

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "../src/c/rabin_karp.h"


int main(int argc, char *argv[]) {
    if (argc != 2) { 
        fprintf(stderr, "Uso: %s <padrao>\n", argv[0]);
        return 1;
    }

    static char text[MAX_TEXT_SIZE];

    if (fgets(text, MAX_TEXT_SIZE, stdin) == NULL) {
        fprintf(stderr, "Erro ao ler o texto (stdin).\n");
        return 1;
    }

    text[strcspn(text, "\n")] = 0; 

    //parsind do padrao
    const char *pattern = argv[1];
    long N = strlen(text);
    long M = strlen(pattern);

    // timing
    struct timespec start, end;
    long long time_ns; 

    clock_gettime(CLOCK_MONOTONIC, &start);
    rabin_karp_search(text, N, pattern, M);
    clock_gettime(CLOCK_MONOTONIC, &end);

    time_ns = (end.tv_sec - start.tv_sec) * 1000000000LL + (end.tv_nsec - start.tv_nsec);
    double execution_time = (double)time_ns / 1000000000.0;

    printf("%.12f\n", execution_time); 

    return 0;
}