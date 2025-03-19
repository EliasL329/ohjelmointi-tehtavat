while True:
    tuuma = float(input("Tuumia: "))
    
    if tuuma < 0:
        break

    print(f"{tuuma} tuumaa on {tuuma * 2.56} senttimetriä")