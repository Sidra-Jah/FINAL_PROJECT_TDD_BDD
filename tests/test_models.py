import pytest
from ..models.model import delete_function, read_function  # Make sure both functions are imported correctly

def test_delete_function():
    # Read current state before deletion
    initial_result = read_function()  
    
    item_to_delete = "item_id"  # Replace with actual ID or name of the item
    assert item_to_delete in initial_result  # Verify the item exists

    # Delete the item
    delete_function(item_to_delete)  

    # Check the result after deletion
    result = read_function()  
    assert item_to_delete not in result  # Verify the item is deleted
