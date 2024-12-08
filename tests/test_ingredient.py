import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

test_data = [
    (INGREDIENT_TYPE_SAUCE, "sour cream", 150.5),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200.0),
    (INGREDIENT_TYPE_FILLING, "", 0.5),
    (INGREDIENT_TYPE_SAUCE, "hot sauce", -100.0),
]


@pytest.mark.parametrize("ingredient_type, name, price", test_data)
class TestIngredient:

    @pytest.fixture
    def ingredient(self, ingredient_type, name, price):
        return Ingredient(ingredient_type, name, price)

    def test_get_type(self, ingredient, ingredient_type):
        assert ingredient.get_type() == ingredient_type

    def test_get_name(self, ingredient, name):
        assert ingredient.get_name() == name

    def test_get_price(self, ingredient, price):
        assert ingredient.get_price() == price
