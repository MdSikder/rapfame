import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {

    'platformName': 'Android',  # e.g., Android or iOS
    'platformVersion': '7.1.2',
    'deviceName': 'LDPlayer',
    'appPackage': "com.komspek.battleme",  # Replace with the actual app package name
    'appActivity': "com.komspek.battleme.presentation.feature.splash.PreloadActivity",
    # Replace with the actual main activity
    'automationName': 'Appium',
    'noReset': True,
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(15)

# TouchAction(driver).press(x=505, y=1714).move_to(x=530, y=696).release().perform()


# try:
#     # Perform actions in the app to bring focus to an element, if needed
#
#     # Simulate pressing the "Tab" key on the keyboard
#     driver.press_keycode(61)
#
#     # Wait for some time to observe the effect (you can adjust this time as needed)
#     time.sleep(7)
#
# except Exception as e:
#     print(f"An error occurred: {e}")


try:
    recent_header = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '//android.widget.LinearLayout[@content-desc="Recent"]/android.widget.TextView'))
    )
    recent_header.click()
    time.sleep(5)
except NoSuchElementException as e:
    print("NoSuchElementException error :\n", e, "\n")

for _ in range(40):
    try:
        play = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, 'com.komspek.battleme:id/ivAvatar'))
        )
        play.click()
        time.sleep(15)

        # Perform a "like" action on the post
        like_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.komspek.battleme:id/ivVoteOne'))
        )
        like_button.click()
    except NoSuchElementException as e:
        print("NoSuchElementException error :\n", e, "\n")

        TouchAction(driver).press(x=530, y=696).move_to(x=530, y=790).release().perform()
        time.sleep(3)

    else:
        TouchAction(driver).press(x=530, y=696).move_to(x=530, y=750).release().perform()
        time.sleep(3)

driver.quit()
#
# # Scroll to the next post
# # action = TouchAction(driver)
# # action.press(x=500, y=1600).move_to(x=500, y=200).release().perform()
#
#
# driver.quit()
