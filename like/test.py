import time

from appium import webdriver
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





# driver.swipe(470, 1468, 800, 300, )
# time.sleep(5)

# Scroll to the next post
# action = TouchAction(driver)
# action.press(x=0, y=0).move_to(x=500, y=200).release().perform()
# time.sleep(5)


# try:
#     elements = driver.find_element(By.ID, "com.komspek.battleme:id/ivIcon")
#     # driver.find_elements(By.ID, "com.komspek.battleme:id/ivIcon").c()
#     elements.click()
#     # Check if the list is not empty and if the desired index exists
#     # if len(elements) >= 2:
#     #     second_element = elements[0]
#     #     # Now you can perform actions on the second_element
#     #     second_element.click()
#     #     time.sleep(5)
#     # else:
#     #     # Handle the case when there is no second element
#     #     print("There is no second element.")
#
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
try:
    recent_header = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '//android.widget.LinearLayout[@content-desc="Recent"]/android.widget.TextView'))
    )
    recent_header.click()
    time.sleep(10)
except NoSuchElementException as e:
    print("NoSuchElementException error :\n", e, "\n")

driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 150")
time.sleep(6)


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
