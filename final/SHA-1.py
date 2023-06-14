import hashlib

def hash_function(data):

    hash_object = hashlib.sha1()
    hash_object.update(data.encode())
    hash_value = hash_object.hexdigest()

    return hash_value

input_data = "Using hash functions"
hash_value = hash_function(input_data)
print("hash value", hash_value)