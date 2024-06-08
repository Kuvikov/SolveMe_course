import pytest

def setup():
    print ("Фикстура: setup")
 
def teardown():
    print ("Фикстура: teardown")

def setup_module(module):
    print ("Фикстура МОДУЛЯ: setup")
 
def teardown_module(module):
    print ("Фикстура МОДУЛЯ: teardown")
 
def setup_function(function):
    print ("Фикстура ФУНКЦИИ: setup")
 
def teardown_function(function):
    print ("Фикстура ФУНКЦИИ: teardown")
 
def test_numbers_3_4():
    print ("ТЕСТ test 3*4")
    assert 3*4 == 12 
 
def test_strings_a_3():
    print ("ТЕСТ test a*3")
    assert 'a'*3 == 'aaa' 
  
class TestUM:
    def setup(self):
        print ("Информация о начале класса")
 
    def teardown(self):
        print ("Информация о окончании класса")
 
    def setup_class(cls):
        print ("Фикстура КЛАССА: setup")
 
    def teardown_class(cls):
        print ("Фикстура КЛАССА: teardown")
 
    def setup_method(self, method):
        print ("Метод: setup")
 
    def teardown_method(self, method):
        print ("Метод: teardown")
 
    def test_numbers_5_6(self):
        print ("test 5*6")
        assert 5*6 == 30 
 
    def test_strings_b_2(self):
        print ("test b*2")
        assert 'b'*2 == 'bb'