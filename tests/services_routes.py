# tests/service_routes.py

# List to store items (this should represent your data model)
items = []

def list_all_function():
    """Returns all items."""
    return items

def read_function(item_id):
    """Returns a specific item by ID."""
    for item in items:
        if item['id'] == item_id:
            return item
    return None

def update_item(item_id, updated_data):
    """Updates an item by its ID."""
    item = read_function(item_id)
    if item:
        item.update(updated_data)
        return item
    return None

def delete_function(item_id):
    """Deletes an item by its ID."""
    global items
    items = [item for item in items if item['id'] != item_id]

# Adding sample data for testing (optional)
items.append({'id': 1, 'name': 'Item 1'})
items.append({'id': 2, 'name': 'Item 2'})

# Test Cases
import pytest

def test_list_all_function():
    result = list_all_function()
    assert result is not None
    assert isinstance(result, list)

def test_read_function():
    result = read_function(1)  # Assuming ID 1 exists
    assert result is not None
    assert result['id'] == 1

def test_update_item():
    updated_data = {'name': 'Updated Item 1'}
    updated_item = update_item(1, updated_data)
    assert updated_item is not None
    assert updated_item['name'] == 'Updated Item 1'

def test_delete_function():
    # Precondition: Check if the item exists before deletion
    result_before = read_function(1)
    assert result_before is not None

    # Action: Delete the item
    delete_function(1)

    # Assertion: Verify the item has been deleted
    result_after = read_function(1)
    assert result_after is None
