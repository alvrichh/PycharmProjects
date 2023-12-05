def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): Peso de la persona en kilogramos.
        altura (float): Altura de la persona en metros.

    Returns:
        float: El IMC calculado.

    Raises:
        ValueError: Si el peso o la altura son menores o iguales a cero.
    """
    if peso <= 0:
        raise ValueError(f"El peso {peso} no es válido.")
    elif altura <=0:
        raise ValueError(f"La altura {altura} no es válida.")
    else:
        imc = peso / (altura**2)
        if imc < 18.5:
            mensaje = "Bajo peso"
        elif 18.5 < imc < 24.9:
            mensaje = "Peso Normal"
        elif 25.0 < imc < 29.9:
            mensaje = "Sobrepeso"
        elif imc > 30.0:
            mensaje = "Obesidad"
        else:
            mensaje = ""

        print(f"IMC = {imc}, {mensaje}")
        return imc
