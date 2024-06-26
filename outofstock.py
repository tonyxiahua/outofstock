from bs4 import BeautifulSoup
from urllib.request import urlopen
#import sys
#import webbrowser
from selenium import webdriver
from notifications.notifications import NotificationHandler
import config
import threading
import time
import random
import subprocess
#import win32clipboard


def delay(min:int = 15, max:int =30):
    time.sleep(random.randint(min,max))

#def instockCall(stocklist:list):
#    win32clipboard.OpenClipboard()
#    win32clipboard.EmptyClipboard()
#    win32clipboard.SetClipboardText("\n\n".join(stocklist))
#    win32clipboard.CloseClipboard()
#    subprocess.call(['C:\\Program Files\\AutoHotkey\\AutoHotkey.exe',"callme.ahk"])

# def instockCall(stocklist:list):
#     win32clipboard.OpenClipboard()
#     win32clipboard.EmptyClipboard()
#     win32clipboard.SetClipboardText("\n\n".join(stocklist))
#     win32clipboard.CloseClipboard()
#     notification_handler = NotificationHandler()
#     notification_handler.urgent_call("\n\n".join(stocklist))
#     #subprocess.call(['C:\\Program Files\\AutoHotkey\\AutoHotkey.exe',"callne.ahk"])

# def brokenWebsite(textThis:list):
    #win32clipboard.OpenClipboard()
    #win32clipboard.EmptyClipboard()
    #win32clipboard.SetClipboardText("\n\n".join(textThis))
    #win32clipboard.CloseClipboard()
    #subprocess.call(['C:\\Program Files\\AutoHotkey\\AutoHotkey.exe',"textme.ahk"])
    notification_handler = NotificationHandler()
    notification_handler.send_notification("\n\n".join(textThis))
    delay(179,180)

def newegg(page_url:str):
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    #print(time.strftime("%H:%M:%S", time.localtime())+"\t- Newegg page refresh...")
    driver.get(page_url)
    page_soup = BeautifulSoup(driver.page_source, "html.parser")
    instock_links = []
    title = ""
    if page_soup.title:
        title = page_soup.title.text
    while True:
        if page_soup.title and page_soup.title.text != title:
            print(time.strftime("%H:%M:%S", time.localtime())+ " - ***Newegg broke***")
            brokenWebsite(["Newegg site is broken.\n"])
            driver.get(page_url)
        else:
        #if True:
            #client = urlopen(page_url)
            #page_soup = BeautifulSoup(client.read(), "html.parser")
            #client.close()
            items = page_soup.findAll("div", {"class":"item-container"})
            print(time.strftime("%H:%M:%S", time.localtime())+" - Newegg page refresh...items: " + str(len(items)))
            #outfilename = "GPUs.csv"
            #headers = "Stock,Name,Price,Shipping,URL\n"
            #outfile = open(outfilename,"w")
            #outfile.write(headers)
            for item in items:
                #Make sure it is not an ad
                if item.div.a.text != 'learn more':
                    #product_name = item.a.img["title"].split(",",1)[0].strip().replace("\n","")
                    #product_url = item.a["href"]
                    #stock = ''
                    #brand = item.div.select("a")[0].img["title"].title()
                    if  item.div.select("p") and item.div.select("p")[0].text == 'OUT OF STOCK':
                        #stock = 'N'
                        pass
                    else:
                        #stock = 'Y'
                        instock_links                       .append(item.a["href"])
                        #break
                    #print(product_name)
                    #price = item.findAll("li",{"class":"price-current"})[0].strong.text.strip().replace(",","")
                    #if  price != 'COMING SOON':
                    #    price = price + item.findAll("li",{"class":"price-current"})[0].sup.text.strip()
                    #shipping = item.findAll("li",{"class":"price-ship"})[0].text.replace(" Shipping", "").replace("$","").replace(",","")
                    #outfile.write(stock+","+product_name+","+price+","+shipping+","+product_url+'\n')
            #outfile.close()
            if instock_links:
                print(time.strftime("%H:%M:%S", time.localtime())+" - Pinging the homie for Newegg.")
                instockCall(instock_links)
                instock_links.clear()
                delay(135,136)
            delay()
            #driver.get("https://www.newegg.com/p/pl?N=100007709%20601357247%204841%20601321572&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_1&cm_mmc=snc-twitter-_-promo-_-brd-nvidia-3080-psa-_-091620")
            driver.refresh()
        page_soup = BeautifulSoup(driver.page_source, "html.parser")
            #print("New newegg URL:")
    driver.quit()
    return instock_links

def bestbuy(page_url:str):
    #print("Enter a new link:")
    #page_url = input()
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    #print(time.strftime("%H:%M:%S", time.localtime())+ "\t- Best Buy page refresh...")
    driver.get(page_url)
    page_soup = BeautifulSoup(driver.page_source, "html.parser")
    instock_links = []
    title = ""
    if page_soup.title:
        title = page_soup.title.text
    while True:
        if page_soup.title and page_soup.title.text != title:
            print(time.strftime("%H:%M:%S", time.localtime())+ " - ***Best Buy broke***")
            brokenWebsite(["Best Buy site is broken.\n"])
            driver.get(page_url)
        else:
            items = page_soup.findAll("li", {"class":"sku-item"})
            print(time.strftime("%H:%M:%S", time.localtime())+ " - Best Buy page refresh...items: " + str(len(items)))
            for item in items:
                if item.findAll("button",{"class":"btn btn-primary btn-sm btn-block btn-leading-ficon add-to-cart-button"}):
                    instock_links.append("https://bestbuy.com/" + (item.h4.select("a")[0]["href"]))
                #elif not item.findAll("button",{"class":"btn btn-disabled btn-sm btn-block add-to-cart-button"}):
                #    instockCall(["Best Buy is down."])

            if instock_links:
                print(time.strftime("%H:%M:%S", time.localtime())+" - Pinging the homie for Best Buy.")
                instockCall(instock_links)
                instock_links.clear()
                delay(135,136)
            delay()
            driver.refresh()
            delay(5)
        page_soup = BeautifulSoup(driver.page_source, "html.parser")
            #print("Enter a new Best Buy link:")
            #page_url = "https://www.bestbuy.com/site/computer-cards-components/video-graphics-cards/abcat0507002.c?id=abcat0507002&qp=gpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~AMD%20Radeon%20RX%205700%20XT%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20GTX%201660%20SUPER%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203070%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203080%5Egpusv_facet%3DGraphics%20Processing%20Unit%20(GPU)~NVIDIA%20GeForce%20RTX%203090"
            #driver.refresh()
            #link = "https://bestbuy.com/" + (items[0].h4.select("a")[0]["href"])
    #driver.close()
    driver.quit()
    #print(instock_links)
    return instock_links

def evga(page_url:str):
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    #print(time.strftime("%H:%M:%S", time.localtime())+ "\t- EVGA page refresh...")
    driver.get(page_url)
    page_soup = BeautifulSoup(driver.page_source, "html.parser")
    instock_links = []
    title = ""
    if page_soup.title:
        title = page_soup.title.text
    while True:
        if page_soup.title and page_soup.title.text != title:
            print(time.strftime("%H:%M:%S", time.localtime())+ " - ***EVGA broke***")
            brokenWebsite(["EVGA site is broken.\n"])
            driver.get(page_url)
        else:
            items = page_soup.findAll("div", {"class":"list-item"})
            print(time.strftime("%H:%M:%S", time.localtime())+ " - EVGA page refresh...items: " + str(len(items)))
            for item in items:
                if not item.findAll("i", {"class":"fa fa-info-circle"}):
                    instock_links.append("https://evga.com/" + item.div.a["href"])

            if instock_links:
                print(time.strftime("%H:%M:%S", time.localtime())+" - Pinging the homie for EVGA.")
                instockCall(instock_links)
                instock_links.clear()
                delay(135,136)
            delay()
            driver.refresh()
        #page_url = "https://www.evga.com/products/ProductList.aspx?type=0"
        page_soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    return instock_links

def bh(page_url:str):
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    #print(time.strftime("%H:%M:%S", time.localtime())+ "\t- B&H page refresh...")
    driver.get(page_url)
    page_soup = BeautifulSoup(driver.page_source, "html.parser")
    instock_links = []
    title = "rtx 3080 | B&H Photo Video"
    #if page_soup.title:
    #    title = page_soup.title.text
    while True:
        if page_soup.title and page_soup.title.text != title:
            print(time.strftime("%H:%M:%S", time.localtime())+ " - ***B&H broke***")
            brokenWebsite(["B&H site is broken.\n"])
            driver.get(page_url)
        else:
            items = page_soup.findAll("div", {"data-selenium":"miniProductPage"})
            print(time.strftime("%H:%M:%S", time.localtime())+ " - B&H page refresh...items: " + str(len(items)))
            for item in items:
                if item.findAll("button", {"data-selenium":"addToCartButton"}):
                    instock_links.append("https://www.bhphotovideo.com" + item.div.div.div.a["href"])

            if instock_links:
                print(time.strftime("%H:%M:%S", time.localtime())+" - Pinging the homie for B&H.")
                instock_links.clear()
                instock_links = []
                delay(135,136)
            delay()
            driver.refresh()
            #page_url = "https://www.bhphotovideo.com/c/search?Ntt=rtx&N=0&InitialSearch=yes&sts=ma"
        page_soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    return instock_links

def amazon(page_url:str):
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    #print(time.strftime("%H:%M:%S", time.localtime())+ "\t- amazon page refresh...")
    driver.get(page_url)
    page_soup = BeautifulSoup(driver.page_source, "html.parser")
    instock_links = []
    title = ""
    if page_soup.title:
        title = page_soup.title.text
    while True:
        if page_soup.title and page_soup.title.text != title:
            print(time.strftime("%H:%M:%S", time.localtime())+ " - ***amazon broke***")
            brokenWebsite(["amazon site is broken.\n"])
            driver.get(page_url)
        else:
            items = page_soup.findAll("li", {"class":"style__itemOuter__2dxew style__fixed__k9Vjk"})
            print(time.strftime("%H:%M:%S", time.localtime())+ " - amazon page refresh...items: " + str(len(items)))
            #print("total items: " + str(len(items)))
            for item in items:
                if item.findAll("button", {"data-click-type":"ADDTOCART"}):
                    instock_links.append("https://www.amazon.com" + item.a["href"])

            if instock_links:
                print(time.strftime("%H:%M:%S", time.localtime())+" - Pinging the homie for amazon.")
                instockCall(instock_links)
                instock_links.clear()
                delay(135,136)
            delay()
            driver.refresh()
        #page_url = "D:\\Downloads\\neweggtest\\Amazon.com_ GeForce _ RTX 3080.html"
        page_soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    return instock_links

def nvidia(page_url:str):
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    #print(time.strftime("%H:%M:%S", time.localtime())+ "\t- nVidia page refresh...")
    driver.get(page_url)
    page_soup = BeautifulSoup(driver.page_source, "html.parser")
    title = ""
    if page_soup.title:
        title = page_soup.title.text
    while True:
        if page_soup.title and page_soup.title.text != title:
            print(time.strftime("%H:%M:%S", time.localtime())+ " - ***nVidia broke***")
            brokenWebsite(["nVidia site is broken.\n"])
            driver.get(page_url)
        else:
            print(time.strftime("%H:%M:%S", time.localtime())+ " - nVidia page refresh...items: 1")
            if not page_soup.findAll("div",{"class":"cta-button btn show-out-of-stock oos-btn"}):
                print(time.strftime("%H:%M:%S", time.localtime())+" - Pinging the homie for nVidia.")
                instockCall([page_url])
                delay(120,121)
            delay(29,30)
            #page_url = "D:\\Downloads\\neweggtest\\Amazon.com_ GeForce _ RTX 3080.html"
            driver.refresh()
        delay(29,30)
        page_soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    return page_url

def adorama(page_url:str):
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    #print(time.strftime("%H:%M:%S", time.localtime())+ "\t- Adorama page refresh...")
    driver.get(page_url)
    page_soup = BeautifulSoup(driver.page_source, "html.parser")
    instock_links = []
    title = "rtx 3080 buy or learn at Adorama"
    #if page_soup.title:
    #    title = page_soup.title.text
    while True:
        if page_soup.title and page_soup.title.text != title:
            print(time.strftime("%H:%M:%S", time.localtime())+ " - ***Adorama broke***")
            #brokenWebsite(["Adorama site is broken.\n"])
            driver.get(page_url)
        else:
            items = page_soup.findAll("div", {"class":"item"})
            del items[-1]
            print(time.strftime("%H:%M:%S", time.localtime())+ " - Adorama page refresh...items: " + str(len(items)))
            for item in items:
                #print(item)
                if not item.findAll("button", {"data-orig-val":"Temporarily not available"}):
                    print(item)
                    instock_links.append(item.a["href"])

            if instock_links:
                print(time.strftime("%H:%M:%S", time.localtime())+" - Pinging the homie for Adorama.")
                instockCall(instock_links)
                instock_links.clear()
            driver.refresh()
        delay(105,135)
        #page_url = "https://www.adorama.com/l/?searchinfo=rtx%202080&sel=Item-Condition_New-Items"
        page_soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    return instock_links

def microcenter(page_url:str):
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    #print(time.strftime("%H:%M:%S", time.localtime())+ "\t- Microcenter page refresh...")
    driver.get(page_url)
    page_soup = BeautifulSoup(driver.page_source, "html.parser")
    instock_links = []
    title = ""
    if page_soup.title:
        title = page_soup.title.text
    while True:
        if page_soup.title and page_soup.title.text != title:
            print(time.strftime("%H:%M:%S", time.localtime())+ " - ***Microcenter broke***")
            brokenWebsite(["Microcenter site is broken.\n"])
            driver.get(page_url)
        else:
            items = page_soup.findAll("li", {"class":"product_wrapper"})
            print(time.strftime("%H:%M:%S", time.localtime())+ " - Microcenter page refresh...items: " + str(len(items)))
                
            #print("total items: " + str(len(items)))
            for item in items:
                #print(item)
                if item.findAll("div", {"class":"stock"})[0].strong.span.text != 'Sold Out':
                    instock_links.append("https://microcenter.com" + item.h2.a["href"])

            if instock_links:
                print(time.strftime("%H:%M:%S", time.localtime())+" - Pinging the homie for Microcenter.")
                instockCall(instock_links)
                instock_links.clear()
                delay(135,136)
            driver.refresh()
            delay()
            #page_url = "https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt=rtx&searchButton=search&storeid=101"
        page_soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    return instock_links

def asus(page_url:str):
    driver = webdriver.Chrome()
    #print(time.strftime("%H:%M:%S", time.localtime())+ "\t- Adorama page refresh...")
    driver.get(page_url)
    driver.implicitly_wait(15)
    page_soup = BeautifulSoup(driver.page_source, "html.parser")
    instock_links = []
    title = ""
    if page_soup.title:
        title = page_soup.title.text
    while True:
        if page_soup.title and page_soup.title.text != title:
                print(time.strftime("%H:%M:%S", time.localtime())+ " - ***ASUS broke***")
                brokenWebsite(["ASUS site is broken.\n"])
                driver.get(page_url)
        else:
            items = page_soup.findAll("figure",{"class":"item is-border-none"})
            print(time.strftime("%H:%M:%S", time.localtime())+ " - ASUS page refresh...items: " + str(len(items)))
            for item in items:
                #print("|||" + item.img["alt"])
                if item.findAll("a",{"ga_class":"btn-addcart"}):
                    instock_links.append("https:" + item.a["href"])

            if instock_links:
                print(time.strftime("%H:%M:%S", time.localtime())+" - Pinging the homie for ASUS.")
                #print("-------------------")
                #for x in instock_links:
                #    print(x)
                #print("-------------------")
                instockCall(instock_links)
                instock_links.clear()
                delay(149,150)
            driver.refresh()
        delay()
        page_soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

threads = list()
threads.append(threading.Thread(target=bestbuy, args=(config.bestbuy_url,)))
threads.append(threading.Thread(target=newegg, args=(config.newegg_url,)))
#threads.append(threading.Thread(target=evga, args=(config.evga_url,)))
#threads.append(threading.Thread(target=bh, args=(config.bh_url,)))
threads.append(threading.Thread(target=amazon, args=(config.amazon_url,)))
#threads.append(threading.Thread(target=microcenter, args=(config.microcenter_url,)))
threads.append(threading.Thread(target=asus, args=(config.asus_url,)))
#threads.append(threading.Thread(target=adorama, args=(config.adorama_url,)))
#threads.append(threading.Thread(target=nvidia, args=(config.nvidia_url,)))
for t in threads:
    t.start()
print("waiting for tasks to rejoin")
for t in threads:
    t.join()


#driver = webdriver.Chrome()
#driver.get("https://hangouts.google.com/")
#driver.find_element_by_xpath('//*[@id="gb_70"]').click()
#driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(config.hangouts['man']+'\n')
#driver.close()
