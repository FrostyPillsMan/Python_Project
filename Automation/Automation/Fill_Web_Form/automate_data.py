from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd


chrome_driver_path = "C:\\Users\\User\\Desktop\\chromedriver.exe"
chrome_service: Service = Service(executable_path=chrome_driver_path)
website = "https://forms.gle/RqwqKryRWkpjn5in8"
driver = webdriver.Chrome(service=chrome_service)

df = pd.read_csv("fake_data.csv")

for i in range(0, len(df)):
    driver.get(website)
    time.sleep(3)
    for column in df.columns:
        text_input = driver.find_element(
            by="xpath",
            value=f"//div[contains(@data-params, '{column}')]//input |"
            f"//div[contains(@data-params, '{column}')]//textarea",
        )
        text_input.send_keys(df.loc[i, column])
    submit_button = driver.find_element(
        by="xpath", value="//div[@role='button']//span[text()='Submit']"
    )
    submit_button.click()

driver.quit()



