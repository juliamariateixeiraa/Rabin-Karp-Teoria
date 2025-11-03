# src/python/rabin_karp.py

class RabinKarp:
    """Implementação do algoritmo Rabin-Karp para String Matching."""

    # Q (módulo): Um primo grande para evitar colisões
    Q = 1000000007 
    # D (base/radix): 256 para alfabeto ASCII
    D = 256         

    def search(self, text: str, pattern: str) -> list:
        """
        Executa a busca do padrão no texto usando Rabin-Karp (Rolling Hash).
        """
        N = len(text)
        M = len(pattern)
        results = []

        if M == 0 or N == 0 or M > N:
            return results

        p_hash = 0  
        t_hash = 0  
        H = 1       # H = D^(M-1) % Q 

        # 1. Pré-cálculo de H
        for i in range(M - 1):
            H = (H * self.D) % self.Q

        # 2. Pré-processamento: Calcular os hashes iniciais
        for i in range(M):
            p_hash = (self.D * p_hash + ord(pattern[i])) % self.Q
            t_hash = (self.D * t_hash + ord(text[i])) % self.Q

        # 3. Busca e Rolling Hash
        for i in range(N - M + 1):
            # A. Verificação de Colisão/Match
            if p_hash == t_hash:
                # O hash bateu. Necessário fazer a verificação caractere por caractere.
                if text[i:i + M] == pattern:
                    results.append(i)

            # B. Cálculo do próximo hash (Rolling Hash)
            if i < N - M:
                # Remove o caractere que sai da janela
                t_hash = (t_hash - ord(text[i]) * H) % self.Q
                
                # Adiciona o novo caractere na janela
                t_hash = (t_hash * self.D + ord(text[i + M])) % self.Q

                # Garante que o hash não seja negativo
                if t_hash < 0:
                    t_hash += self.Q

        return results