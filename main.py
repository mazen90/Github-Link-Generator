from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.github.com')
from selenium.webdriver.common.keys import Keys
while True:
    text = input('search for: ')
    if text == 'close':
        browser.quit()
        break
    browser.find_element('xpath','/html/body/div[1]/header/div[3]/div/div/form/label/input[1]').clear()

    browser.find_element('xpath','/html/body/div[1]/header/div[3]/div/div/form/label/input[1]').send_keys(text)
    browser.find_element('xpath','/html/body/div[1]/header/div[3]/div/div/form/label/input[1]').send_keys(Keys.ENTER)
    file = open('files\\{}.txt'.format(text), 'a+')
    file.write('links for {} projects\n'.format(text))
    for i in browser.find_elements('xpath','//*[@id="js-pjax-container"]/div/div[3]/div/ul/*/div[2]/div[1]/div/a'):
        print(i.text)
        file.write('https://www.github.com/{}\n'.format(i.text))
    file.close()