import trio
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from devices import get_devices
from ports import get_ports
import time

# Define the emails list
emails = ["ryannguyen18032000@gmail.com", "ryannguyen1803@gmail.com"]

async def run_automation(device_id, email, port):
    desired_cap = {
        "uuid": device_id,  # device ID
        "platformName": "Android",
        "appPackage": "com.facebook.lite",  # adb shell dumpsys window | find "mCurrentFocus"
        "appActivity": "com.facebook.lite.MainActivity",  # adb shell dumpsys window | find "mCurrentFocus",
        "automationName": "UiAutomator2",
        "noReset": True
    }

    async with trio.open_nursery() as inner_nursery:
        async with trio.open_nursery() as nursery:
            driver = webdriver.Remote(f"http://127.0.0.1:{port}/wd/hub", desired_cap)
            driver.implicitly_wait(30)  # Wait until app appears
            await nursery.start(run_automation_task, driver, email)


async def run_automation_task(driver, email):
    try:
        await facebook_register_automation(driver, email)
    except Exception as e:
        print(f"Error: {e.with_traceback()}")
    finally:
        driver.quit()

async def facebook_register_automation(driver, email):
    delays = 10000
    wait = WebDriverWait(driver, delays)
    
    await get_notification(driver)
    
    register_button = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Create new account']")
    register_button.click()
    
    register_get_started_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Get started']/android.view.ViewGroup")
    register_get_started_button.click()

    first_name_selector = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText")))
    first_name_selector.click()
    first_name_selector.send_keys("Ryan")
    time.sleep(2)

    last_name_selector = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText")))
    last_name_selector.click()
    last_name_selector.send_keys("Nguyen")
    time.sleep(3)

    name_next_button = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Next']")
    name_next_button.click()

    birthday_year_picker = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[3]/android.widget.Button[1]")

    while birthday_year_picker.text != "2000":
        birthday_year_picker.click()

    set_button = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[2]")
    set_button.click()

    birthday_next_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Next']/android.view.ViewGroup")
    birthday_next_button.click()
    gender_option = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Male']/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView")
    gender_option.click()

    gender_next_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Next']/android.view.ViewGroup")
    gender_next_button.click()

    sign_up_email_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Sign up with email']/android.view.ViewGroup")
    sign_up_email_button.click()

    email_input = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText")
    email_input.clear()
    email_input.send_keys(email)

    email_next_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Next']/android.view.ViewGroup")
    email_next_button.click()
    time.sleep(5)

    password_input = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText")
    password_input.clear()
    password_input.send_keys("HoangLinh@1803")

    password_next_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Next']/android.view.ViewGroup")
    password_next_button.click()

    save_login_info_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Not now']/android.view.ViewGroup")
    save_login_info_button.click()

    agree_button = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='I agree']/android.view.ViewGroup")
    agree_button.click()

    contact_permission_deny = driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_deny_button")
    contact_permission_deny.click()

    logout_button = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.View[7]")
    logout_button.click()

    logout_confirm_button = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.View")
    logout_confirm_button.click()

async def get_notification(driver):
    while len(driver.find_elements(AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='Choose a Credential']/android.widget.LinearLayout/android.widget.Button")) > 0:
        driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='Choose a Credential']/android.widget.LinearLayout/android.widget.Button").click()
        if len(driver.find_elements(AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='Choose a Credential']/android.widget.LinearLayout/android.widget.Button")) == 0:
            break

async def main():
    devices = get_devices()
    ports = get_ports()
    
    if devices != []:
        async with trio.open_nursery() as nursery:
            if len(devices) > 0:
                if len(devices) == 1:
                    # Assign emails to the single device sequentially
                    for email in emails:
                        nursery.start_soon(run_automation, devices[0], email, ports[0])
                else:
                    # Pair each device with its corresponding email
                    for device_id, email, port in zip(devices, emails, ports):
                        nursery.start_soon(run_automation, device_id, email, port)
            else:
                print("No devices found.")

if __name__ == "__main__":
    trio.run(main)
