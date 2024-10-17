import pytest
from ..models.model import delete_function, read_function  # Make sure both functions are imported correctly

def test_delete_function():
    # First, ensure the item exists. You may need to adjust this based on your application's logic.
    initial_result = read_function()  # Read current state before deletion
    
    item_to_delete = "item_id"  # Replace with the actual ID you are testing
    assert item_to_delete in initial_result  # Check that the item exists before deletion

    # Now delete the item
    delete_function(item_to_delete)  

    # Read the result again after deletion
    result = read_function()  
    assert item_to_delete not in result  # Verify the item is deleted
