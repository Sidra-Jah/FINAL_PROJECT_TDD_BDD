import pytest
from ..models.model import list_all_function, read_function  # Adjust the import based on your project structure

def test_list_all_function():
    # Call the function to get all items
    result = list_all_function()  # Replace with your actual function name

    # Assert that the result is not empty
    assert result is not None
    assert isinstance(result, list)  # Ensure the result is a list
    assert len(result) > 0  # Check that there are items in the list

def test_read_function():
    # Assuming you have a read_function() to test
    result = read_function()  # Call your READ function
    assert result is not None  # Check that the result is not empty or None

# This is a test comment to force Git recognition
