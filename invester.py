import random
from selenium import webdriver


class investor:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def fillForm(self):
        self.driver.get("https://www.wjx.cn/jq/27950054.aspx")
        elems = self.driver.find_elements_by_class_name("div_table_radio_question")
        for i in elems:
            underlines = i.find_elements_by_class_name('underline')
            if underlines:
                underlines[0].send_keys("你好")
            else:
                options = i.find_elements_by_class_name('jqRadio')
                if options:
                    index = random.randint(0, len(options)-1)
                    options[index].click()
                else:
                    multiSelects = i.find_elements_by_class_name('jqCheckbox')
                    if multiSelects:
                        indexM = random.randint(0, len(multiSelects) - 1)
                        multiSelects[indexM].click()
        self.driver.find_element_by_class_name("submitbutton").click()

    def __del__(self):
        self.driver.close()

if __name__  == "__main__":
    i = investor()
    i.fillForm()

