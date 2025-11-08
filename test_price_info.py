import price_info

def test_cost_of_fruits():
    assert price_info.cost_of_fruits('apple', 10) == 12.0
    assert price_info.cost_of_fruits('pineapple', 2) == 5.4
    assert price_info.cost_of_fruits('pear', 0) == 0
    assert price_info.cost_of_fruits('mango', 5) == 0  

def test_total_cost_shopping():
    # 46.75 is the total from all items in your dictionaries
    assert price_info.total_cost_shopping() == 46.75
