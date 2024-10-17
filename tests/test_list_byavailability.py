import pytest
from ..models.model import list_by_availability_function  # Import the function you want to test

def test_list_by_availability():
    availability_to_search = True  # or False depending on what you want to test
    expected_result = [...]  # Define what you expect the result to be
    
    result = list_by_availability_function(availability_to_search)  # Call your function here
    
    assert result == expected_result  # Verify that the result matches the expected result
