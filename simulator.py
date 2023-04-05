import hashlib
import time

MAX_NONCE = 1000000000  # Maximum nonce value to try

def sha256(text):
    return hashlib.sha256(text.encode('ascii')).hexdigest()

def mine(block_number, transactions, previous_hash, difficulty):
    prefix = '0' * difficulty
    for nonce in range(MAX_NONCE):
        data = str(block_number) + transactions + previous_hash + str(nonce)
        hash_value = sha256(data)
        if hash_value.startswith(prefix):
            print(f"Block mined successfully with nonce value: {nonce}")
            return hash_value

    raise BaseException(f"Couldn't find a valid hash after trying {MAX_NONCE} nonces")

if __name__ == '__main__':
    transactions = "Alice->Bob->10"
    difficulty = 4
    start_time = time.time()
    block_number = 1
    previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"
    mined_hash = mine(block_number, transactions, previous_hash, difficulty)
    total_time = time.time() - start_time
    print(f"Mining completed successfully in {total_time:.2f} seconds")
    print(f"Mined hash value: {mined_hash}")
