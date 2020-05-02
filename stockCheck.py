from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def main():
    print("Enter the link to the creality product you'd like to check:")
    website = input()
    in_stock(website)


def in_stock(web_address):
    driver = webdriver.Chrome()
    # connect to product page
    driver.get(web_address)
    stock = False

    # check to see if 'add to cart' is available for product
    try:
        driver.find_elements_by_class_name(
            "btn btn--full product-form__cart-submit btn--sold-out btn--secondary-accent")
    except NoSuchElementException:
        stock = True

    if stock:
        print("yeet, we got it bois")
    else:
        print("sike, they don't got it")

    driver.close()


if __name__ == '__main__':
    # sample website:
    # https://www.creality3dofficial.com/products/creality-ender-3-pro-3d-printer?variant=31314964578377
    main()
