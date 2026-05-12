# ── PUNTO 1 ────────────────────────────────────────────────────────────────
temperaturas = [22, -1, 30, -3, 28, 25, -1, 19, 31, -2, 27]

def filtrar_validas(temperaturas):
    validas = []
    for t in temperaturas:
        if t >= 0:
            validas.append(t)
    return validas

def clasificar_clima(validas):
    total = 0
    for t in validas:
        total += t

    #prom = sum(validas) / len(validas)
    prom = total / len(validas)

    if prom < 15:
        return "Frío"
    elif prom < 28:
        return "Templado"
    else:
        return "Caluroso"

print(clasificar_clima(filtrar_validas(temperaturas)))
# validas = [22, 30, 28, 25, 19, 31, 27]
# prom = 26.0 → "Templado"


# ── PUNTO 2 ────────────────────────────────────────────────────────────────
fahrenheit = [150, 200, 160, 230, 140, 210, 175, 220, 155, 190]

def convertir_a_celsius(fahrenheit):
    celsius = []
    for f in fahrenheit:
        celsius.append((f - 32) * 5/9)
    return celsius

def diagnosticar_sistema(celsius):
    criticas = []
    for c in celsius:
        if c > 80:
            criticas.append(True)
        else:
            criticas.append(False)
    n = criticas.count(True)
    if n == 0:
        return "Sistema estable"
    elif n <= 3:
        return "Alerta temprana"
    else:
        return "Sistema recalentado"

print(diagnosticar_sistema(convertir_a_celsius(fahrenheit)))
# celsius ≈ [65.6, 93.3, 71.1, 110.0, 60.0, 98.9, 79.4, 104.4, 68.3, 87.8]
# criticas = [F, T, F, T, F, T, F, T, F, T]
# count(True) = 5 → "Sistema recalentado"


# ── PUNTO 3 ────────────────────────────────────────────────────────────────
alumnos = [("Ana", 9.5), ("Luis", 6.0), ("Mia", 3.8), ("Pedro", 7.2),
           ("Sara", 5.1), ("Juan", 4.0), ("Lina", 8.8), ("Tomas", 6.5)]

def generar_categorias(alumnos):
    categorias = []
    for nombre, nota in alumnos:
        if nota >= 6:
            categorias.append("Aprobado")
        else:
            categorias.append("Desaprobado")
    return categorias

def diagnosticar_grupo(categorias):
    aprobados    = categorias.count("Aprobado")
    desaprobados = categorias.count("Desaprobado")
    if aprobados > desaprobados:
        return "Grupo mayormente aprobado"
    elif aprobados == desaprobados:
        return "Grupo dividido"
    else:
        return "Grupo mayormente desaprobado"

print(diagnosticar_grupo(generar_categorias(alumnos)))
# categorias = ["Aprobado", "Aprobado", "Desaprobado", "Aprobado",
#               "Desaprobado", "Desaprobado", "Aprobado", "Aprobado"]
# aprobados = 5, desaprobados = 3 → "Grupo mayormente aprobado"