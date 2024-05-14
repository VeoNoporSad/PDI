def main():
    # Definición de tabla_datos
    tabla_datos = {
        (3, 5): {10: 205, 12.5: 200, 20: 185, 25: 180, 40: 160, 50: 155, 70: 145, 150: 125},
        (8, 10): {10: 225, 12.5: 215, 20: 200, 25: 195, 40: 175, 50: 170, 70: 160, 150: 140},
        (15, 18): {10: 240, 12.5: 230, 20: 210, 25: 205, 40: 185, 50: 180, 70: 170, 150: '-'},
    }

    # Definición de tabla_agua_cemento
    tabla_agua_cemento = {
        450: 0.38,
        440: 0.39,
        430: 0.4,
        420: 0.41,
        410: 0.42,
        400: 0.43,
        390: 0.44,
        380: 0.45,
        370: 0.46,
        360: 0.47,
        350: 0.48,
        340: 0.49,
        330: 0.5,
        320: 0.51,
        310: 0.52,
        300: 0.55,
        290: 0.56,
        280: 0.57,
        270: 0.58,
        260: 0.59,
        250: 0.62,
        240: 0.63,
        230: 0.64,
        220: 0.65,
        210: 0.66,
        200: 0.7,
        190: 0.71,
        180: 0.72,
        170: 0.73,
        160: 0.74,
        150: 0.8,
        140: 0.81,
        130: 0.82,
        120: 0.83,
        110: 0.84
    }

    # Solicitar los datos al usuario
    tipo_hormigon = float(input("Tipo de hormigón (kg/cm^2): "))
    tamano_max_nominal = float(input("Tamaño máximo nominal (mm): "))
    revenimiento = float(input("Revenimiento (cm): "))
    peso_agua = float(input("Peso específico de agua (kg/m^3): "))
    peso_cemento = float(input("Peso específico de cemento (kg/m^3): "))
    peso_grava = float(input("Peso específico de grava (kg/m^3): "))
    PesoUnitarioGrava = float(input("Peso Unitario de grava (kg/m^3): "))
    peso_arena = float(input("Peso específico de arena (kg/m^3): "))
    PesoUnitarioArena = float(input("Peso Unitario de arena (kg/m^3): "))
    humedad_grava = float(input("% de humedad de grava: "))
    humedad_arena = float(input("% de humedad de arena: "))
    absorcion_grava = float(input("% de absorción de grava: "))
    absorcion_arena = float(input("% de absorción de arena: "))
    CantidadTotalDeHormigonEnM3 = float(input("Cantidad Total de hormigon: "))

    if (tamano_max_nominal == 10):
        PorcentajeDeAire = 3
    if (tamano_max_nominal == 12.5):
        PorcentajeDeAire = 2.5
    if (tamano_max_nominal == 20):
        PorcentajeDeAire = 2
    if (tamano_max_nominal == 25):
        PorcentajeDeAire = 1.5
    if (tamano_max_nominal == 40):
        PorcentajeDeAire = 1
    if (tamano_max_nominal == 50):
        PorcentajeDeAire = 0.5
    if (tamano_max_nominal == 70):
        PorcentajeDeAire = 0.3
    if (tamano_max_nominal == 150):
        PorcentajeDeAire = 0.2

    tipo_hormigon_m2 = tipo_hormigon * 10000
    print(f"Tipo de hormigón en kg/m²: {tipo_hormigon_m2}")

    # Buscar el dato en la tabla
    for rango_revenimiento, valores in tabla_datos.items():
        if rango_revenimiento[0] <= revenimiento <= rango_revenimiento[1]:
            if tamano_max_nominal in valores:
                AguaEnKgSobreM3 = valores[tamano_max_nominal]
                print(f"El dato correspondiente a un revenimiento de {revenimiento} cm y un TMN de {tamano_max_nominal} mm es: {AguaEnKgSobreM3}")
                break
    else:
        print("No se encontró un dato correspondiente en la tabla.")

    # Consultar valor de concreto sin aire incluido
    if tipo_hormigon in tabla_datos:
        concreto_sin_aire = tabla_datos[tipo_hormigon]
        print(f"El valor 'Concreto sin aire incluido' para una resistencia de {tipo_hormigon} kg/cm² es: {concreto_sin_aire}")
    else:
        print("No se encontró un valor correspondiente en la tabla para esa resistencia.")

    # Consultar relación agua/cemento
    if tipo_hormigon in tabla_agua_cemento:
        relacion_agua_cemento = tabla_agua_cemento[tipo_hormigon]
        print(f"La relación agua/cemento para una resistencia de {tipo_hormigon} kg/cm² es: {relacion_agua_cemento}")
    else:
        print("No se encontró un valor correspondiente en la tabla de agua/cemento para esa resistencia.")

    PesoCementoEnKg = AguaEnKgSobreM3/relacion_agua_cemento

    VolumenDelAguaEnM3 = AguaEnKgSobreM3/peso_agua

    GravaEnKg = PesoUnitarioGrava * 0.64
    PorcentajeDeArena = 1 - (AguaEnKgSobreM3/(peso_agua) + PorcentajeDeAire/100 + GravaEnKg/peso_grava + PesoCementoEnKg/peso_cemento)
    PesoArenaEnKg = PorcentajeDeArena * peso_arena
   
    PesoAguaEnKgCorregido = AguaEnKgSobreM3-(PesoArenaEnKg * ((humedad_arena - absorcion_arena)/100)+GravaEnKg*((humedad_grava - absorcion_grava)/100))

    VolumenAguaEnM3 = PesoAguaEnKgCorregido/peso_agua
    VolumenCementoEnM3 = PesoCementoEnKg/peso_cemento
    VolumenGravaEnM3 = GravaEnKg/peso_grava
    VolumenArenaEnM3 = PorcentajeDeArena
    PesoAguaHumedoEnKg = PesoAguaEnKgCorregido
    PesoCementoHumedoEnKg = PesoCementoEnKg
    PesoHumedoArenaEnKg = PesoArenaEnKg * (1 + humedad_arena/100)
    PesoHumedoGravaEnKg = GravaEnKg * (1 + humedad_grava/100)
    
    VolumenTotalAguaEnM3 = VolumenAguaEnM3 * CantidadTotalDeHormigonEnM3/100
    VolumenTotalCementoEnM3 = VolumenCementoEnM3 * CantidadTotalDeHormigonEnM3/100
    VolumenTotalGravaEnM3 = VolumenGravaEnM3 * CantidadTotalDeHormigonEnM3/100
    VolumenTotalArenaEnM3 = VolumenArenaEnM3 * CantidadTotalDeHormigonEnM3/100

    PesoTotalAguaEnM3 = AguaEnKgSobreM3 * VolumenAguaEnM3 / CantidadTotalDeHormigonEnM3
    PesoTotalCementoEnM3 = PesoCementoEnKg * VolumenCementoEnM3 / CantidadTotalDeHormigonEnM3
    PesoTotalGravaEnM3 = GravaEnKg * VolumenGravaEnM3 / CantidadTotalDeHormigonEnM3
    PesoTotalArenaEnM3 = PesoArenaEnKg * VolumenArenaEnM3 / CantidadTotalDeHormigonEnM3

    print("-------------Cantidad Total-------------")
    print(f"Volumen total de agua en m^3: {VolumenTotalAguaEnM3}")
    print(f"Volumen total de cemento en m^3: {VolumenTotalCementoEnM3}")
    print(f"Volumen total de grava en m^3: {VolumenTotalGravaEnM3}")
    print(f"Volumen total de arena en m^3: {VolumenTotalArenaEnM3}")

    print(f"Peso total de agua en m^3: {PesoTotalAguaEnM3}")
    print(f"Peso total de cemento en m^3: {PesoTotalCementoEnM3}")
    print(f"Peso total de grava en m^3: {PesoTotalGravaEnM3}")
    print(f"Peso total de arena en m^3: {PesoTotalArenaEnM3}")

    print("-------------Por peso(kg) para un m^3-------------")
    print(f"Agua en kg/m^3: {AguaEnKgSobreM3}")
    print(f"Cemento en kg/m^3: {PesoCementoEnKg}")
    print(f"Grava en kg/m^3: {GravaEnKg}")
    print(f"Arena en kg/m^3: {PesoArenaEnKg}")
    print(f"Agua húmeda en kg/m^3: {PesoAguaHumedoEnKg}")
    print(f"Cemento húmedo en kg/m^3: {PesoCementoHumedoEnKg}")
    print(f"Grava húmeda en kg/m^3: {PesoHumedoGravaEnKg}")
    print(f"Arena húmeda en kg/m^3: {PesoHumedoArenaEnKg}")


    print("-------------Por volumen en m^3-------------")
    print(f"Volumen de agua en m^3: {VolumenAguaEnM3}")
    print(f"Volumen de cemento en m^3: {VolumenCementoEnM3}")
    print(f"Volumen de grava en m^3: {VolumenGravaEnM3}")
    print(f"Volumen de arena en m^3: {VolumenArenaEnM3}")


if __name__ == "__main__":
    main()
