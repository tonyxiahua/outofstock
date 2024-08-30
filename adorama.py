from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_adorama(search_query, output_file):
    driver = webdriver.Chrome()
    output_list = []
    try: 
        driver.get("https://www.adorama.com/l/Used/?sel=Condition_X")
        # Find the search input field using the appropriate locating strategy
        #search_input = driver.find_element(By.NAME, "searchinfo")
        #search_input.send_keys(search_query)
        # search_input.send_keys(Keys.RETURN)
        
        names = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "Products_title__ROEN5"))
        )
        notes = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "Products_usedItemNote__enJLb"))
        )
        prices = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "Products_price__ACYq_"))
        )        
        for name, note , price in zip(names, notes, prices):
            output_line = f"{name.text} -- {price.text}\n {note.text} \n"
            output_list.append(output_line)
        driver.find_element('xpath','//*[@id="mainContent"]/section/div[2]/div[4]/a[2]').click()
    except Exception as e:
        print("An error occurred:", e)
    finally:
        time.sleep(5)
        driver.quit()
        
    print(output_list)
    #with open(output_file, "w") as file:
        #file.write(output_list)

if __name__ == "__main__":
    search_query = ""
    output_file = "Adorama_Query.txt"
    scrape_adorama(search_query, output_file)