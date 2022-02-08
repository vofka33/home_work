class Vobler:
    vobler_count = 0

    def start(self, brand, model, form, action, depth, size, mass, wiring):
        print("Добавлен")
        self.brand = brand
        self.model = model
        self.form = form
        self.action = action
        self.depth = depth
        self.size = size
        self.mass = mass
        self.wiring = wiring
        Vobler.vobler_count += 1

bite_60 = Vobler()
bite_60.stert('liberty', 'Byte 60', 'minnow', 'suspender', 'dr', 60, 6.72, 'twich')

print(vobler_count)
