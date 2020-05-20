from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


def main():

    print("Enter the link to the creality product you'd like to check:")
    print("***Please make sure you select product for you respective country, otherwise will throw error when "
          "purchasing***")

    # Sample link: https://www.creality3dofficial.com/products/creality-ender-3-pro-3d-printer?variant=31314964578377

    website = input()

    if in_stock(website):
        print("The printer is available!")
        print("If you would like to purchase the printer, please enter yes!")
        if input() == "yes":
            purchase_item(website)
            print("You just bought the printer...that you will only ever use once.")
        else:
            print("Well you've just wasted precious computing power, go have a think about that")
    else:
        print("Sorry, you can't have it...or afford it.")


# purchase_item("https://www.creality3dofficial.com/products/creality-ender-3-pro-3d-printer?variant=31422802362441")


def in_stock(web_address):
    # connect to product page
    driver = webdriver.Chrome()
    driver.get(web_address)

    stock_condition = ""

    #  check add to cart span id to check stock
    for elem in driver.find_elements_by_xpath('.//span[@id = "AddToCartText-product-template"]'):
        stock_condition = elem.text

    #  close browser
    driver.close()

    #  returns bool to indicate whether or not prod is in stock
    if stock_condition == "Add to Cart":
        return True
    elif stock_condition == "Sold Out":
        return False
    else:
        #  not too familiar with python exceptions so picked this:
        raise NameError("website has changed stock condition location")


def purchase_item(web_address):
    # print("please enter your creality username:")
    # usr = input()
    # print("please enter your creality password:")
    # passwd = input()

    usr = "asda"
    passwd = "abc"

    # connect to product page
    driver = webdriver.Chrome()
    driver.get(web_address)

    #  inserted delay because find_elem would not work in time
    #  driver.maximize_window()
    driver.implicitly_wait(10)

    #  click on buy now to proceed to checkout
    button_clicker = driver.find_element_by_xpath("//*[@id='AddToCartForm-product-template']/div["
                                                  "4]/div/div/div/div/button[1]").click()
    act = ActionChains(button_clicker)
    act.click().perform()

    #  to do: login in with premade account and fill out purchase info

    #  driver.close()


if __name__ == '__main__':
    main()
