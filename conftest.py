import pytest
import requests
import allure
import pymysql


@pytest.fixture(scope="Session")
def connect_to_db():
    with allure.step("Get connect to DB"):
        pass




