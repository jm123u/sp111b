import hashlib

def hash_function(data):

    hash_object = hashlib.sha256()

    # update
    hash_object.update(data.encode())


    hash_value = hash_object.hexdigest()

    return hash_value

input_data = "Hash functions"
hash_value = hash_function(input_data)
print("Hash Value:", hash_value)
