import hashlib

def hash_function(data):

    hash_object = hashlib.md5()

    # update
    hash_object.update(data.encode())


    hash_value = hash_object.hexdigest()

    return hash_value

input_data = "My final homework"
hash_value = hash_function(input_data)
print("Hash Value:", hash_value)
