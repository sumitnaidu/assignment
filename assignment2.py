import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

from baseclass import base

obj = base()


class popularshows(base):

    _popular_shows_section = ".popularShowsCarousel__content"
    _popular_show_list = "//*[@id='react-root']/div/div[1]/section[9]/div/div[1]/div[1]/div/div/div/div"  # Used xpath due to timeshortage but would prefer css instead"
    _next_show_arrow_icon_1 = ".icon-arrow-right"
    _next_show_arrow_icon_2 = ".popularShowsCarousel__controlsProp .icon-arrow-right"
    _popular_show_title = ".popularShowTile__showButtonWrapper"
    _show_more_btn = ".episodeList__showMoreButton"
    _episode_list = ".episodeList__list li"
    _episode_title = ".episodeTitle"
    _episode_duration = ".minutes"


    driver=obj.driverfactory()
    ele = driver.find_element_by_css_selector(_popular_shows_section)
    #driver.execute_script("arguments[0].scrollIntoView();", ele)
    obj.scroll_to_element(ele)
    popular_length = driver.find_elements_by_xpath("//*[@id='react-root']/div/div[1]/section[9]/div/div[1]/div[1]/div/div/div/div")
    ele = driver.find_element_by_css_selector(_next_show_arrow_icon_1)
    try:
        for i in range(len(popular_length)):
            driver.find_element_by_css_selector(_next_show_arrow_icon_2).click()
    except NoSuchElementException:
        driver.implicitly_wait(5)
        driver.find_elements_by_css_selector(_popular_show_title)[i].click()
    obj.scrollwindow(1000)
    obj.waitTillElementVisible(_show_more_btn,10)
    show_btn = driver.find_element_by_css_selector(_show_more_btn)
    if show_btn.is_displayed():
        show_btn.click()
    else:
        obj.scrollwindow(200)
        show_btn.click()
    episodelist =  driver.find_elements_by_css_selector(_episode_list)
    try:
        with open("episode.txt","w") as fp:
            fp.truncate()
            for episode in episodelist:
                episode_title = episode.find_element_by_css_selector(_episode_title).text
                episode_duration = episode.find_element_by_css_selector(_episode_duration).text
                episode_details = "Title: " + str(episode_title) +","+"Duration: "+str(episode_duration) +"\n"
                print(episode_details)
                fp.write(episode_details)
    except NoSuchElementException:
        driver.quit()


