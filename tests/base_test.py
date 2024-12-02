import pytest


# @pytest.mark.usefixtures("initialize_driver")
# class BaseTest:
#     pass

@pytest.mark.usefixtures("driver_initialization")
class BaseTest:
    pass
