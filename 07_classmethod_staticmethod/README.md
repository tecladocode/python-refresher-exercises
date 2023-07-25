# @classmethod and @staticmethod

This coding exercise requires you to complete two method implementations.

1. The `franchise` method, which takes in a store as argument. It should return a new `Store` object, with a name equal to the argument + `" - franchise"`.
2. The `store_details` method, which also takes in a store as argument. It should return a string representing the argument.

A few examples:

```python
store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

Store.franchise(store)  # returns a Store with name "Test - franchise"
Store.franchise(store2)  # returns a Store with name "Amazon - franchise"

Store.store_details(store)  # returns "Test, total stock price: 0"
Store.store_details(store2)  # returns "Amazon, total stock price: 160"
```

When completing the `store_details` method, you may need to convert the output of `store.stock_price` to an integer. You can do this like so: `int(store.stock_price)`.

Good luck!
