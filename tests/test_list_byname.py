import pytest
from ..models.model import list_by_name_function  # Ensure the correct import

def test_list_by_name():
    name_to_search = "example_name"  # Replace with an actual name in your data
    result = list_by_name_function(name_to_search)  # Call your function here

    assert isinstance(result, list)  # Check if the result is a list
    assert all(item['name'] == name_to_search for item in result)  # Validate the names in the result

