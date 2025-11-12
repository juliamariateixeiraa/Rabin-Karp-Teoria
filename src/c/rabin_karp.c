#include "rabin_karp.h"
#include <stdio.h>
#include <string.h>
#include <math.h>

void rabin_karp_search(const char *text, long N, const char *pattern, long M) {
    if (M == 0 || N == 0 || M > N) {
        return;
    }

    long long p_hash = 0;
    long long t_hash = 0;
    long long H = 1;

    for (int i = 0; i < M - 1; i++) {
        H = (H * D) % Q;
    }

    // calcula os hashes iniciais
    for (int i = 0; i < M; i++) {
        p_hash = (D * p_hash + pattern[i]) % Q;
        t_hash = (D * t_hash + text[i]) % Q;
    }

    // busca e rolling hash
    for (int i = 0; i <= N - M; i++) {
        // verifica a  colisão/match
        if (p_hash == t_hash) {
            int j;
            for (j = 0; j < M; j++) {
                if (text[i + j] != pattern[j]) {
                    break;
                }
            }
            if (j == M) {
            }
        }

        // calcular o próximo hash
        if (i < N - M) {
            t_hash = (t_hash - (text[i] * H) % Q + Q) % Q;
            t_hash = (t_hash * D + text[i + M]) % Q;
        }
    }
}