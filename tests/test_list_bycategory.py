import pytest
from ..models.model import list_by_category_function  # Ensure this is the correct import

def test_list_by_category_function():
    category_to_search = "desired_category"  # Replace with the actual category
    result = list_by_category_function(category_to_search)  # Call your function here

    # Add assertions to validate the result
    assert isinstance(result, list)  # Check if the result is a list
    assert all(item['category'] == category_to_search for item in result)  # Check if all items match the category

