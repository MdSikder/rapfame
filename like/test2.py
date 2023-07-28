from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up desired capabilities for the Rap Fame app
desired_caps = {
    'platformName': 'Android',  # e.g., Android or iOS
    # 'platformVersion': 'Your_platform_version',
    'deviceName': 'LDPlayer',
    'appPackage': 'com.app.rapfame',  # Replace with the actual app package name
    'appActivity': 'com.app.rapfame.MainActivity',  # Replace with the actual main activity
    'automationName': 'uiautomator2'  # or 'XCUITest' for iOS
}

# Create the driver instance and launch the app
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Wait for the app to load and navigate to the recently released music page
try:
    # Assuming the 'Recently Released Music' button is located by 'recently_released_music_button_id'
    recently_released_music_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'com.app.rapfame:id/recently_released_music_button_id'))
    )
    recently_released_music_button.click()

    # Wait for the recently released music page to load
    time.sleep(2)

    # Function to like a post and scroll down to the next post
    def like_and_scroll():
        # Assuming the 'Like' button is located by 'like_button_id'
        like_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.app.rapfame:id/like_button_id'))
        )
        like_button.click()

        # Scroll down to the next post
        action = TouchAction(driver)
        action.press(x=500, y=1600).move_to(x=500, y=200).release().perform()

    # Play song and like the first post
    like_and_scroll()

    # Repeat for 9 more posts (total 10 posts)
    for _ in range(9):
        # Assuming the 'Play' button is located by 'play_button_id'
        play_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.app.rapfame:id/play_button_id'))
        )
        play_button.click()

        # Give the song some time to play
        time.sleep(5)

        # Like the post and scroll down
        like_and_scroll()

finally:
    # Close the app and end the driver session
    driver.quit()
