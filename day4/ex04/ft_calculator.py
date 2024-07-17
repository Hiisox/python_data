class calculator:
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        i = 0
        for x in range(len(V1)):
            i = i + V1[x] * V2[x]
        print(f"Dot product is: {i}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        V3 = [float(V1[x] + V2[x]) for x in range(len(V1))]
        print(f"Add Vector is : {V3}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        V3 = [float(V1[x] - V2[x]) for x in range(len(V1))]
        print(f"Sous Vector is : {V3}")
