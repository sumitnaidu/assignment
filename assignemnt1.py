import re
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from baseclass import base

obj = base()
favourite_list=[]
un_favourite_list=[]
my_video_list=[]


class favouritelist(base):


    _show_btn = ".dscHeaderMain__showsLink"
    _all_shows_btn = ".dscShowsDropContent__seeAllShows"
    _search_btn = ".headerSearch__searchIcon"
    _search_text_area = ".search-input"
    _search_result_list = ".searchGrid__tilesList .searchGrid__tile"
    _favourite_icon_element = ".showHero__showBrand .my-favorites-button-container .icon-plus"
    _unfavourite_icon_element = ".showHero__showBrand .my-favorites-button-container .icon-minus"
    _shows_details = ".showHero__showLogo"
    _menu_bar_list = ".dscHeaderMain__hideMobile .dscHeaderMain__iconMenu"
    _my_video_link = "My Videos"
    _my_video_modal = ".myVideosLayout__title"
    _favourite_show_section = ".FavoriteShowsCarousel"
    _favourite_show_lists = ".FavoriteShowsCarousel .carousel__main .showCarousel__content .showTileSquare__main"
    _favourite_show_title = ".showTileSquare__content .showTileSquare__title"

    driver=obj.driverfactory()
    driver.find_element_by_css_selector(_show_btn).click()
    obj.scrollwindow(200)
    obj.waitTillElementVisible(_all_shows_btn,10)
    driver.find_element_by_css_selector(_all_shows_btn).click()
    driver.find_element_by_css_selector(_search_btn).click()
    bb = driver.find_element_by_css_selector(_search_text_area)
    bb.send_keys("apollo")
    bb.send_keys(Keys.ENTER)
    obj.waitTillElementVisible(_search_result_list,10)
#wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".searchGrid__tilesList .searchGrid__tile")))
    shows = driver.find_elements_by_css_selector(_search_result_list)
    print(len(shows))
    for i in range(len(shows)):
        shows = driver.find_elements_by_css_selector(_search_result_list)
        show = shows[i].click()
        try:
            #men_menu = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".showHero__showBrand .my-favorites-button-container .icon-plus")))
            obj.waitTillElementVisible(_favourite_icon_element, 10)
            element = driver.find_element_by_css_selector(_favourite_icon_element)
            status = driver.find_element_by_css_selector(_favourite_icon_element).is_displayed()
            if status:
                element.click()
                show_title = str(driver.find_element_by_css_selector(_shows_details).get_attribute("alt"))
                favourite_list.append(show_title)
                driver.execute_script("window.history.go(-1)")
        except NoSuchElementException:
            element1 = driver.find_element_by_css_selector(_unfavourite_icon_element)
            element1.click()
            show_title = show_title = str(driver.find_element_by_css_selector(_shows_details ).get_attribute("alt"))
            un_favourite_list.append(show_title)
            driver.execute_script("window.history.go(-1)")
    print(favourite_list)
    driver.find_element_by_css_selector(_menu_bar_list).click()
    driver.find_element_by_link_text(_my_video_link).click()
    obj.waitTillElementVisible(_my_video_modal, 10)
    #wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".myVideosLayout__title")))
    result = driver.find_element_by_css_selector(_my_video_modal).is_displayed()
    assert result
    obj.scrollwindow(200)
    obj.waitTillElementVisible(_favourite_show_section, 10)
    #wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".FavoriteShowsCarousel")))
    favourite_section = driver.find_element_by_css_selector(_favourite_show_section).is_displayed()
    assert favourite_section
    #fav_list = driver.find_elements_by_css_selector(".showCarousel__carousel")
    fav_list = driver.find_elements_by_css_selector(_favourite_show_lists)
    for fav in fav_list:
        show_title = fav.find_element_by_css_selector(_favourite_show_title).get_attribute("innerHTML")
        title_list=re.findall(r">(.*?)<", show_title)
        my_video_list.append(title_list[0])

    favourite_list.sort()
    my_video_list.sort()
    if len(favourite_list) == len(my_video_list):
        status = cmp(favourite_list,my_video_list)
        if status == 0:
            assert  True
        else:
            assert False


    driver.quit()









