import datetime
from unittest import mock

from django.core.exceptions import ValidationError
from django.test import TestCase

from book.models import current_year, max_value_current_year


class ValidatorsTests(TestCase):
    def setUp(self):
        self.datetime_mock = mock.Mock(wraps=datetime.date)
        self.datetime_mock.today.return_value = datetime.datetime(2021, 11, 25)

    def test_returns_current_year(self):
        with mock.patch("datetime.date", new=self.datetime_mock):
            result = current_year()
            expected_result = datetime.datetime(2021, 11, 25).year
            assert result == expected_result

    def test_throws_error_when_max_value_greater_than_current_year(self):
        with mock.patch("datetime.date", new=self.datetime_mock):
            year = 2022
            with self.assertRaises(ValidationError):
                max_value_current_year(year)
