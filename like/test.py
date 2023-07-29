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

try:
    # Perform actions to reach the initial state where "Tab" key needs to be pressed
    # (e.g., focus on an input field or a specific UI element)

    # Replace "target_element_id" with the actual ID or other locator of the target element
    target_element_locator = (MobileBy.ID, "com.komspek.battleme:id/ivAvatar")

    driver.press_keycode(61)
    time.sleep(3)
    # Loop until the target element becomes visible
    max_attempts = 10  # Adjust the maximum number of attempts as needed
    attempts = 0
    while attempts < max_attempts:
        # Press the "Tab" key on the keyboard
        driver.press_keycode(61)

        # Wait for a short period to allow the element to become visible
        time.sleep(5)  # Adjust the time as needed

        # Check if the target element is now visible
        target_element = driver.find_elements(*target_element_locator)
        if target_element:
            # Element found, exit the loop
            break
        # Increment the attempts counter
        attempts += 1

    # if not target_element:
    #     print("Target element not found after multiple attempts.")

    # Perform further actions with the visible target element

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the driver
    driver.quit()

# try:
#     # Perform actions in the app to bring focus to an element, if needed
#
#     # Simulate pressing the "Tab" key on the keyboard
#     driver.press_keycode(61)
#
#     # Wait for some time to observe the effect (you can adjust this time as needed)
#     time.sleep(7)
#
#
#     driver.press_keycode(61)
#
#     # Wait for some time to observe the effect (you can adjust this time as needed)
#     time.sleep(7)
#
#     # Perform further actions after pressing the "Tab" key
#
# except Exception as e:
#     print(f"An error occurred: {e}")

# driver.swipe(470, 1468, 800, 300, )
# time.sleep(5)

# Scroll to the next post
# action = TouchAction(driver)
# action.press(x=0, y=0).move_to(x=500, y=200).release().perform()
# time.sleep(5)


# try:
#     elements = driver.find_elements(By.ID, "com.komspek.battleme:id/ivPlay1")
#     # driver.find_elements(By.ID, "com.komspek.battleme:id/ivIcon").c()
#     # Check if the list is not empty and if the desired index exists
#     if len(elements) >= 2:
#         second_element = elements[0]
#         third_elemnt = elements[1]
#         scrollable_view = second_element
#         target_element = third_elemnt
#
#         driver.scroll(scrollable_view, target_element)
#         time.sleep(5)
#     else:
#         # Handle the case when there is no second element
#         print("There is no second element.")

# except NoSuchElementException as e:
#     print("NoSuchElementException error :\n", e, "\n")

# time.sleep(5)


# try:
#
#     categories = WebDriverWait(driver, 40).until(
#         EC.presence_of_element_located((By.ID, 'com.komspek.battleme:id/ivIcon').)
#     )
#     categories.click()
#     time.sleep(5)
#
# except NoSuchElementException as e:
#     print("NoSuchElementException error :\n", e, "\n")
#
# try:
#     recent_header = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located(
#             (By.XPATH, '//android.widget.LinearLayout[@content-desc="Recent"]/android.widget.TextView'))
#     )
#     recent_header.click()
#     time.sleep(5)
# except NoSuchElementException as e:
#     print("NoSuchElementException error :\n", e, "\n")

# action = TouchAction(driver)
# action.press(x=22, y=165).move_to(x=22, y=800).release().perform()
# time.sleep(5)

# try:
#     play = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located(
#             (By.ID, 'com.komspek.battleme:id/ivAvatar'))
#     )
#     play.click()
#     time.sleep(10)
# except NoSuchElementException as e:
#     print("NoSuchElementException error :\n", e, "\n")
#
#
# # driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 150")
# # time.sleep(4)
#
# # # Scroll down to the next post
# # action = TouchAction(driver)
# # action.press(x=500, y=1600).move_to(x=500, y=200).release().perform()
# # time.sleep(5)
#
#
#
# try:
#     # Perform a "like" action on the post
#     like_button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'com.komspek.battleme:id/ivVoteOne'))
#     )
#     like_button.click()
# except NoSuchElementException as e:
#     print("NoSuchElementException error :\n", e, "\n")
# time.sleep(5)
#
# action = TouchAction(driver)
# action.press(x=354, y=650).move_to(x=320, y=820).release().perform()
# time.sleep(5)

# #
# # Scroll down to the next post
# action = TouchAction(driver)
# action.press(x=500, y=1600).move_to(x=500, y=200).release().perform()
# time.sleep(5)
#
#
# try:
#     # Perform a "like" action on the post
#     like_button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'com.komspek.battleme:id/ivVoteOne'))
#     )
#     like_button.click()
# except NoSuchElementException as e:
#     print("NoSuchElementException error :\n", e, "\n")
# time.sleep(5)


# for _ in range(10):
# Assuming the elements of the posts are located by 'post_id'
# post = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.ImageView'))
# )
#     # time.sleep(3)
# try:
#     # Perform a "like" action on the post
#     like_button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ImageView'))
#     )
#     like_button.click()
# except NoSuchElementException as e:
#     print("NoSuchElementException error :\n", e, "\n")
#
# time.sleep(10)
# You may need to add some delays to let the animation complete and ensure stability
# For example: time.sleep(2)

# Scroll to the next post
# action = TouchAction(driver)
# action.press(x=500, y=1600).move_to(x=500, y=200).release().perform()


driver.quit()
