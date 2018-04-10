from reviews.models import Wine, Review
import pytest
from unittest.mock import Mock, MagicMock
from datetime import datetime

class TestWine:
    def setup(self):
        self.new_wine = Wine(name='Wine1')

    def test_wine_creation_class(self):
        assert self.new_wine.name == 'Wine1'


class TestReview:
    def setup(self):
        self.new_wine = Wine(name='Wine1')
        self.new_review = Review(
            wine=self.new_wine,
            pub_date=datetime(2015, 1, 1, 12, 30, 59, 0),
            user_name='admin',
            comment='Best wine',
            rating=4
        )

    def test_review_class_pubdate(self):
        from datetime import datetime
        assert self.new_review.pub_date == datetime(2015, 1, 1, 12, 30, 59, 0)

    def test_review_class_username(self):
        assert self.new_review.user_name == 'admin'

    def test_review_class_comment(self):
        assert self.new_review.comment == 'Best wine'

    def test_review_class_rating(self):
        assert self.new_review.rating == 4

    def test_review_class_rating_choices(self):
        RATING_CHOICES = (
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        )
        assert self.new_review.RATING_CHOICES == RATING_CHOICES
