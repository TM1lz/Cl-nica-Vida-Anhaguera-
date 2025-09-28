# acesso.py

def consulta_normal(A, B, C, D):
    # (A AND B AND C) OR (B AND C AND D)
    return (A and B and C) or (B and C and D)

def emergencia(A, B, C, D):
    # C AND (B OR D)
    return C and (B or D)
