from selenium import webdriver
from slacker import Slacker
from slackbot_settings import API_TOKEN
import os.path

def dokkaiahen():
    url='http://dka-hero.com/top.html'
    driver=webdriver.PhantomJS()
    print(driver.title)
    driver.get(url)

    frame = driver.find_element_by_name('contents')
    driver.switch_to_frame(frame)
    newtitle = driver.find_element_by_xpath('//table/tbody/tr[3]')


    file=open('change_record.txt','w+')

    if newtitle.text != file.read():
        file.write(newtitle.text)
        file.close()

        return '読解アヘン{}が更新されました！'.format(newtitle.text)
    else:
        pass


if __name__=='__main__':
    slack=Slacker(API_TOKEN)
    notice=dokkaiahen()
    if notice:
        slack.chat.post_message('#general',notice,as_user=True)