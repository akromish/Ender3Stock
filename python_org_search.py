from selenium import webdriver

driver = webdriver.Chrome()
# connect to product page
driver.get("https://www.creality3dofficial.com/products/creality-ender-3-pro-3d-printer?variant=31314964578377")

# check to see if 'add to cart' is availble for product
if "Add to Cart" in driver.page_source:
    # this seems to go positive even if not in stock
    print("Go go go, they have it in stockkkkkk")
else:
    print("No no no, hi hi hi recruiter person(please give me an interviewwwwww)")

driver.close()
