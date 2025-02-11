from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os
import requests
from collections import defaultdict
 
 
graph = defaultdict(list)
def create_graph(searcher_id, elements, n):
    """Create an adjacency list graph where all elements connect to searcher_id"""
    for i in range(min(n, len(elements))):
        graph[searcher_id].append(elements[i])
    return graph
 
# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 
# Open Coursea
driver.get("https://www.instagram.com/")
 
time.sleep(60)
# def reel_comments():
#     
#     wait = WebDriverWait(driver, 10)
#     driver.get("https://www.instagram.com/reels/")
#     time.sleep(5)
#     clickable_divs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xw7yly9.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1')))
 
#     # Click all div elements with style="cursor: pointer;" and role="button"
#     div = clickable_divs[0]
#     div.click()
#     time.sleep(2)
#     button_div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.x1i10hfl.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xe8uvvx.xat24cr.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x6s0dn4.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x1ypdohk.x78zum5.xl56j7k.xcdnw81.x18d9i69.xp7jhwk.x1n0m28w.x9otpla.xurb0ha.x1sxyh0.x1y1aw1k[role="button"]')))
#     button_div.click()
#     time.sleep(2)
 
#     # Execute JavaScript to find the input element and set its value
#     js_script = """
#     let inputElement = document.querySelector('.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.xw2csxc.x1odjw0f.x1n2onr6.x1hnll1o.xs3hnx8.x1db89rt.xyfr5zc.x7xwk5j.xpqswwc.xl565be.x5dp1im.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1ye3gou.xn6708d.x5n08af.xh8yej3.x13faqbe');
#     if (inputElement) {
#         inputElement.value = 'HELL';  // Set the value
#         inputElement.dispatchEvent(new Event('input', { bubbles: true })); // Trigger input event
#         return 'Text \"HELL\" entered successfully!';
#     } else {
#         return 'Input element not found.';
#     }
#     """
#     # Execute the JavaScript and get the result
#     result = driver.execute_script(js_script)
#     time.sleep(6)
#     print(result)
#     # # Select all <span> elements with the specific class
#     # spans = driver.find_elements(By.CSS_SELECTOR, 'span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x1ji0vk5.x18bv5gf.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.xo1l8bm.x9bdzbf.x10wh9bi.x1wdrske.x8viiok.x18hxmgj')
#     # # Iterate over each <span> element
#     # for span in spans:
#     #     # Find all <a> tags within the current <span>
#     #     links = span.find_elements(By.CSS_SELECTOR, 'a')
#     #     a_texts = [a.get_attribute("innerText") for a in links]
#     #     print(a_texts)
#     #     hashtags = [text[1:] for text in a_texts if text.startswith("#")]
#     #     print(hashtags)
        
 
# reel_comments()
user_to_search = ['kartikaaryan']
try:
    for depth in range(1):
        span_texts = []
        for seed_username in user_to_search:
            driver.get("https://www.instagram.com/"+seed_username+"/")
            followers_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,f"//a[@href='/{seed_username}/followers/']")))
            followers_link.click()
            scrollable_div = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, 
                'div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6'
            ))
        )
 
            # Scroll multiple times (adjust iterations as needed)
            for _ in range(2):  # Scroll 5 times
                # Scroll down using JavaScript
                driver.execute_script(
                    "arguments[0].scrollTop += arguments[0].offsetHeight * 0.8;",
                    scrollable_div
                )
                time.sleep(2)  # Allow content to load
                # Wait for buttons to be available
            WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button._acan._acap._acas._aj1-._ap30'))
            )
 
            # Find all "Follow" buttons
            buttons = driver.find_elements(By.CSS_SELECTOR, 'button._acan._acap._acas._aj1-._ap30')
 
            # Filter only those that have "Follow" as text
            follow_buttons = [btn for btn in buttons if btn.text.strip() == "Follow"]
 
            print(f"Found {len(follow_buttons)} 'Follow' buttons.")
 
            # Click each button with a random delay
            # for button in follow_buttons:
            #     try:
            #         button.click()
            #         wait_time = random.uniform(5, 10)  # Random wait between 1-3 seconds
            #         print(f"Clicked a 'Follow' button, waiting {wait_time:.2f} seconds...")
            #         time.sleep(wait_time)
            #     except Exception as e:
            #         print(f"Error clicking button: {e}")
 
except Exception as e:
    print(f"An error occurred: {e}")
 
finally:
    driver.quit()
 
print("Graph Structure:")
for key, value in graph.items():
    print(f"{key}: {value}")