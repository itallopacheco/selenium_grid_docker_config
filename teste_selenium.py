from seleniumrequests import Chrome

# URL do hub do Selenium Grid
hub_url = "http://localhost:4444/wd/hub"

# Inicializa o driver remoto do Selenium Grid
webdriver = Chrome()

webdriver.get("http://www.google.com")

response = webdriver.request('GET', 'http://www.google.com')

print(response)

webdriver.quit()
