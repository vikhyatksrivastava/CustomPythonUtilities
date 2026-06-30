# Hash cracker: attempts to find the original text for a given hash using a wordlist
import hashlib

def crack_hash(hash_string, hash_type, wordlist_path):
	"""
	Attempts to find the original text for a given hash using a wordlist.
	:param hash_string: The hash string to crack
	:param hash_type: The hash algorithm (e.g., 'md5', 'sha1', 'sha256')
	:param wordlist_path: Path to the wordlist file
	:return: The original text if found, else None
	"""
	try:
		hash_func = getattr(hashlib, hash_type)
	except AttributeError:
		print(f"Unsupported hash type: {hash_type}")
		return None

	with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
		for line in f:
			word = line.strip()
			if not word:
				continue
			hashed_word = hash_func(word.encode('utf-8')).hexdigest()
			if hashed_word == hash_string:
				return word
	return None

if __name__ == "__main__":
	# Example usage
	hash_string = input("Enter the hash string: ").strip()
	hash_type = input("Enter the hash type (md5, sha1, sha256, etc.): ").strip().lower()
	wordlist_path = input("Enter the path to the wordlist file: ").strip()
	result = crack_hash(hash_string, hash_type, wordlist_path)
	if result:
		print(f"Original text found: {result}")
	else:
		print("Original text not found in wordlist.")
