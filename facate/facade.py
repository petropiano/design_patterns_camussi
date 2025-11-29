class NoiseGate:
    def set_threshold(self, value):
        print(f"NoiseGate: Threshold definido para {value}dB.")

    def enable(self):
        print("NoiseGate: Ligado.")
      

class DistortionPedal:
    def set_gain(self, level):
        print(f"DistortionPedal: Ganho definido para {level}/10.")

    def set_tone(self, level):
        print(f"DistortionPedal: Tom ajustado para agudos em {level}/10.")

    def turn_on(self):
        print("DistortionPedal: Ligado.")
      

class Amplifier:
    def set_volume(self, level):
        print(f"Amplifier: Volume master no nível {level}.")

    def set_eq(self, bass, mid, treble):
        print(f"Amplifier: EQ ajustado - Graves: {bass}, Médios: {mid}, Agudos: {treble}.")
          
    def turn_on(self):
        print("Amplifier: Ligado")
      

class CabinetSimulator:
    def set_mic_position(self, position):
        print(f"CabinetSimulator: Microfone posicionado no {position} do cone.")
      

class GuitarRigFacade:
    def __init__(self):
        self.noise_gate = NoiseGate()
        self.pedal = DistortionPedal()
        self.amp = Amplifier()
        self.cab = CabinetSimulator()

    def activate_metal_tone(self):
        print("--- Preset: NU METAL ---")
        self.amp.turn_on()
        self.noise_gate.set_threshold(-40)
        self.noise_gate.enable()
        
        self.pedal.set_gain(9)
        self.pedal.set_tone(8)
        self.pedal.turn_on()
        
        self.amp.set_eq(bass=8, mid=3, treble=9)
        self.amp.set_volume(11)
        
        self.cab.set_mic_position("centro")
        print("--- Rig pronto. A aguardar input da guitarra ---")

  def activate_black_metal(self):
        print("\n--- Preset: TRUE NORWEGIAN BLACK METAL ---")
        self.amp.turn_on()
        
        self.noise_gate.set_threshold(-20) 
        self.noise_gate.enable()
        
        self.pedal.set_gain(10)
        self.pedal.set_tone(10) 
        self.pedal.turn_on()
        
        self.amp.set_eq(bass=4, mid=6, treble=10)
        self.amp.set_volume(10)
        
        self.cab.set_mic_position("borda do cone")
        print("--- Rig pronto. ---")

    def activate_death_metal(self):
        print("\n--- Preset: OLD SCHOOL DEATH METAL ---")
        self.amp.turn_on()
        
        self.noise_gate.set_threshold(-60) 
        self.noise_gate.enable()
        
        self.pedal.set_gain(10)
        self.pedal.set_tone(5) 
        self.pedal.turn_on()
        
        self.amp.set_eq(bass=10, mid=2, treble=8)
        self.amp.set_volume(11)
        
        self.cab.set_mic_position("centro")
        print("--- Rig pronto. ---")
      

    def shutdown(self):
        print("\n--- Rig Desligado---")
