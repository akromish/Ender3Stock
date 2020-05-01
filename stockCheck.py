from selenium import webdriver

driver = webdriver.Chrome()
# connect to product page
driver.get("https://www.creality3dofficial.com/products/creality-ender-3-pro-3d-printer?variant=31314964578377")
stock = True
# check to see if 'add to cart' is available for product

for element in driver.find_elements_by_class_name\
            ("btn btn--full product-form__cart-submit btn--sold-out btn--secondary-accent"):
    # does not find any 'elements' by class name
    print("Its out of stock pal")
    stock = False

print("we moved on")
print(stock)

driver.close()

