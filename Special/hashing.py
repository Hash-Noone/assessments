# QUEST 3 — Hashing and Hash Maps: Build the Mechanism (25 marks)
# Learning target: Understand keys, hash indexes, collisions, 
# buckets, and why a hash map still needs to compare keys.
# You may use lists, tuples, loops, and conditionals, 
# but you may NOT use dict or set in this question.
def hash_key(key):
    return sum(ord(char) for char in key) % 7
# A. Calculate (5 marks): Manually calculate the slot index 
# for 'cat', 'act', 'dog', and 'god'. Show the character-code sum and remainder for each.
# It converts each character into its character code, adds the codes together, 
# and takes the remainder after dividing by 7.
# Key	Character codes	    Sum	Calculation	Index
# cat	c=99, a=97, t=116	312	312 % 7 = 4	4
# act	a=97, c=99, t=116	312	312 % 7 = 4	4
# dog	d=100, o=111, g=103	314	314 % 7 = 6	6
# god	g=103, o=111, d=100	314	314 % 7 = 6	6

# Final answer:
# - cat → slot 4
# - act → slot 4
# - dog → slot 6
# - god → slot 6
# B. Reason about collisions (5 marks): 
# Identify any collisions. Explain why different strings can map to the 
# same index and why a matching index does not prove two keys are equal.
# A collision occurs when two different keys map to the same bucket index.

# There are two collisions in our examples:
# - cat and act both map to slot 4.
# - dog and god both map to slot 6.
# Why does this happen?

# Our hash function adds the character codes together. Since addition is commutative, 
# changing the order of the same characters does not change their sum.

# For example:
# \[
# 99+97+116=97+99+116=312
# \]

# Both strings therefore produce the same hash index.

# A matching index does not prove that two keys are equal because a bucket can store 
# multiple different keys. The hash function reduces a potentially large number of 
# possible strings to just seven indexes, so different strings must sometimes share 
# indexes.

# How the hash map handles this: It stores multiple key-value pairs in the same bucket and compares the actual keys to find the correct pair.
# C. Implement (10 marks): Build a seven-slot hash map using separate chaining. 
# Implement put(key, value), get(key), and delete(key). 
# put must update an existing key rather than duplicate it; get must 
# return None for a missing key; 
# delete must remove only the requested key.
# D. Analyse (5 marks): Explain expected time complexity under reasonable 
# hashing assumptions and worst-case complexity if all keys land in 
# one bucket. Explain how a larger table may help without guaranteeing 
# O(1) for every operation.
# Implementation guidance: Each slot can hold a list of key-value pairs. 
# To retrieve a value, compute the bucket index, then scan that bucket and 
# compare the stored key with the requested key.
# Do not confuse the hash function with the whole hash map. 
# The hash function chooses a bucket; collision handling and key comparison 
# are still necessary.


class SevenSlotHashMap:
    def __init__(self, capacity=7):
        # Create a fixed number of empty buckets.
        # Each bucket stores key-value pairs that share an index.
        self.capacity = capacity
        self.slots = [[] for _ in range(capacity)]

    def hash(self, key):
        # Generate a hash value using a polynomial hash function.
        # The multiplier helps account for the order of characters.
        hash_value = 0
        multiplier = 29

        for char in key:
            hash_value = hash_value * multiplier + ord(char)

        # Map the hash value to a valid bucket index.
        return hash_value % self.capacity

    def put(self, key, value):
        # Calculate the bucket where the key should be stored.
        bucket_index = self.hash(key)
        bucket = self.slots[bucket_index]

        # If the key already exists, update its value.
        for index, pair in enumerate(bucket):
            if pair[0] == key:
                bucket[index] = [key, value]
                return f"Successfully updated {key} to {value}"

        # If the key does not exist, add a new key-value pair.
        bucket.append([key, value])
        return f"Successfully added {key}: {value} to the map"

    def get(self, key):
        # Find the bucket that should contain the key.
        bucket_index = self.hash(key)
        bucket = self.slots[bucket_index]

        # Compare keys to find the exact matching pair.
        for stored_key, value in bucket:
            if stored_key == key:
                return value

        # Return None if the key is not present.
        return None

    def delete(self, key):
        # Find the bucket that should contain the key.
        bucket_index = self.hash(key)
        bucket = self.slots[bucket_index]

        # Find and remove only the pair with the matching key.
        for index, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(index)
                return f"Successfully removed {key}"

        # Report when the key cannot be found.
        return f"{key} does not exist in the map"


# Create a hash map and test its operations.
seven_hash = SevenSlotHashMap()

print(seven_hash.put("Drake", 25))
print(seven_hash.get("Drake"))
print(seven_hash.delete("Drake"))

### Complexity Analysis

# The time complexity of a hash map depends on how its keys are distributed across 
# its buckets and how many key-value pairs each bucket contains.

# **1. Average-case complexity**

# Under reasonable hashing assumptions, `get()` and `delete()` have an expected time 
# complexity of O(1) when the load factor remains bounded. The `put()` operation 
# also has expected O(1) time complexity under these conditions.

# When inserting a new key, the map calculates its bucket index and appends the key-value 
# pair. However, it must first check whether the key already exists to avoid duplicates.

# **2. Worst-case complexity**

# If many keys map to the same bucket, the map must scan that bucket to find the 
# requested key. Consequently, `get()`, `delete()`, and `put()` can take O(n) time in the 
# worst case, where n is the total number of stored key-value pairs.

# For example, if a bucket contains 500 pairs and the requested key is the last pair, 
# the map may need to compare the requested key against all 500 stored keys before 
# finding it.

# Although the hash function identifies the correct bucket quickly, it cannot guarantee 
# that the bucket contains only a few pairs.

# **3. Increasing the table capacity**

# Increasing the number of buckets can reduce collisions and shorten the average search 
# within each bucket. However, a larger table does not guarantee constant-time 
# operations because keys may still cluster in the same bucket.

# **4. Dynamic resizing**

# A more scalable approach is to resize the hash map automatically when its load factor 
# exceeds a chosen threshold. For example, the map could double its capacity and 
# redistribute existing key-value pairs into the new buckets.

# This process is called *rehashing*. It takes O(n) time for a resize, but because 
# resizing does not happen on every insertion, the amortized insertion complexity 
# can remain O(1) under reasonable hashing assumptions.

# In conclusion, separate chaining provides expected constant-time operations when keys 
# are distributed reasonably and the load factor is controlled. Dynamic resizing helps 
# maintain that performance as the number of stored pairs grows, but it does not 
# eliminate the possibility of worst-case O(n) operations.