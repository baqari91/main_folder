from Homework_26_unitTest import Vehicle, ElectricVehicle
import unittest
# დასატესტ ფაილში პრინტები გადავაკეთე რეთარნებად

class TestVehicle(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.car1 = Vehicle("BMW", "428xi", 'sport car')

    def test_vehicle_initialization(self):
        self.assertEqual(self.car1.brand, 'BMW')
        self.assertEqual(self.car1.model, '428xi')
        self.assertEqual(self.car1.type, 'sport car')
        self.assertEqual(self.car1.gas_tank_size, 14)
        self.assertEqual(self.car1.fuel_level,0)
    def test_fuel_up(self):
        self.assertEqual(self.car1.fuel_up(), 'Gas tank is now full.')
        self.assertEqual(self.car1.fuel_level, 14)

    def test_drive(self):
        self.assertEqual(self.car1.drive(), f'The {self.car1.model} is now driving.')

    class TestElectricVehicle(unittest.TestCase):
        def setUp(self):
            print("setUp")
            self.e_car1 = ElectricVehicle("Tesla", "Model S", 'sedan')

        def test_electric_vehicle_initialization(self):
            self.assertEqual(self.e_car1.brand, 'Tesla')
            self.assertEqual(self.e_car1.model, 'Model S')
            self.assertEqual(self.e_car1.type, 'sedan')
            self.assertEqual(self.e_car1.battery_size, 85)
            self.assertEqual(self.e_car1.charge_level, 0)

        def test_charge(self):
            self.assertEqual(self.e_car1.charge_level, 100)
            self.assertEqual(self.e_car1.charge(), 'The vehicle is now charged.')

        def test_fuel_up(self):
            self.assertEqual(self.e_car1.fuel_up(), 'This vehicle has no fuel tank!')


if __name__ == '__main__':
    unittest.main()

