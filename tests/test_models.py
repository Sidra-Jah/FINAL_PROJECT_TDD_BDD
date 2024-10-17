import pytest
from ..models.model import delete_function, read_function  # Ensure correct imports

def test_delete_function():
    # Assume the item to delete
    item_to_delete = "item_id"  # Replace with actual ID

    # Verify the item exists before deletion
    initial_result = read_function()  # Get current items
    assert item_to_delete in initial_result  # Check it exists

    # Perform the delete operation
    delete_function(item_to_delete)

    # Verify the item no longer exists
    result = read_function()  # Get items after deletion
    assert item_to_delete not in result  # Check it has been deleted
