class Name:
    def __init__(self, name) -> None:
        if name not in ["Богдан", "Nazar"]:
            raise ValueError("Дозволені імена: Богдан, Nazar")
        self.name = name

a = Name("Ладик")