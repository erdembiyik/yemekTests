# coding=utf-8

import unittest
from selenium.webdriver.common.action_chains import ActionChains


class ProfileCases(unittest.TestCase):
    def __init__(self):
        print ''

    def go_profile(self, testrunner):
        element = testrunner.find_element_by_class_name('avatar')
        hov = ActionChains(testrunner).move_to_element(element)
        hov.perform()
        print 'Donut üzerine hover yapıldı'

        testrunner.find_element_by_xpath('//*[@data-yto="headerProfile"]').click()
        print 'Profil butonuna basıldı'

        ###Sayfa kontrolleri
        ###Yazılar Tabı
        PChecker_1 = testrunner.find_element_by_id('yazilarLink')
        assert PChecker_1.text == 'Yazılar'.decode('utf-8')
        PText_1 = testrunner.find_element_by_xpath('//*[@data-yto="noneText"]')
        assert PText_1.text == 'Henüz hiç yemeli içmeli yazısı yok, keşke olsa :/'.decode('utf-8')

        ###Tarifler Tabı
        PChecker_2 = testrunner.find_element_by_id('tariflerLink')
        assert PChecker_2.text == 'Tarifler'.decode('utf-8')
        testrunner.find_element_by_id('tariflerLink').click()
        PText_2 = testrunner.find_element_by_xpath('//*[@data-yto="noneRecipe"]')
        assert PText_2.text == 'Henüz hiç spesiyal tarifi yok, keşke olsa :/'.decode('utf-8')

        ###Favoriler Tabı
        PChecker_3 = testrunner.find_element_by_id('favorilerLink')
        assert PChecker_3.text == 'Favoriler'.decode('utf-8')
        testrunner.find_element_by_id('favorilerLink').click()
        PText_3 = testrunner.find_element_by_xpath('//*[@data-yto="noneFavorite"]')
        assert PText_3.text == 'Henüz hiç favorilediği içerik yok, keşke olsa :/'.decode('utf-8')

        ###RatingBox
        PChecker_4 = testrunner.find_element_by_xpath('//*[@data-yto="authorTakipci"]')
        assert PChecker_4.text == 'takipçi'.decode('utf-8')
        PChecker_5 = testrunner.find_element_by_xpath('//*[@data-yto="authorYazi"]')
        assert PChecker_5.text == 'yazı'.decode('utf-8')
        PChecker_6 = testrunner.find_element_by_xpath('//*[@data-yto="authorYorum"]')
        assert PChecker_6.text == 'yorum'.decode('utf-8')

        ###Takip ettikleri
        PChecker_7 = testrunner.find_element_by_xpath('//*[@data-yto="authorTakipBox"]')
        assert PChecker_7.text == 'Takip Ettikleri'.decode('utf-8')

    def go_setting_from_profile(self, testrunner):
        ### Menuye gidildi
        element = testrunner.find_element_by_class_name('avatar')
        hov = ActionChains(testrunner).move_to_element(element)
        hov.perform()
        print 'Donut üzerine hover yapıldı'

        ### Profil butonuna basildi
        testrunner.find_element_by_xpath('//*[@data-yto="headerProfile"]').click()
        print 'Profil butonuna basıldı'

        ### Yazar edit butonuna basildi
        element2 = testrunner.find_element_by_class_name('author')
        hov = ActionChains(testrunner).move_to_element(element2)
        hov.perform()
        testrunner.find_element_by_class_name('edit').click()
        print 'Profil sayfasındaki Yazar Edit butonuna basıldı'
        testrunner.find_element_by_xpath('//*[@id="settingsOverlayContent"]/div[1]/button').click()