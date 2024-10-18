import pytest
from .models.model import delete_function, read_function  # Ensure the correct imports

def test_delete_function():
    # Setup: add an item to be deleted
    item_to_delete = "item_id"  # Replace with the actual ID you are testing
    
    # Precondition: make sure the item exists (optional based on your setup)
    initial_result = read_function()
    assert item_to_delete in initial_result, "Item should exist before deletion"

    # Action: delete the item
    delete_function(item_to_delete)

    # Assertion: verify the item has been deleted
    result = read_function()
    assert item_to_delete not in result, "Item should be deleted"

