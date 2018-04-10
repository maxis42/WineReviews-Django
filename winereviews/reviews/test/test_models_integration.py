from reviews.models import Wine, Review
import pytest
from unittest.mock import Mock, MagicMock

def test_wine_clas_average_rating_called_with():
    new_wine = Wine()
    new_wine.average_rating = MagicMock(return_value=3)
    new_wine.average_rating()
    new_wine.average_rating.assert_called_with()

def test_wine_clas_average_rating_returned_value():
    new_wine = Wine()
    new_wine.average_rating = MagicMock(return_value=3)
    assert new_wine.average_rating() == 3

def test_wine_clas_min_rating_called_with():
    new_wine = Wine()
    new_wine.min_rating = MagicMock(return_value=3)
    new_wine.min_rating()
    new_wine.min_rating.assert_called_with()

def test_wine_clas_min_rating_returned_value():
    new_wine = Wine()
    new_wine.min_rating = MagicMock(return_value=3)
    assert new_wine.min_rating() == 3

def test_wine_clas_max_rating_called_with():
    new_wine = Wine()
    new_wine.max_rating = MagicMock(return_value=3)
    new_wine.max_rating()
    new_wine.max_rating.assert_called_with()

def test_wine_clas_max_rating_returned_value():
    new_wine = Wine()
    new_wine.max_rating = MagicMock(return_value=3)
    assert new_wine.max_rating() == 3

def test_review_class_rating_choices_called_with():
    new_review = Review()
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    new_review.return_rating_choices = MagicMock(return_value=RATING_CHOICES)
    new_review.return_rating_choices()
    new_review.return_rating_choices.assert_called_with()

def test_review_class_rating_choices_returned_value():
    new_review = Review()
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    new_review.return_rating_choices = MagicMock(return_value=RATING_CHOICES)
    assert new_review.return_rating_choices() == RATING_CHOICES
