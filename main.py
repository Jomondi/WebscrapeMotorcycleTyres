import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from tire_rim_size import RimSize, aspect_ratio


TEST_URL = "https://www.cyclegear.com/motorcycle-tires?query=tires"

# Create object instances of the classes that are being imported
# aspect_ratio = AspectRatio()
rim = RimSize()

# Enter the driver path in the executable path value
driver = webdriver.Chrome(executable_path="")
driver.get(TEST_URL)

# Find and input values for the tire width
find_width = \
    driver.find_element(By.XPATH, "//*[@id='motorcycle_tire_finder']/div/div[1]/div[1]/div[1]/div[1]/select")
select_width = Select(find_width)
select_width.select_by_visible_text(aspect_ratio.TIRE_WIDTH)

# Find and input values for the tire aspect ratio
find_aspect_ratio = \
    driver.find_element(By.XPATH, "//*[@id='motorcycle_tire_finder']/div/div[1]/div[1]/div[1]/div[2]/select")
select_aspect_ratio = Select(find_aspect_ratio)
select_aspect_ratio.select_by_visible_text(aspect_ratio.TIRE_ASPECT_RATIO)

# Find and input values for the tire rim size
find_rim_size = \
    driver.find_element(By.XPATH, "//*[@id='motorcycle_tire_finder']/div/div[1]/div[1]/div[1]/div[3]/select")
select_rim_size = Select(find_rim_size)
select_rim_size.select_by_visible_text(rim.TIRE_RIM_SIZE)

# Search for the selected tire values
driver.find_element(By.CLASS_NAME, "tire-finder__search-wrapper").click()

# Retrieve results description and price
tire_names = []
tire_prices = []
content = driver.page_source

soup = BeautifulSoup(content)

for elements in soup.findAll('div', {'product-tile__name'}):
    if elements not in tire_names:
        tire_names.append(elements.text.strip())

for elements in soup.findAll('div', {'product-details__price-retail product-tile__price-retail '
                                     'product-tile__price-retail--sale mny__rng', 'product-details__price-retail '
                                                                                  'product-tile__price-retail '
                                                                                  'mny__rng'}):
    # Strip and remove white spaces from the returned price range then replace the middle white space with a dash
    if elements not in tire_prices:
        vals = elements.text.strip()
        tire_prices.append(vals.replace('\n', " - "))


# Create and save the results in a csv document
df = pd.DataFrame({'Tire Name': tire_names, 'Tire Price': tire_prices})
df.to_csv('Tire_price.csv', index=False, encoding='utf-8')
driver.quit()