print("""

 _   _           _           _   _                       
| \ | |         | |         | \ | |                      
|  \| | __ _ ___| |_ _   _  |  \| | __ _ _ __   ___ _ __ 
| . ` |/ _` / __| __| | | | | . ` |/ _` | '_ \ / _ \ '__|
| |\  | (_| \__ \ |_| |_| | | |\  | (_| | |_) |  __/ |   
\_| \_/\__,_|___/\__|\__, | \_| \_/\__,_| .__/ \___|_|   
                      __/ |             | |              
                     |___/              |_|              


""")

from selenium import webdriver

driver = webdriver.Chrome('C:/Users/This pc/Desktop/whatsapp bot/chromedriver.exe')

driver.implicitly_wait(15)

driver.get('https://web.whatsapp.com')

driver.find_element_by_css_selector("span[title='" + input("Enter the target name: ") + "']").click()

inputString = input("Enter message to send: ")

turn = input(int("How many times you want to send message: "))

i = 0;

while(i <= turn):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)

    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

    i += 1


print("Mission Complete !!")