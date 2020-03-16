from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get(site):
    driver = webdriver.Firefox()
    driver.get("https://"+site+".com")
    driver.implicitly_wait(10)
    return driver
def Person(driver,contact):
    driver.find_element_by_xpath("//*[@title='"+contact+"']").click()

def news(msg,driver,search_engine):
    search=msg[-1].text[5:]
    search_engine.get("https://www.bing.com/news/search?q="+search+"&FORM=HDRSC6")
    count=10
    results=search_engine.find_elements_by_css_selector('a.title')
    news=search_engine.find_elements_by_css_selector('div.snippet')
    for i in range(min(len(news),count+1)):
        send_message("*"+results[i].text+"*"+"  "+news[i].text+"   "+results[i].get_attribute('href'),10,driver)
    if min(len(news),count+1)==0:
        send_message("No Results Found!! :(",10,driver)
    else:
        send_message("Results Found!!",10,driver)
    return


def youtube(msg,driver,search_engine):
    link=msg[-1].text
    search_engine.get(link)
    search_engine.implicitly_wait(100)
    comments=search_engine.find_elements_by_css_selector('ytd-expander.expander-exp.style-scope.ytd-comment-renderer')
    for i in comments:
        send_message(i.text,10,driver)


def get_msgs(driver):
    return driver.find_elements_by_class_name("_F7Vk.selectable-text.invisible-space.copyable-text")
def mes(driver,search_engine):
    msg=get_msgs(driver)
    if 'news' in msg[-1].text.lower()[:6]:
        news(msg,driver,search_engine)
        return 1
    elif 'exit' in msg[-1].text.lower():
        send_message("Turning off Bot!!",10,driver)
        return 0
    elif 'youtu.be' in msg[-1].text.lower():
        youtube(msg,driver,search_engine)
    return 1
    



def send_message(message, wait, browser):
    text_field=driver.find_element_by_class_name("_3u328.copyable-text.selectable-text")
    text_field.send_keys(message)
    text_field.send_keys(Keys.ENTER)

    
if __name__=='__main__':
    site="web.whatsapp"
    driver=get(site)
    name=input('Enter Contact Name:')
    Person(driver,name)
    msg=input('Enter Message:')
    times=int(input('Enter Number of Times:'))
    for j in range(times):
        send_message(msg,0,driver)
    
    
