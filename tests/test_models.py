import pytest
from ..models.model import update_function  # Adjust this import based on your actual function

def test_update_function():
    initial_data = "Initial Data"  # Set initial data
    update_data = "Updated Data"    # Set data to update
    result = update_function(initial_data, update_data)  # Call your update function
    expected_result = "Updated Data"  # Replace with the expected output from your function
    assert result == expected_result
