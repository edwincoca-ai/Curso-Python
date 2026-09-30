# ==========================================================
# RETO SEMANA 11 - FUNDAMENTOS DE PYTHON
# Varias listas: eliminar elementos repetidos en listas posteriores
# ==========================================================

import m_retosemanal as m


def main():
    print("========================================")
    print("     RETO SEMANA 11 - LISTAS")
    print("========================================\n")

    # Creamos la lista de listas
    listas = m.crear_listas()

    # Mostramos las originales
    m.imprimir_listas(listas, "LISTAS ORIGINALES")

    # Quitamos los elementos que estén en listas posteriores
    listas_filtradas = m.eliminar_repetidos(listas)

    # Mostramos el resultado
    m.imprimir_listas(
        listas_filtradas,
        "LISTAS SIN LOS ELEMENTOS QUE ESTABAN EN LISTAS POSTERIORES",
    )


if __name__ == "__main__":
    main()