import os
from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List


class CustomError(Exception):
    def __init__(self, random_value, msg: str = "Error 404"):
        self.random = random_value
        self.message = msg
        super().__init__(msg)


class Role(Enum):
    """ Accepted Node Types """
    CEO = auto()
    WORKER = auto()


@dataclass
class Employee(ABC):

    name: str
    role: Role

    @abstractmethod
    def pay(self) -> None:
        """ Pay day"""


@dataclass
class HourlyEmployee(Employee):

    hourly_rate_dollars: float = 25
    hours_worked: int = 10

    def __repr__(self):
        """
        Define repr to get a custom class representation

        Without repr:
            HourlyEmployee(name='Tim', role=<Role.WORKER: 2>, hourly_rate_dollars=25, hours_worked=10)

        With repr:
            Tim [HOURLY]: 10 @ $25



        """
        return f"{self.name} [hourly]: {self.hours_worked} @ ${self.hourly_rate_dollars}"

    def pay(self) -> None:
        """ Pay day"""
        print(
            f"Paying {self.name} an hourly rate of ${self.hourly_rate_dollars} for {self.hours_worked} hours."
        )


@dataclass
class SalariedEmployee(Employee):

    monthly_salary: float = 5000

    def pay(self) -> None:
        """ Pay day"""
        print(
            f"Paying {self.name} a monthly salary of ${self.monthly_salary}."
        )


class Company:
    def __init__(self):
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def find_employee_by_role(self, role) -> List[Employee]:
        return [employee for employee in self.employees if employee.role is role]


# class BaseNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


if __name__ == "__main__":
    company = Company()

    company.add_employee(HourlyEmployee(name="Tim", role=Role.WORKER))
    company.add_employee(SalariedEmployee(name="Jesus", role=Role.WORKER))
    company.add_employee(SalariedEmployee(name="Susana", role=Role.CEO))

    print(company.find_employee_by_role(Role.WORKER))

    for employee in company.employees:
        employee.pay()

    # raise CustomError("Does this serve any purpose", "This is a random msg")
