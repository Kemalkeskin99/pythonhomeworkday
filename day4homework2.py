from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from selenium.webdriver.common.by import By

class test_sauce:
    def question_1(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        inputUserName=driver.find_element(By.ID,"user-name")
        inputUserName.send_keys()
        inputPassword=driver.find_element(By.ID,"password")
        inputPassword.send_keys()
        sleep(2)
        btnLogin=driver.find_element(By.ID,"login-button")
        btnLogin.click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text == "Epic sadface: Username is required"
        print(f"Uyarı: {testResult}")
       


    def question_2(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        inputUserName=driver.find_element(By.ID,"user-name")
        inputUserName.send_keys("1")
        inputPassword=driver.find_element(By.ID,"password")
        inputPassword.send_keys()
        sleep(2)
        btnLogin=driver.find_element(By.ID,"login-button")
        btnLogin.click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text == "Epic sadface: Password is required"
        print(f"Uyarı: {testResult}")
     


    def question_3(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        inputUserName=driver.find_element(By.ID,"user-name")
        inputUserName.send_keys("locked_out_user")
        inputPassword=driver.find_element(By.ID,"password")
        inputPassword.send_keys("secret_sauce")
        sleep(2)
        btnLogin=driver.find_element(By.ID,"login-button")
        btnLogin.click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text == "Epic sadface: Sorry, this user has been locked out"
        print(f"Uyarı: {testResult}")
    

    def question_4(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        inputUserName=driver.find_element(By.ID,"user-name")
        inputUserName.send_keys()
        inputPassword=driver.find_element(By.ID,"password")
        inputPassword.send_keys()
        sleep(2)
        btnLogin=driver.find_element(By.ID,"login-button")
        btnLogin.click()
        sleep(2)
        btnLogin=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        btnLogin.click()
        sleep(10)
    
    def question_5(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        inputUserName=driver.find_element(By.ID,"user-name")
        inputUserName.send_keys("standard_user")
        inputPassword=driver.find_element(By.ID,"password")
        inputPassword.send_keys("secret_sauce")
        sleep(2)
        btnLogin=driver.find_element(By.ID,"login-button")
        btnLogin.click()
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(100)
       

    def question_6(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        inputUserName=driver.find_element(By.ID,"user-name")
        inputUserName.send_keys("standard_user")
        inputPassword=driver.find_element(By.ID,"password")
        inputPassword.send_keys("secret_sauce")
        sleep(2)
        btnLogin=driver.find_element(By.ID,"login-button")
        btnLogin.click()
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(2)

        lengthProduct=driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Kullancıya Gösterilen ürün sayısı: {len(lengthProduct)}")

        





        while True:
            continue    

testSauce=test_sauce() 
#testSauce.question_1()
#testSauce.question_2()
#testSauce.question_3()
#testSauce.question_4()
#testSauce.question_5()
testSauce.question_6()

