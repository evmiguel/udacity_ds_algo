import hashlib, datetime
from datetime import timezone

class Block:
    def __init__(self, timestamp, data, previous_hash, previous=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous = previous
    
    def calc_hash(self):
        sha = hashlib.sha256()
        str_to_encode = str(self.data)+self.previous_hash if self.previous_hash else str(self.data)
        hash_str = (str_to_encode).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return 'Timestamp: {}, Data: {}, Previous Hash: {}, Hash: {}'.format(self.timestamp, self.data, self.previous_hash if self.previous_hash else self.previous_hash, self.hash)

class Blockchain:
    def __init__(self, root=None):
        self.root = root
    
    def add_block(self, data):
        if self.root is None:
            self.root = Block(datetime.datetime.now(tz=timezone.utc), data, None, None)
            return
        else:
            self.root = Block(datetime.datetime.now(tz=timezone.utc), data, self.root.hash, self.root)
            

    def print(self):
        current = self.root
        while current is not None:
            print(current)
            current = current.previous
        

if __name__ == '__main__':
    blockchain = Blockchain()

    # Test case
    blockchain.add_block('first node')
    blockchain.add_block('second node')
    blockchain.add_block('third node')
     # This function prints the whole chain
    blockchain.print()

    # Timestamp: 2021-01-12 03:44:20.285354+00:00, Data: third node, Previous Hash: 1a7ff20f98655b2d639988ac50ea0f738e8f5d3558e41ffff409adbdf6d9e68e, Hash: d59a604e32bebbe2af057fc62d97a2396b7af319afa7370ab9d034f0918dc2c2
    # Timestamp: 2021-01-12 03:44:20.285346+00:00, Data: second node, Previous Hash: b8a3b979a9ede2dbec6abaa7e12f6b3d2b9bb3cf342a7d593b508ad4d25d8413, Hash: 1a7ff20f98655b2d639988ac50ea0f738e8f5d3558e41ffff409adbdf6d9e68e
    # Timestamp: 2021-01-12 03:44:20.285061+00:00, Data: first node, Previous Hash: None, Hash: b8a3b979a9ede2dbec6abaa7e12f6b3d2b9bb3cf342a7d593b508ad4d25d8413

    print()

    # Edge case - replace timestamp. This implementation supports this
    old_timestamp = blockchain.root.previous.timestamp
    blockchain.root.previous.timestamp = blockchain.root.timestamp
    blockchain.print()
    # Timestamp: 2021-01-13 16:08:41.467270+00:00, Data: third node, Previous Hash: 1a7ff20f98655b2d639988ac50ea0f738e8f5d3558e41ffff409adbdf6d9e68e, Hash: d59a604e32bebbe2af057fc62d97a2396b7af319afa7370ab9d034f0918dc2c2
    # Timestamp: 2021-01-13 16:08:41.467270+00:00, Data: second node, Previous Hash: b8a3b979a9ede2dbec6abaa7e12f6b3d2b9bb3cf342a7d593b508ad4d25d8413, Hash: 1a7ff20f98655b2d639988ac50ea0f738e8f5d3558e41ffff409adbdf6d9e68e
    # Timestamp: 2021-01-13 16:08:41.467093+00:00, Data: first node, Previous Hash: None, Hash: b8a3b979a9ede2dbec6abaa7e12f6b3d2b9bb3cf342a7d593b508ad4d25d8413

    print()

    # Edge case - set all fields of previous node to None. The chain effectively ends here.
    node = blockchain.root.previous
    blockchain.root.previous.timestamp = None
    blockchain.root.previous.data = None
    blockchain.root.previous.previous_hash = None
    blockchain.root.previous.previous = None
    blockchain.root.previous.hash = None
    blockchain.print()



    
