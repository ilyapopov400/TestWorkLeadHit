from django.test import TestCase
import unittest
import random
import datetime

from . import views


# Create your tests here.

class TestValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.Validator = views.Validator

    def test_none(self):
        list_form = ['', '', '', '', ]
        result = self.Validator(list_form=list_form).run()
        correct_answer = {'email': None, 'phone': None, 'data': None, 'text': ''}
        self.assertEqual(correct_answer, result)

    def test_true1(self):
        for _ in range(10):
            list_form = ['il_pop@mail.ru', '+7 927 598 93 45', '30.09.1975', 'Hello World!', ]
            random.shuffle(list_form)
            result = self.Validator(list_form=list_form).run()
            correct_answer = {'email': 'il_pop@mail.ru', 'phone': '+7 927 598 93 45',
                              'data': datetime.date(1975, 9, 30),
                              'text': 'Hello World!'}

            self.assertEqual(correct_answer, result)

    def test_true2(self):
        for _ in range(10):
            list_form = ['il_pop@mail.ru', '+7 927 598 93 45', '1975.09.30', 'Hello World!', ]
            random.shuffle(list_form)
            result = self.Validator(list_form=list_form).run()
            correct_answer = {'email': 'il_pop@mail.ru', 'phone': '+7 927 598 93 45',
                              'data': datetime.date(1975, 9, 30),
                              'text': 'Hello World!'}

            self.assertEqual(correct_answer, result)

    def test_partially_without_phone(self):
        for _ in range(10):
            list_form = ['il_pop@mail.ru', '+7 927 598 93 4qwerty', '1975.09.30', 'Hello World!', ]
            random.shuffle(list_form)
            result = self.Validator(list_form=list_form).run()
            correct_answer = {'email': 'il_pop@mail.ru', 'phone': None,
                              'data': datetime.date(1975, 9, 30),
                              'text': 'Hello World!'}

            self.assertEqual(correct_answer.get('phone'), result.get('phone'))
            self.assertEqual(correct_answer.get('email'), result.get('email'))
            self.assertEqual(correct_answer.get('data'), result.get('data'))

    def test_partially_without_email(self):
        for _ in range(10):
            list_form = ['ilru', '+7 927 598 93 45', '1975.09.30', 'Hello World!', ]
            random.shuffle(list_form)
            result = self.Validator(list_form=list_form).run()
            correct_answer = {'email': None, 'phone': '+7 927 598 93 45',
                              'data': datetime.date(1975, 9, 30),
                              'text': 'Hello World!'}

            self.assertEqual(correct_answer.get('phone'), result.get('phone'))
            self.assertEqual(correct_answer.get('email'), result.get('email'))
            self.assertEqual(correct_answer.get('data'), result.get('data'))

    def test_partially_without_data(self):
        for _ in range(10):
            list_form = ['il_pop@mail.ru', '+7 927 598 93 45', '19751975.09.30', 'Hello World!', ]
            random.shuffle(list_form)
            result = self.Validator(list_form=list_form).run()
            correct_answer = {'email': 'il_pop@mail.ru', 'phone': '+7 927 598 93 45',
                              'data': None,
                              'text': 'Hello World!'}

            self.assertEqual(correct_answer.get('phone'), result.get('phone'))
            self.assertEqual(correct_answer.get('email'), result.get('email'))
            self.assertEqual(correct_answer.get('data'), result.get('data'))
