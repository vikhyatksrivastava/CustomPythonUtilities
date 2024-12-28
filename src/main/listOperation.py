def combine_unused_words(list1, list2):
  """Combines unused words from two lists into a single string.

  Args:
    list1: The first list of words.
    list2: The second list of words.

  Returns:
    A string containing the unused words from both lists.
  """

  set1 = set(list1)
  set2 = set(list2)

  unused_words = set1.symmetric_difference(set2)
  # symmetric_difference() gives elements that are in either set1 or set2, but not both

  return ' '.join(unused_words)

# Example usage:
words1 = ["hello", "world", "python", "is", "fun"]
words2 = ["hello", "programming", "is", "awesome"]

result_string = combine_unused_words(words1, words2)
print(result_string)  # Output: world fun python programming awesome