import time
import pytest


@pytest.mark.smoke
def test_sample_tc__3(setup):
    driver = setup['driver']
    time.sleep(5)
    driver.get("https://www.amazon.com/")
    print("*********tested************")
    time.sleep(5)
    driver.quit()
