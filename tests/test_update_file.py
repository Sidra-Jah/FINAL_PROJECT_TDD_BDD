import pytest
from ..models.model import update_function, read_function  # Import the update and read functions

def test_update_function():
    # Initial item setup: Make sure the item you want to update exists
    item_id = "existing_item_id"  # Replace with actual ID
    initial_data = read_function(item_id)  # Read the current state of the item
    
    assert initial_data is not None  # Ensure the item exists before updating

    # Define the new data for the update
    updated_data = {"name": "New Name", "category": "New Category"}

    # Perform the update
    update_function(item_id, updated_data)

    # Read the updated item to verify changes
    updated_item = read_function(item_id)
    
    assert updated_item["name"] == "New Name"  # Check if the name was updated
    assert updated_item["category"] == "New Category"  # Check if the category was updated

    # Test for updating an item

