from selenium import webdriver
import time
import pyautogui

#Reading the Credentials

doc=open('credentials.txt', "r")
username=doc.readline()
password=doc.readline()

usrname = (username[9:-1])
pwd = (password[4:-1])




#Advertisement Kind Of -_-
print('https://github.com/yashbos5620x')
print('Instagram Follow Bot V1)

#Inputing the username
searchUsrName = input('Input the username to be followed: ')

#Opening the Log-In page
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://instagram.com")

time.sleep(5)
#Finding the username and password box and typing the values in
usrbox = driver.find_element_by_name('username')
usrbox.send_keys(str(usrname))
pwdbox = driver.find_element_by_name('password')
pwdbox.send_keys(str(pwd))
#Finding the log-in button using pyautogui
time.sleep(1)
clickToLog = pyautogui.locateOnScreen('assets/login.png')
pyautogui.click(clickToLog)
time.sleep(5)
#Searching for the user
searchBox = driver.find_element_by_class_name('eyXLr')
searchBox.click()
pyautogui.typewrite(searchUsrName)
time.sleep(2)
#Selecting the user
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(5)
#Following
followBtn = pyautogui.locateOnScreen('assets/follow.png')
pyautogui.click(followBtn)