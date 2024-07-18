from passlib.hash import sha256_crypt


class Hash:
    
    def hash(value:str):
        value = value.encode('utf-8') 
        hash_value = sha256_crypt.hash(value)
        
        print(f"hash value = {hash_value}")
        return hash_value

    
if __name__ == "__main__":
    print(Hash.hash("1234"))