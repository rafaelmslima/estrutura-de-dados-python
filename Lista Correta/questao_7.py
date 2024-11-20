def torre_hanoi_recursivo(discos,torre_origem,torre_destino, torre_auxiliar):
    if discos == 1:
        print(f"Mova o disco de {torre_origem} para {torre_destino}")
        return
    torre_hanoi_recursivo(discos - 1, torre_origem, torre_auxiliar, torre_destino)
    print(f"Mova o disco {discos} de {torre_origem} para {torre_destino}")
    torre_hanoi_recursivo(discos - 1, torre_origem, torre_auxiliar, torre_destino)

torre_hanoi_recursivo(1000, 'A', 'B', 'C')