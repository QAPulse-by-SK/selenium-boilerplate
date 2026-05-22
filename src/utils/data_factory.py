"""
QA Pulse by SK — Selenium Boilerplate
DataFactory — generates realistic test data using Faker
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional

from faker import Faker

fake = Faker()


@dataclass
class UserData:
    first_name: str
    last_name:  str
    email:      str
    username:   str
    password:   str
    phone:      str
    address:    str
    city:       str
    country:    str
    zip_code:   str


@dataclass
class ProductData:
    name:        str
    description: str
    price:       float
    sku:         str
    category:    str


@dataclass
class AddressData:
    street:   str
    city:     str
    state:    str
    zip_code: str
    country:  str


class DataFactory:
    """
    Generates realistic test data using Faker.

    Usage:
        user    = DataFactory.create_user()
        product = DataFactory.create_product()
        address = DataFactory.create_address()
    """

    @staticmethod
    def create_user(
        first_name: Optional[str] = None,
        last_name:  Optional[str] = None,
        email:      Optional[str] = None,
    ) -> UserData:
        """Create a realistic user with optional overrides."""
        fn = first_name or fake.first_name()
        ln = last_name  or fake.last_name()
        return UserData(
            first_name = fn,
            last_name  = ln,
            email      = email or fake.email(),
            username   = fake.user_name(),
            password   = fake.password(length=12, special_chars=True, digits=True, upper_case=True),
            phone      = fake.phone_number(),
            address    = fake.street_address(),
            city       = fake.city(),
            country    = fake.country(),
            zip_code   = fake.postcode(),
        )

    @staticmethod
    def create_product(category: Optional[str] = None) -> ProductData:
        """Create a realistic product."""
        return ProductData(
            name        = fake.catch_phrase(),
            description = fake.text(max_nb_chars=200),
            price       = round(fake.pyfloat(min_value=1, max_value=999, right_digits=2), 2),
            sku         = fake.bothify(text="SKU-####-???").upper(),
            category    = category or fake.word(),
        )

    @staticmethod
    def create_address() -> AddressData:
        """Create a realistic address."""
        return AddressData(
            street   = fake.street_address(),
            city     = fake.city(),
            state    = fake.state(),
            zip_code = fake.postcode(),
            country  = fake.country(),
        )

    @staticmethod
    def create_email(domain: str = "qapulse.dev") -> str:
        """Create a unique email with a specific domain."""
        return f"{fake.user_name()}.{fake.random_int(100, 999)}@{domain}"

    @staticmethod
    def random_string(length: int = 8) -> str:
        """Generate a random alphanumeric string."""
        return fake.bothify("?" * length, letters="abcdefghijklmnopqrstuvwxyz0123456789")

    @staticmethod
    def random_number(min_val: int = 1, max_val: int = 9999) -> int:
        """Generate a random integer."""
        return fake.random_int(min=min_val, max=max_val)

    @staticmethod
    def random_price(min_val: float = 1.0, max_val: float = 999.0) -> float:
        """Generate a random price."""
        return round(fake.pyfloat(min_value=min_val, max_value=max_val, right_digits=2), 2)
