import pytest
from selenium import webdriver
import re


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    return {
        'driver': driver
    }


# test_results = {}

#
# def pytest_runtest_protocol(item, nextitem):
#     print('********123******')
#     test_case_name = item.nodeid
#     match = re.search(r'__([\d]+)', test_case_name)
#     if match:
#         testcase_id = match.group(1)
#     else:
#         testcase_id = test_case_name
#
#     test_results[testcase_id] = None
#     return None
#
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_runtest_logreport(report):
#     print('** ** ** ** 456 ** ** **' )
#     test_case_name = report.nodeid
#     match = re.search(r'__([\d]+)', test_case_name)
#     if match:
#         testcase_id = match.group(1)
#     else:
#         testcase_id = test_case_name
#     if report.passed:
#         test_result = "Passed"
#     elif report.failed:
#         test_result = "Failed"
#     else:
#         test_result = "Skipped"
#
#     test_results[testcase_id] = test_result
#
#
# def pytest_sessionfinish(session, exitstatus):
#     print('** ** ** ** 789 ** ** **')
#     for testcase_id, test_result in test_results.items():
#         print(f"{testcase_id}:{test_result}")
