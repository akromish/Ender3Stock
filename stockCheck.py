from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def main():

    print("Enter the link to the creality product you'd like to check:")

    # sample website:
    # https://www.creality3dofficial.com/products/creality-ender-3-pro-3d-printer?variant=31314964578377
    website = input()

    print(in_stock(website))


def in_stock(web_address):

    # connect to product page
    driver = webdriver.Chrome()
    driver.get(web_address)

    stock_condition = ""

    #  check add to cart span id to check stock
    for elem in driver.find_elements_by_xpath('.//span[@id = "AddToCartText-product-template"]'):
        stock_condition = elem.text

    #  returns bool to indicate whether or not prod is in stock
    if stock_condition == "Add to Cart":
        return True
    elif stock_condition == "Sold Out":
        return False
    else:
        #  not too familiar with python exceptions so picked this:
        raise NameError("website has changed stock condition location")

    #  close browser
    driver.close()


if __name__ == '__main__':
    main()
