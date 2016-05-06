# coding=utf-8

import unittest


class SearchCases(unittest.TestCase):
    def __init__(self):
        print ''

    def go_search_page(self,testrunner):

        ### Arama kutusunu aç
        testrunner.find_element_by_class_name('search').click()
        print 'Arama kutusu açıldı'

    def search_page_search_keyword(self,testrunner):

        ### Arama sayfasını aç
        search = SearchCases()
        search.go_search_page(testrunner)

        ### Arama yapılıyor
        testrunner.find_element_by_xpath('//*[@data-yto="searchInput"]').send_keys('lahmacun')

    def close_search_page(self,testrunner):

        ### Arama sayfasını aç
        search = SearchCases()
        search.go_search_page(testrunner)

        ### Aramayı kapat
        testrunner.find_element_by_xpath('//*[@data-yto="searchClose"]').click()
        print 'Arama kapatıldı'