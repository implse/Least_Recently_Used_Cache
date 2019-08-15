# Least Recently Used Cache

Least Recently Used (LRU) cache algorithm keeps recently used items near the top of cache.
Whenever a new item is accessed, the LRU places it at the top of the cache.
When the cache limit has been reached, items that have been accessed less recently will be removed starting from the bottom of the cache.
This can be an expensive algorithm to use, as it needs to keep "age bits" that show exactly when the item was accessed.
In addition, when a LRU cache algorithm deletes an item, the "age bit" changes on all the other items.


- Default capacity is 5 or pass integer value when instantiate LRUCache class.
- Fast Lookups : Hash Table
- Fast Removals : Double Linked List
