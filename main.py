from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time

f = open("DescriereNFT", "r")
descriereNft = f.read()
f.close()

f = open("LoseText", "r")
loseText = f.read()
f.close()

f = open("WinText", "r")
winText = f.read()
f.close()

tabel = [[0 for i in range(5)] for j in range(160)]

j = 0
x = 1
with open("tabel") as file:
    for linie in file:
        for i in linie.split():
            tabel[x][j] = i
            j = j + 1
            if j == 5:
                x = x + 1
                j = 0

keyboard = Controller()

options = webdriver.ChromeOptions()
options.add_argument("-no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_extension("/home/seba/PycharmProjects/OpenSeaUploader/venv/metamask.crx")

chrome = webdriver.Chrome(options=options)
chrome.maximize_window()


def tabKeyboard(nr):
    for i in range(nr):
        keyboard.press(Key.tab)
        time.sleep(0.3)
        keyboard.release(Key.tab)
        time.sleep(0.3)


def typeWord(word):
    for i in word:
        keyboard.press(i)
        time.sleep(0.05)
        keyboard.release(i)
        time.sleep(0.05)


# extension installation and management
chrome.get(
    "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase")
time.sleep(2)

keyboard.press(Key.ctrl)
keyboard.press("w")
time.sleep(1)
keyboard.release(Key.ctrl)
keyboard.release("w")
time.sleep(1)

# metamask import
element = chrome.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/input")
element.send_keys("***")  # mnemonic key
element = chrome.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div[5]/div/input")
element.send_keys("***")  # metamask password
element = chrome.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div[6]/div/input")
element.send_keys("***")  # metamask password
element = chrome.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div[7]/div")
element.click()
element = chrome.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/button")
element.click()
time.sleep(6)

# metamask login
chrome.get("https://opensea.io/")
time.sleep(3)
element = chrome.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/nav/ul/div[2]/div/li/a/i")
element.click()
time.sleep(3)

element = chrome.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[2]/ul/li[1]/button/div[2]")
element.click()
time.sleep(5)

tabKeyboard(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)

tabKeyboard(2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(5)

# first time on the create page
chrome.get("https://opensea.io/asset/create")
time.sleep(5)

element = chrome.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/div[2]/ul/li[1]/button/div[2]")
element.click()
time.sleep(2)

keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(0.5)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(1)

# --------------------------------------

index = 93
maximIndex = 100
while index < maximIndex + 1:
    tempLungime = len(str(index))
    if tempLungime == 3:
        formattedNum = index
    else:
        if tempLungime == 2:
            formattedNum = "0" + str(index)
        else:
            formattedNum = "00" + str(index)

    chrome.get("https://opensea.io/asset/create")
    time.sleep(5)

    element = chrome.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/section/div/form/div[1]/div/div[2]")
    element.send_keys("/home/seba/Desktop/AAA Terminat/bot/1.gif")
    time.sleep(3)

    typeWord("/home/seba/Desktop/AAA Terminat/bot/%s.gif" % (tabel[index][0]))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)

    # title section
    element = chrome.find_element(By.XPATH,
                                  "/html/body/div[1]/div[1]/main/div/div/section/div/form/div[2]/div/div[2]/div["
                                  "1]/input")
    element.send_keys("L.U.C.K - %s" % (tabel[index][2]))

    # description section
    element = chrome.find_element(By.XPATH,
                                  "/html/body/div[1]/div[1]/main/div/div/section/div/form/div[4]/div/textarea")
    element.send_keys(descriereNft % (formattedNum, tabel[index][2]))

    # proprieties section
    time.sleep(2)
    tabKeyboard(4)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)

    tabKeyboard(1)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)

    typeWord("L.U.C.K")

    tabKeyboard(1)

    typeWord(str(tabel[index][2]))

    tabKeyboard(1)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    tabKeyboard(5)

    typeWord("Series")

    tabKeyboard(1)

    typeWord("I")

    tabKeyboard(2)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)

    tabKeyboard(4)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)

    typeWord("Number")

    tabKeyboard(2)

    typeWord(str(100))

    tabKeyboard(5)

    typeWord(str(index))

    tabKeyboard(3)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)

    tabKeyboard(2)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)

    # unlockable section
    time.sleep(1)
    element = chrome.find_element(By.XPATH,
                                  "/html/body/div[1]/div[1]/main/div/div/section/div/form/section/div[4]/div["
                                  "2]/textarea")

    if int(tabel[index][3]) == 1:
        element.send_keys(
            winText % (tabel[index][2], tabel[index][2], str(tabel[index][1])[0:2], str(tabel[index][1])[2:4],
                       str(tabel[index][1])[4:6], str(tabel[index][1])[6:8], str(tabel[index][1])[8],
                       tabel[index][1]))
    else:
        element.send_keys(loseText % (tabel[index][2], tabel[index][2]))

    # network selection
    tabKeyboard(5)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)

    # confirm and send
    tabKeyboard(1)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)

    index = index + 100

    time.sleep(90)
