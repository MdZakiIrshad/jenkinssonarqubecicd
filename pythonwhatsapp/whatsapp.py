from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def send_whatsapp_message(contact_name, message):
    # Set the path to your Chrome WebDriver
    webdriver_path = "/path/to/chromedriver"

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(executable_path=webdriver_path)

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    input("Please scan the QR code and press Enter after logging in.")

    try:
        # Locate the search box
        search_box = driver.find_element("xpath", '//div[@contenteditable="true"][@data-tab="3"]')

        # Search for the contact
        search_box.send_keys(contact_name)
        time.sleep(2)  # Wait for the search results to load
        search_box.send_keys(Keys.RETURN)

        # Locate the message input box
        message_box = driver.find_element("xpath", '//div[@contenteditable="true"][@data-tab="1"]')

        # Type and send the message
        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)

        print(f"Message sent to {contact_name}: {message}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser window
        driver.quit()

# Example usage
contact_name = "Contact Name"  # Replace with the name of your contact
message = "Hello, this is a test message sent using Selenium!"  # Replace with your message

send_whatsapp_message(contact_name, message)

