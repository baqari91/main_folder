from abc import ABC, abstractmethod


# 1. Single Responsibility Principle
class WebDeveloper:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_salary(self):
        return self.salary


class DeveloperDatabase:
    def save_database(self, developer):
        return developer

    def remove_database(self, developer):
        return developer


class DeveloperPrinter:
    def print_developer_info(self, developer):
        print(f"firstname: {developer.name}")
        print(f"lastname: {developer.position}")
        print(f"salary per month: {developer.salary}")


# #2 The Open/Closed Principle
class SolaryCalculatorPerYear:
    bonus = 1.15

    def salary_calculated(self, developer):
        calculated = self.calculator_per_year(developer.salary)
        return f" developer:{developer.name}'s salary per year: {calculated} Gel"

    def calculator_per_year(self, salary: int):
        return salary * 12 * self.bonus


developer1 = WebDeveloper('Giorgi', 'back-end', 3000)
developer2 = WebDeveloper('levani', 'front-end', 2700)
print_developer = DeveloperPrinter()
solary_calculator = SolaryCalculatorPerYear()
print(solary_calculator.salary_calculated(developer1))
print_developer.print_developer_info(developer2)


# აქ მთავრდება ეს პროგრამა რომელიც მოიცავს პირველ და მეორე პრინციპს.


# 3 Liskov Substitution Principle
class ElectronicDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class ElectronicDeviceWithAudio(ElectronicDevice):
    def adjust_volume(self):
        pass


class Tv(ElectronicDevice):
    def turn_on(self):
        print('Turned on TV')

    def turn_off(self):
        print('Turned off TV')


class AudioSystem(ElectronicDeviceWithAudio):

    def turn_on(self):
        print('turned on audio system')

    def turn_off(self):
        print('Turned off audio system')

    def adjust_volume(self):
        print("Adjusting volume")


# დასასრული

# 4) Interface Segregation Principle (ISP)
class BasicMessagingInterface(ABC):
    @abstractmethod
    def send_message(self):
        pass

    @abstractmethod
    def receive_message(self):
        pass

    @abstractmethod
    def view_messages(self):
        pass

    @abstractmethod
    def delete_message(self):
        pass


class GroupChatInterface(BasicMessagingInterface):
    @abstractmethod
    def create_group(self):
        pass

    @abstractmethod
    def add_member_to_group(self):
        pass

    @abstractmethod
    def remove_member_from_group(self):
        pass

    @abstractmethod
    def list_group_members(self):
        pass


class BasicUser(BasicMessagingInterface):
    def send_message(self):
        print("User sent a message")

    def receive_message(self):
        print("User received a message")

    def view_messages(self):
        print("User viewed messages")

    def delete_message(self):
        print("User deleted a message")


class PowerUser(GroupChatInterface):
    def send_message(self):
        print("User sent a message")

    def receive_message(self):
        print("User received a message")

    def view_messages(self):
        print("User viewed messages")

    def delete_message(self):
        print("User deleted a message")

    def create_group(self):
        print("User created a group")

    def add_member_to_group(self):
        print("User added a member to the group")

    def remove_member_from_group(self):
        print("User removed a member from the group")

    def list_group_members(self):
        print("User listed group members")


# 5) Dependency Inversion Principle (DIP)
class PaymentGatewayInterface(ABC):
    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def verify_payment(self):
        pass


class OnlinePaymentProcessor(PaymentGatewayInterface):
    def process_payment(self):
        print("Processing online payment...")

    def verify_payment(self):
        print("Verifying online payment...")


class CashOnDeliveryProcessor(PaymentGatewayInterface):
    def process_payment(self):
        print("Processing cash on delivery payment...")

    def verify_payment(self):
        print("Verifying cash on delivery payment...")


class OrderProcessor:
    def __init__(self, payment_processor: PaymentGatewayInterface):
        self.payment_processor = payment_processor

    def process_order(self):
        self.payment_processor.process_payment()
        self.payment_processor.verify_payment()


online_processor = OnlinePaymentProcessor()
cash_on_delivery_processor = CashOnDeliveryProcessor()

order_processor_online_payment = OrderProcessor(online_processor)
order_processor_cash_on_delivery = OrderProcessor(cash_on_delivery_processor)

order_processor_online_payment.process_order()
order_processor_cash_on_delivery.process_order()
