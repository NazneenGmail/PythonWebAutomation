
import pytest
import os
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

from utilities.test_data import TestData
#
@pytest.fixture(params=["chrome","firefox","safari"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "safari":
        driver = webdriver.Safari()

    request.cls.driver = driver
    yield
    driver.close()

# 1st Step: Declare Variables For Setting Up LambdaTest
user_name = os.getenv("LT_UserName")
access_token = os.getenv("LT_AccessKey")
remote_url = "https://" + user_name + ":" + access_token + "@hub.lambdatest.com/wd/hub"

# 2nd Step: Define The Desired Capabilities (3 Caps)
chrome_caps = {
  "build"       : "1.0",
  "name"        : "LambdaTest Grid On Chrome",
  "platform"    : "Windows 10",
  "browserName" : "Chrome",
  "version"     : "latest"
  }

firefox_caps = {
  "build"         : "2.0",
  "name"          : "LambdaTest Grid On Firefox",
  "platform"      : "Windows 10",
  "browserName"   : "Firefox",
  "version"       : "latest"
}

#3rd Step: Connect To LambdaTest Using A Fixture & RemoteConnection
#, "firefox"
@pytest.fixture(params=["chrome"])
def driver_initialization(request):
  """
  Initialize Driver For Selenium Grid On LambdaTest
  :param request:
  """
  desired_caps = {}
  chromeOptions = webdriver.ChromeOptions()
  chromeOptions.browser_version = "130"
  lt_options = {}
  lt_options["username"] = user_name
  lt_options["accessKey"] = access_token
  lt_options["name"] = "selenium-pytest-101-basic"
  lt_options["platformName"] = "Windows 10"
  lt_options["w3c"] = True
  lt_options["plugin"] = "python-pytest"
  lt_options["video"] = True
  lt_options["resolution"] = "1920x1080"
  lt_options["network"] = True
  lt_options["build"] = "Test build 1"
  lt_options["project"] = "project 1"
  lt_options["smartUI.project"] = "test"
  chromeOptions.set_capability('LT:Options', lt_options)

  firefoxOptiions = webdriver.FirefoxOptions()

  if request.param == "chrome":
    desired_caps.update(chrome_caps)
    driver = webdriver.Remote(
        command_executor=RemoteConnection(remote_url),
        options=chromeOptions
    )

  # elif request.param == "firefox":
  #   desired_caps.update(firefox_caps)
  #   driver = webdriver.Remote(
  #       command_executor=RemoteConnection(remote_url),
  #       options=firefoxOptiions
  #   )

  request.cls.driver = driver
  yield
  driver.close()
