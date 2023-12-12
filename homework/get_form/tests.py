from django.test import TestCase
import unittest
import random
import datetime

from . import views
from . import models


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


class TestGetForm(TestCase):
    @staticmethod
    def print_info(message):
        count = models.GetForm.objects.count()
        print(f"{message}: #all_forms={count}")

    def setUp(self) -> None:
        print("*" * 40)
        self.print_info('Start setUp')
        self.recording_form = models.GetForm.objects.create(email='ilyapopov@mail.ru',
                                                            phone='+7 999 999 99 99',
                                                            date='1975-09-30',
                                                            text='Hello World')
        self.print_info('Finish setUp')

    def test_creation(self):
        # Проверка создания объекта GetForm
        self.print_info('Start test_movie_creation')
        self.assertEqual(self.recording_form.email, 'ilyapopov@mail.ru')
        self.assertEqual(self.recording_form.phone, '+7 999 999 99 99')
        self.assertEqual(self.recording_form.date, '1975-09-30')
        self.assertEqual(self.recording_form.text, 'Hello World')
        self.print_info('Finish test_movie_creation')

    def test_get_all_records(self):
        # Проверка получения всех записей из бд
        self.print_info('Start test_movie_get_all_records')
        movies = models.GetForm.objects.all()
        self.assertEqual(len(movies), 1)
        self.print_info('Finish test_movie_get_all_records')

    def test_movie_get_record(self):
        # Проверка получения записи из бд
        self.print_info('Start test_movie_get_record')
        mask = models.GetForm.objects.get(email='ilyapopov@mail.ru')
        self.assertEqual(mask.text, 'Hello World')
        self.print_info('Finish test_movie_get_record')
