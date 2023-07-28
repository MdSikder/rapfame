from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.touch_actions import TouchActions



desired_caps = {
    'platformName': 'Android',
    'deviceName': 'LDPlayer',
    'appPackage': 'com.rap.fame',
    'appActivity': 'com.rap.fame.MainActivity',
    'automationName': 'Appium',
    'noReset': True,
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# recent_header = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.ID, 'com.app.rapfame:id/recent_header_id'))
# )
# recent_header.click()

for _ in range(10):
    # Assuming the elements of the posts are located by 'post_id'
    # post = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, 'com.app.rapfame:id/post_id'))
    # )
    #
    # # Perform a "like" action on the post
    # like_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, 'com.app.rapfame:id/like_button_id'))
    # )
    # like_button.click()

    # You may need to add some delays to let the animation complete and ensure stability
    # For example: time.sleep(2)

    # Scroll to the next post
    action = TouchAction(driver)
    action.press(x=500, y=1600).move_to(x=500, y=200).release().perform()

driver.quit()
