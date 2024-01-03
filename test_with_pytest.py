import pytest
from Homework_27_pytest import Vehicle, ElectricVehicle


class TestVehicle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.car1 = Vehicle("BMW", "428xi", 'sport car')

    def test_vehicle_initialization(self):
        assert self.car1.brand == 'BMW'
        assert self.car1.model == '428xi'
        assert self.car1.type == 'sport car'
        assert self.car1.gas_tank_size == 14
        assert self.car1.fuel_level == 0

    def test_fuel_up(self):
        assert self.car1.fuel_up() == 'Gas tank is now full.'
        assert self.car1.fuel_level == 14

    def test_drive(self):
        assert self.car1.drive() == f'The {self.car1.model} is now driving.'


class TestElectricVehicle:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.e_car1 = ElectricVehicle("Tesla", "Model S", 'sedan')

    def test_electric_vehicle_initialization(self):
        assert self.e_car1.brand == 'Tesla'
        assert self.e_car1.model == 'Model S'
        assert self.e_car1.type == 'sedan'
        assert self.e_car1.battery_size == 85
        assert self.e_car1.charge_level == 0

    def test_charge(self):
        assert self.e_car1.charge() == 'The vehicle is now charged.'
        assert self.e_car1.charge_level == 100
