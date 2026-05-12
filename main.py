def calcular_imc(peso, altura):
    return peso / altura ** 2

def calcular_imc(peso: float, altura: float) -> float:
    return peso / altura ** 2

private float CalcularImc(float peso, float altura) {
    return peso / (altura * altura);
}
def celsius_a_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32
temps_c = [0, 20, 37, 100]


temps_f = [celsius_a_fahrenheit(t) for t in temps_c]
print(temps_f)

    

+