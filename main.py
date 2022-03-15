from msilib.schema import ODBCAttribute


class Planet:
    def __init__(self, name : str, size : int) -> None:
        self.name = name
        self.size = size
        self.moons = []
    
    def get_name(self):
        return self.name
    def get_size(self):
        return self.size
    def get_moons(self):
        return self.moons
    def add_moon(self, moon):
        self.moons.append(moon)
        
    def print_moons(self):
        for moon in self.moons:
            print(moon.get_name())
            
    def certain_size(self, size : int):
        print(f"The following moons around {self.get_name()} larger than {size} sqkm:")
        for moon in self.moons:
            if moon.get_size() > size:
                print(moon.get_name())


class Moon:
    def __init__(self, name : str, size: int):
        self.name = name
        self.size = size
        self.orbits = None

    def get_name(self):
        return self.name
    def get_size(self):
        return self.size
    def get_orbits(self):
        return self.orbits
    
    def add_orbit(self, orbit):
        self.orbits = orbit
    
def main():
    tellus = Planet("Tellus", 5.101e8)
    mars = Planet("Mars", 1.44e8)
    jupiter = Planet("Jupiter", 6.142e10)
    
    luna = Moon("Luna", 1.46e7)
    phobos = Moon("Phobos", 1.55e3)
    deimos = Moon("Deimos", 495)
    europa = Moon("Europa", 3.09e7)
    io = Moon("Io", 4.19e7)
    
    tellus.add_moon(luna)
    mars.add_moon(phobos)
    mars.add_moon(deimos)
    jupiter.add_moon(europa)
    jupiter.add_moon(io)
    
    luna.add_orbit(tellus)
    phobos.add_orbit(mars)
    deimos.add_orbit(mars)
    europa.add_orbit(jupiter)
    io.add_orbit(jupiter)
    
    tellus.print_moons()
    jupiter.print_moons()
    
    mars.certain_size(1000)
    
if __name__ == "__main__":
    main()