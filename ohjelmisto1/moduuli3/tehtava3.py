sukupuoli = input("Biologinen sukupuoli: ")
hg_arvo = int(input("Hemoglobiiniarvo (g/l): "))

if sukupuoli.lower() == "nainen":
    if hg_arvo < 117:
        print("Sinulla on alhainen hemoglobiiniarvo")
    elif hg_arvo >= 117 and hg_arvo <= 175:
        print("Sinulla on normaali hemoglobiiniarvo")
    else:
        print("Sinulla on korkea hemoglobiiniarvo")

elif sukupuoli.lower() == "mies":
    if hg_arvo < 134:
        print("Sinulla on alhainen hemoglobiiniarvo")
    elif hg_arvo >= 134 and hg_arvo <= 195:
        print("Sinulla on normaali hemoglobiiniarvo")
    else:
        print("Sinulla on korkea hemoglobiiniarvo")