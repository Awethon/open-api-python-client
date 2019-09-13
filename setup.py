# coding: utf-8

from setuptools import setup, find_packages

NAME = "openapi-client-wrapper"
VERSION = "1.0.0"

REQUIRES = [
    "websocket_client==0.56.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="OpenAPI Wrapper",
    author_email="a.polovinkin@tinkoff.ru",
    url="",
    keywords=["Swagger", "OpenAPI", "Wrapper"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True
)
