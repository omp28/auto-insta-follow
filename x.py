import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
from datetime import datetime
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HumanLikeInteraction:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.actions = None
        self.interaction_count = 0
        self.session_start_time = datetime.now()

    def attach_to_chrome(self):
        """Attach to existing Chrome instance with human-like behavior enabled"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)

        # marketting comments
        self.marketing_tweets = [
            "Think you know your partner better than they know      you? 👀 Play Who Knows Better? and put your love to     the test! https://who-knows-better.fun",
    
            "Date night idea unlocked! Answer fun couple        questions and see who reigns supreme in love    knowledge! ❤️ Play now: https://who-knows-better.    fun",
    
            "Valentine's Challenge: Who knows who better? Play      this couples quiz & find out! #ValentinesDay        https://who-knows-better.fun",
    
            "Couples quiz alert! Test your relationship         knowledge with your partner. Who will win? Take the         quiz: https://who-knows-better.fun",
    
            "What's my favorite movie? What's my dream      vacation? ✈️ Think you know? Prove it in this fun       couples quiz! Start now: https://who-knows-better.     fun",

            "Valentine's Date Night Hack! Take our fun couples      quiz and make your night unforgettable! ❤️ Play     here: https://who-knows-better.fun",
    
            "Challenge your partner! Who really listens better?         Play this interactive relationship test now! 🎮         https://who-knows-better.fun",
    
            "❤️ Love is a game... and we made it a quiz! See        how well you really know each other! Play Who Knows     Better? https://who-knows-better.fun",
    
            "Who's the relationship expert? Play this fun quiz      and find out who really knows better! Start here:       https://who-knows-better.fun",
    
            "Couples, assemble! It's time to test your love         knowledge. Who's got the best memory? Play now:         https://who-knows-better.fun"
        ]


    def human_activity_simulation(self):
        """Simulate random human activities"""
        activities = [
            self.simulate_reading,
            self.simulate_tab_switch,
            self.simulate_scroll_pause,
            self.simulate_mouse_movement,
            self.simulate_text_selection
        ]
        
        # Randomly choose and perform activities
        if random.random() < 0.3:
            random.choice(activities)()

    def safe_scroll_into_view(self, element):
        """Safely scroll element into view with retry mechanism"""
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                # Scroll to element with offset to avoid header/footer
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", 
                    element
                )
                time.sleep(random.uniform(1, 2))
                # Add some offset to avoid fixed headers
                self.driver.execute_script("window.scrollBy(0, -100);")
                return True
            except Exception as e:
                logger.warning(f"Scroll attempt {attempt + 1} failed: {str(e)}")
                time.sleep(1)
        return False

    def safe_click(self, element, wait_time=5):
        """Safely click element with multiple attempts and strategies"""
        try:
            # Wait for element to be clickable
            self.wait.until(EC.element_to_be_clickable(element))
            
            # Try regular click first
            try:
                element.click()
                return True
            except:
                pass

            # Try JavaScript click if regular click fails
            try:
                self.driver.execute_script("arguments[0].click();", element)
                return True
            except:
                pass

            # Try Actions click if JavaScript click fails
            try:
                self.actions.move_to_element(element).click().perform()
                return True
            except:
                return False

        except Exception as e:
            logger.error(f"All click attempts failed: {str(e)}")
            return False

    def simulate_reading(self):
        """Simulate reading behavior"""
        # Calculate reading time based on content length
        content_length = len(self.driver.find_element(By.TAG_NAME, "body").text)
        reading_time = random.uniform(0.02, 0.04) * content_length  # 200-400 words per minute
        time.sleep(min(reading_time, 15))  # Cap at 15 seconds

    def simulate_tab_switch(self):
        """Simulate switching between tabs"""
        if random.random() < 0.2:
            # Store current handle
            current = self.driver.current_window_handle
            # Open new tab
            self.driver.execute_script("window.open('');")
            time.sleep(random.uniform(2, 5))
            # Switch back
            self.driver.switch_to.window(current)

    def simulate_scroll_pause(self):
        """Simulate natural scroll pauses"""
        if random.random() < 0.3:
            pause_time = random.uniform(2, 8)
            logger.info(f"Taking a natural reading pause for {pause_time:.1f} seconds")
            time.sleep(pause_time)

    def simulate_mouse_movement(self):
        """Simulate natural mouse movements"""
        try:
            # Move to random positions on screen
            viewport_width = self.driver.execute_script("return window.innerWidth;")
            viewport_height = self.driver.execute_script("return window.innerHeight;")
            
            points = [
                (random.randint(0, viewport_width), random.randint(0, viewport_height))
                for _ in range(random.randint(2, 5))
            ]
            
            for point in points:
                self.actions.move_by_offset(point[0], point[1])
                time.sleep(random.uniform(0.1, 0.3))
                self.actions.perform()
                
        except Exception as e:
            logger.debug(f"Mouse movement simulation error: {str(e)}")

    def simulate_text_selection(self):
        """Simulate text selection behavior"""
        try:
            elements = self.driver.find_elements(By.TAG_NAME, "p")
            if elements:
                element = random.choice(elements)
                self.actions.move_to_element(element)
                self.actions.click_and_hold()
                self.actions.move_by_offset(50, 0)  # Select ~8-10 characters
                self.actions.release()
                self.actions.perform()
                time.sleep(random.uniform(0.5, 1.5))
        except Exception as e:
            logger.debug(f"Text selection simulation error: {str(e)}")

    def check_session_limits(self):
        """Check and enforce session limits"""
        session_duration = (datetime.now() - self.session_start_time).total_seconds() / 3600
        
        # End session if too long or too many interactions
        if session_duration > 2 or self.interaction_count > 20:  # 2 hours or 20 interactions
            logger.info("Session limits reached, taking a long break...")
            time.sleep(random.uniform(1800, 3600))  # 30-60 minute break
            self.session_start_time = datetime.now()
            self.interaction_count = 0

    def get_contextual_comment(self, post_text):
        """Generate context-aware comment"""
        # Detect post context
        # if any(word in post_text.lower() for word in ['tech', 'technology', 'coding', 'programming']):
        #     return random.choice(self.tech_comments)
        # elif any(word in post_text.lower() for word in ['news', 'update', 'breaking']):
        #     return random.choice(self.news_comments)
        # return random.choice(self.comments)
        return random.choice(self.marketing_tweets)

    def human_like_type(self, element, text):
        """Type text with human-like patterns"""
        # Simulate thinking before typing
        time.sleep(random.uniform(1, 3))
        
        words = text.split()
        for i, word in enumerate(words):
            # Type word
            for char in word:
                element.send_keys(char)
                time.sleep(random.uniform(0.1, 0.3))
            
            # Add space after word
            if i < len(words) - 1:
                element.send_keys(Keys.SPACE)
                
                # Sometimes pause between words
                if random.random() < 0.2:
                    time.sleep(random.uniform(0.5, 1.5))
                
                # Sometimes make a typo and correct it
                if random.random() < 0.1:
                    typo = random.choice('abcdefghijklmnopqrstuvwxyz')
                    element.send_keys(typo)
                    time.sleep(random.uniform(0.2, 0.5))
                    element.send_keys(Keys.BACKSPACE)
                    time.sleep(random.uniform(0.2, 0.5))

    def wait_for_element_presence(self, by, value, timeout=10):
        """Wait for element with retry mechanism"""
        try:
            element = self.wait.until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            logger.error(f"Element not found: {value}")
            return None

    def interact_with_post(self, post):
        """Enhanced post interaction with more human-like behavior"""
        try:
            # Check session limits
            self.check_session_limits()
            
            # Random skip with variable probability
            # if random.random() < 0.4:
            #     logger.info("Naturally skipping this post")
            #     return

            # Ensure post is visible
            if not self.safe_scroll_into_view(post):
                return

            # Simulate reading the post
            self.simulate_reading()
            
            # Sometimes perform random human activities
            self.human_activity_simulation()

            # Get post text for context
            post_text = post.text
            
            # Find and click reply with improved detection
            reply_button = None
            for selector in [
                '[data-testid="reply"]',
                'button[aria-label*="Reply"]',
                'div[role="button"][aria-label*="Reply"]'
            ]:
                try:
                    reply_button = post.find_element(By.CSS_SELECTOR, selector)
                    if reply_button.is_displayed():
                        break
                except:
                    continue

            if not reply_button:
                return

            # Sometimes like before commenting
            if random.random() < 0.3:
                try:
                    like_button = post.find_element(By.CSS_SELECTOR, '[data-testid="like"]')
                    if random.random() < 0.7:  # 70% chance to actually like
                        self.safe_click(like_button)
                        time.sleep(random.uniform(0.5, 1.5))
                except:
                    pass

            # Click reply
            if not self.safe_click(reply_button):
                return

            # Find and interact with comment box
            comment_box = self.wait_for_element_presence(
                By.CSS_SELECTOR, 
                '[data-testid="tweetTextarea_0"]'
            )
            
            if not comment_box:
                return

            # Generate contextual comment
            comment = self.get_contextual_comment(post_text)
            
            # Type comment naturally
            self.human_like_type(comment_box, comment)

            # Sometimes preview before posting
            if random.random() < 0.3:
                time.sleep(random.uniform(2, 4))
                # Simulate reviewing the comment
                self.actions.move_to_element(comment_box).perform()
                time.sleep(random.uniform(1, 2))

            # Find and click post button
            post_button = self.wait_for_element_presence(
                By.CSS_SELECTOR,
                '[data-testid="tweetButton"]'
            )

            if not post_button:
                return

            # Click post button
            if self.safe_click(post_button):
                self.interaction_count += 1
                
                # Variable delay after posting
                time.sleep(random.uniform(8, 15))
                
                # Sometimes perform additional human activities
                self.human_activity_simulation()

        except Exception as e:
            logger.error(f"Error in post interaction: {str(e)}")
            time.sleep(random.uniform(2, 4))


    def main_loop(self):
        """Main interaction loop with improved error handling"""
        try:
            while True:
                # Find posts with retry mechanism
                posts = None
                for _ in range(3):
                    try:
                        posts = self.wait.until(EC.presence_of_all_elements_located(
                            (By.CSS_SELECTOR, 'article[data-testid="tweet"]')))
                        if posts:
                            break
                    except:
                        self.driver.execute_script("window.scrollBy(0, 300);")
                        time.sleep(2)

                if not posts:
                    logger.error("No posts found")
                    time.sleep(5)
                    continue

                # Process random number of posts
                num_posts = random.randint(1, 3)
                for post in posts[:num_posts]:
                    self.interact_with_post(post)
                    time.sleep(random.uniform(10, 20))

                # Scroll with random pause
                self.driver.execute_script(
                    f"window.scrollBy(0, {random.randint(300, 600)});"
                )
                time.sleep(random.uniform(5, 10))

        except Exception as e:
            logger.error(f"Main loop error: {str(e)}")


# def main():
#     bot = HumanLikeInteraction()
#     try:
#         bot.attach_to_chrome()
#         bot.main_loop()
#     except Exception as e:
#         logger.error(f"Fatal error: {str(e)}")
def main_loop(self):
    """Main interaction loop with improved error handling"""
    try:
        while True:
            # Find posts with retry mechanism
            posts = None
            for _ in range(3):
                try:
                    posts = self.wait.until(EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, 'article[data-testid="tweet"]')))
                    if posts:
                        break
                except:
                    self.driver.execute_script("window.scrollBy(0, 300);")
                    time.sleep(2)

            if not posts:
                logger.error("No posts found")
                time.sleep(5)
                continue

            # Check if all visible posts are your own
            all_own_posts = True
            for post in posts[:3]:  # Check first few posts
                try:
                    username_element = post.find_element(
                        By.CSS_SELECTOR, 
                        '[data-testid="User-Name"] a'
                    )
                    post_username = username_element.get_attribute('href').split('/')[-1]
                    if post_username != self.my_username:
                        all_own_posts = False
                        break
                except:
                    all_own_posts = False
                    break

            # If all visible posts are your own, scroll more
            if all_own_posts:
                self.driver.execute_script(
                    f"window.scrollBy(0, {random.randint(600, 900)});"
                )
                time.sleep(random.uniform(3, 5))
                continue

            # Process random number of posts
            num_posts = random.randint(1, 3)
            for post in posts[:num_posts]:
                self.interact_with_post(post)
                time.sleep(random.uniform(10, 20))

            # Scroll with random pause
            self.driver.execute_script(
                f"window.scrollBy(0, {random.randint(300, 600)});"
            )
            time.sleep(random.uniform(5, 10))

    except Exception as e:
        logger.error(f"Main loop error: {str(e)}")

if __name__ == "__main__":
    main()