"""
QA Pulse by SK — Selenium Boilerplate
DataFactory — generates realistic test data using Faker.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

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
    """Factory for generating dynamic test data."""

    @staticmethod
    def create_user(
        username: Optional[str] = None,
        password: Optional[str] = None
    ) -> UserData:
        """Generate a random user."""
        return UserData(
            first_name = fake.first_name(),
            last_name  = fake.last_name(),
            email      = fake.email(),
            username   = username or fake.user_name(),
            password   = password or fake.password(length=12, special_chars=True),
            phone      = fake.phone_number(),
            address    = fake.street_address(),
            city       = fake.city(),
            country    = fake.country(),
        )

    @staticmethod
    def create_product() -> ProductData:
        """Generate a random product."""
        return ProductData(
            name        = fake.catch_phrase(),
            description = fake.text(max_nb_chars=200),
            price       = round(fake.pyfloat(min_value=1, max_value=999, right_digits=2), 2),
            sku         = fake.bothify("SKU-####-??").upper(),
            category    = fake.word().capitalize(),
        )

    @staticmethod
    def create_address() -> AddressData:
        """Generate a random address."""
        return AddressData(
            street   = fake.street_address(),
            city     = fake.city(),
            state    = fake.state(),
            zip_code = fake.postcode(),
            country  = fake.country(),
        )

    @staticmethod
    def random_email() -> str:
        return fake.email()

    @staticmethod
    def random_name() -> str:
        return fake.name()

    @staticmethod
    def random_phone() -> str:
        return fake.phone_number()

    @staticmethod
    def random_text(max_chars: int = 100) -> str:
        return fake.text(max_nb_chars=max_chars)

    @staticmethod
    def random_number(min_val: int = 1, max_val: int = 100) -> int:
        return fake.random_int(min=min_val, max=max_val)

    @staticmethod
    def random_price() -> float:
        return round(fake.pyfloat(min_value=1, max_value=999, right_digits=2), 2)
