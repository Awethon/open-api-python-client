# coding: utf-8

from setuptools import setup, find_packages

NAME = "tinkoff-invest-openapi-client"
VERSION = "1.0.0"

REQUIRES = [
    "websocket_client==0.56.0",
    "certifi >= 14.05.14",
    "six >= 1.10",
    "python_dateutil >= 2.5.3",
    "setuptools >= 21.0.0",
    "urllib3 >= 1.15.1"
]

setup(
    name=NAME,
    version=VERSION,
    description="Tinkoff Invest OpenAPI Сlient",
    author_email="a.polovinkin@tinkoff.ru",
    url="",
    keywords=["Swagger", "OpenAPI", "Tinkoff"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True
)
