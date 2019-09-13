# coding: utf-8

"""
    OpenAPI

    tinkoff.ru/invest OpenAPI.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: n.v.melnikov@tinkoff.ru
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "openapi-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="OpenAPI",
    author_email="n.v.melnikov@tinkoff.ru",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "OpenAPI"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    tinkoff.ru/invest OpenAPI.  # noqa: E501
    """
)
