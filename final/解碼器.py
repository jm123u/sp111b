import chardet
import hashlib
import unicodedata

def text_decoder(encoded_text, hash_algorithms=['md5', 'sha1', 'sha256', 'my_md5', 'my_sha1', 'my_sha256']):
    result = chardet.detect(encoded_text)
    source_encoding = result['encoding']

    target_encodings = ['utf-8', 'gbk', 'big5']

    decoded_text = None
    integrity_hashes = {}

    for target_encoding in target_encodings:
        try:
            decoded_text = encoded_text.decode(source_encoding)
            normalized_text = unicodedata.normalize('NFKC', decoded_text)
            encoded_text = normalized_text.encode(target_encoding)
            decoded_text = encoded_text.decode(target_encoding)

            for algorithm in hash_algorithms:
                if algorithm == 'my_md5':
                    hash_value = my_md5(decoded_text)
                elif algorithm == 'my_sha1':
                    hash_value = my_sha1(decoded_text)
                elif algorithm == 'my_sha256':
                    hash_value = my_sha256(decoded_text)
                else:
                    hash_value = hashlib.new(algorithm, encoded_text).hexdigest()

                integrity_hashes[algorithm] = hash_value

            return decoded_text, integrity_hashes

        except UnicodeDecodeError:
            continue

    print("Error: Failed to decode the text.")
    return None, None



def my_md5(data):
    hash_object = hashlib.md5()

    # update
    hash_object.update(data.encode())

    hash_value = hash_object.hexdigest()

    return hash_value


def my_sha1(data):
    hash_object = hashlib.sha1()
    hash_object.update(data.encode())
    hash_value = hash_object.hexdigest()

    return hash_value


def my_sha256(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hash_value = hash_object.hexdigest()

    return hash_value


input_data = "My final homework"
hash_value = my_md5(input_data)
print("my_md5:", hash_value)

input_data = "Using hash functions"
hash_value = my_sha1(input_data)
print("my_sha1:", hash_value)

input_data = "Hash functions"
hash_value = my_sha256(input_data)
print("my_sha256:", hash_value)

encoded_text = b'\xef\xbc\xa1\xef\xbc\x92\xef\xbc\x93\xef\xbc\x94\xef\xbc\x95'

decoded_text, integrity_hashes = text_decoder(encoded_text)
if decoded_text and integrity_hashes:
    print("Decoded text:", decoded_text)
    print("Integrity hashes:")
    for algorithm, hash_value in integrity_hashes.items():
        print(f"{algorithm}: {hash_value}")

with open('output.txt', 'w') as file:
    file.write("Decoded text: " + decoded_text + "\n")
    file.write("Integrity hashes:\n")
    for algorithm, hash_value in integrity_hashes.items():
        file.write(f"{algorithm}: {hash_value}\n")

print("Output saved to output.txt file.")