from selenium import webdriver

web = webdriver.Chrome()
web.get('https://www.mk2festivalparadiso.com/registration/627d102885bd0c0087438267?force_new_registration=true')
lastName = 'Bettayeb'
firstName = 'Youssef'
postalCode = '91130'

last = web.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/form/div/div[2]/input')
first = web.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/form/div/div[3]/input')

postal = web.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div/form/div/div[4]/input')

textInfo = [(lastName,last),(firstName,first),(postalCode,postal)]

