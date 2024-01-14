# README for regex.py

This Python script, `regex.py`, demonstrates the use of regular expressions (regex) in Python using the `re` module. It includes several examples of different regex patterns and how they match strings.

Here's a brief overview of the examples:

1. **Exact Match**: The script first demonstrates an exact match, searching for the letter 'm' in a string.

2. **Start of String Match**: The script then shows how to search for a match at the start of a string.

3. **Alternation and Repetition**: The next example demonstrates the use of alternation (P|p) and repetition (+) in a regex. It searches for the word "Pablo" with any number of 'o' characters at the end, and can match either "Pablo" or "pablo".

4. **Search Anywhere**: The script then uses `re.search()` to find a match anywhere in the string. It looks for one or more 'm' or 'M' characters.

5. **End of String Match**: The script shows how to search for a match at the end of a string using the dollar sign ($).

6. **Start of String Match**: The script also demonstrates how to search for a match at the beginning of a string using the caret (^).

7. **Wildcard Character**: Finally, the script demonstrates the use of the dot (.) as a wildcard character that can match any character.

Each example prints the result of the regex search to the console.

Please note that this script is for educational purposes and demonstrates basic usage of regular expressions in Python. For more complex regex patterns, please refer to Python's `re` module documentation or other regex resources.
