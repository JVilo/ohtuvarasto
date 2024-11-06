from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

    print(f"Olutvarasto: {olutta}")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


if __name__ == "__main__":
    main()
