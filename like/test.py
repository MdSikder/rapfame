import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {

    'platformName': 'Android',  # e.g., Android or iOS
    'platformVersion': '7.1.2',
    'deviceName': 'LDPlayer',
    'appPackage': "com.komspek.battleme",  # Replace with the actual app package name
    'appActivity': "com.komspek.battleme.presentation.feature.splash.PreloadActivity",  # Replace with the actual main activity
    'automationName': 'Appium',
    'noReset': True,
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# recent_header = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.ID, 'com.app.rapfame:id/recent_header_id'))
# )
# recent_header.click()
time.sleep(10)

for _ in range(10):
    # Assuming the elements of the posts are located by 'post_id'
    # post = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, 'com.app.rapfame:id/post_id'))
    # )

    # Perform a "like" action on the post
    like_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'com.app.rapfame:id/like_button_id'))
    )
    like_button.click()
    time.sleep(5)

    # You may need to add some delays to let the animation complete and ensure stability
    # For example: time.sleep(2)

    # Scroll to the next post
    action = TouchAction(driver)
    action.press(x=500, y=1600).move_to(x=500, y=200).release().perform()
    time.sleep(5)

driver.quit()
