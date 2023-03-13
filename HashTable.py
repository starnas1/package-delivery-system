# Creating the class for a hash table
class HashTable:

    def __init__(self, size=40):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    # Creating a function for inserting a key and value into the hash table
    def insert(self, key, value):

        hash_bucket = hash(key) % self.size
        bucket_contents = self.table[hash_bucket]

        for kv_pair in bucket_contents:
            if kv_pair[0] == key:
                kv_pair[1] = value
                return True

        key_value_pair = [key, value]
        bucket_contents.append(key_value_pair)
        return True

    # Creating a function for deleting a key and value from the hash table
    def delete(self, key):

        hash_bucket = hash(key) % self.size
        bucket_contents = self.table[hash_bucket]

        for kv_pair in bucket_contents:
            if kv_pair[0] == key:
                bucket_contents.remove(kv_pair)
                return True

        return False

    # Creating a function for searching the hash table and returning the value associated with the key
    def search(self, key):

        hash_bucket = hash(key) % self.size
        bucket_contents = self.table[hash_bucket]

        for kv_pair in bucket_contents:
            if kv_pair[0] == key:
                return kv_pair[1]

        return None
