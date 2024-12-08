import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_buns():
    return [
        Bun("black bun", 100),
        Bun("white bun", 200),
        Bun("red bun", 300),
    ]


@pytest.fixture
def mock_ingredients():
    return [
        Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.5),
        Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200.11),
        Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300.234),
        Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
        Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300),
    ]


@pytest.fixture
def database(mock_buns, mock_ingredients):
    db = Database()
    db.buns = mock_buns
    db.ingredients = mock_ingredients
    return db


def test_buns_count(database):
    assert len(database.available_buns()) == 3


def test_buns_type(database):
    assert all(isinstance(bun, Bun) for bun in database.available_buns())


@pytest.mark.parametrize("index, expected_name", [(0, "black bun"), (1, "white bun"), (2, "red bun")])
def test_bun_names(database, index, expected_name):
    assert database.available_buns()[index].get_name() == expected_name


@pytest.mark.parametrize("index, expected_price", [(0, 100), (1, 200), (2, 300)])
def test_bun_prices(database, index, expected_price):
    assert database.available_buns()[index].get_price() == expected_price


def test_ingredients_count(database, mock_ingredients):
    assert len(database.available_ingredients()) == len(mock_ingredients)


def test_ingredients_type(database):
    assert all(isinstance(ingredient, Ingredient) for ingredient in database.available_ingredients())


@pytest.mark.parametrize(
    "index, expected_name",
    [
        (0, "hot sauce"),
        (1, "sour cream"),
        (2, "chili sauce"),
        (3, "cutlet"),
        (4, "dinosaur"),
        (5, "sausage"),
    ],
)
def test_ingredient_names(database, index, expected_name):
    assert database.available_ingredients()[index].get_name() == expected_name


@pytest.mark.parametrize(
    "index, expected_type",
    [
        (0, INGREDIENT_TYPE_SAUCE),
        (1, INGREDIENT_TYPE_SAUCE),
        (2, INGREDIENT_TYPE_SAUCE),
        (3, INGREDIENT_TYPE_FILLING),
        (4, INGREDIENT_TYPE_FILLING),
        (5, INGREDIENT_TYPE_FILLING),
    ],
)
def test_ingredient_types(database, index, expected_type):
    assert database.available_ingredients()[index].get_type() == expected_type


@pytest.mark.parametrize(
    "index, expected_price",
    [
        (0, 100.5),
        (1, 200.11),
        (2, 300.234),
        (3, 100.00),
        (4, 200.0),
        (5, 300),
    ],
)
def test_ingredient_prices(database, index, expected_price):
    assert database.available_ingredients()[index].get_price() == expected_price
