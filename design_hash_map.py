"""

Problem: 706. Design HashMap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]



Solution: 

The implementation uses a direct addressing table approach with a fixed-size array. Here's how each component works:

Data Structure:

We use a single array self.data of size 1,000,001 to store all key-value mappings
Each index in the array represents a possible key (0 to 1,000,000)
The value at each index represents the corresponding value for that key
Initialization (__init__):

self.data = [-1] * 1000001
Creates an array with 1,000,001 elements, all initialized to -1
The value -1 serves as a marker for "no value exists at this key"
This initialization ensures that get operations on non-existent keys automatically return -1
Put Operation (put(key, value)):

self.data[key] = value
Directly assigns the value to the array at index key
If a value already exists at that key, it gets overwritten (update behavior)
Time complexity: O(1) - direct array access
Get Operation (get(key)):

return self.data[key]
Simply returns the value stored at index key
If the key was never set, it returns -1 (the initialization value)
Time complexity: O(1) - direct array access
Remove Operation (remove(key)):

self.data[key] = -1
Sets the value at index key back to -1
This effectively marks the key as "removed" or "non-existent"
Time complexity: O(1) - direct array access
Trade-offs of this approach:

Advantages: Extremely simple implementation, guaranteed O(1) time for all operations, no collision handling needed
Disadvantages: Uses O(10^6) space regardless of the number of elements stored, only works when keys are integers in a known range
This solution leverages the constraint that keys are bounded integers to eliminate the need for a hash function entirely, making it a perfect example of how problem constraints can lead to simplified solutions.
"""

class MyHashMap:
    def __init__(self):
        """
        Initialize the HashMap data structure. Using direct adddressing with an array to store key-value pairs.
        Array size is 10^6 + 1 to handle the keys range[0,10^6].
        """
        # Intialize the array with -1 to intdicate empty slots

        self.data = [-1]*1000001

    def put(self,key: int,value: int) -> None:
        """
        Insert or update a key-value pair in the hashmap.
        Args:
            key:The key to insert/delete (0 <= key <= 10^6)
            value: the value to associate with the key
        """
        #  Direct addressing : use the key as index

        self.data[key] = value

    def get(self,key:int) -> int:
        """
        Retrive the value associated with the given key.
        args: 
            key: the key to look up
        returns: the value associated with the key, or -1 if key doesn't exisst 
        """
        # return value at index 'key' (-1 if not present)
        return self.data[key]

    def remove(self,key:int) -> None:
        """
        Remove the key-value pair from the HashMap.
      
        Args:
            key: The key to remove
        """
        # Reset to -1 to indicate the key is removed
        self.data[key] = -1



# My MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key, value)
# param_2 = obj.get(key)
# obj.remove(key)
