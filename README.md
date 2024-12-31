ApprenticeshipLearning
Learning: Python, SQL, React

# Entry Level

1.  Python Data Essentials: Python Intorduction - Pluralsight - Faisal Memon on Pluralsight - 24/12/24

    - Data Structures
    - Operators
    - Packages

                 ## Python and Data Science
                          - What is Python
                          - Features of Python
                          - Packages available for Data Science: NumPy, Matplotlib, Pandas, SciPy,
                          - Why Python is Preferred for Data Science?
                          - Jupyter Notebook

                 ## Basic Python
                          - Python Identifiers and Literals
                          - Overviwe of Identifiers
                          - What are Literals and their types
                          - Expression and Operators
                          - What are they
                          - Different types of Operators (arithmetic(-+-/%//*), comparison(<=>), logical (-and, or, not))

                ## Python Packages and Data Structures
                          - What are Packages
                          - How can we use Packages
                          - Python Data structures
                          - What are lists in Python
                          - Tuples
                          - Sets

---

2.  Python3: The Big Picture - Pluralsight - Jason Olson - 30/12/2024

    - Pythons desing philosphy
    - Explore Python itself
    - Pros and cons of Python

                 ## Why Python?
                            - Simple to learn
                            - Simple to use
                            - Great Community
                            - Widely used
                            - High demand
                 ## What is Python?
                            - Syntax - white spce
                            - General -purpose
                            - Multi-paradigm
                            - Interpreted
                            - Garbage-collected
                            - Dynamically-typed
                 ## Pros and Cons
                            - Pros: Comprehensive Standard Library, Community - driven, 3rd Party Libraries, 3rd Party Tools,
                            - Cons: Interpreted (makes it slow), Not Native(mobile and webrowser usage is limited), Dynamic(runtime errors)

---

3.  Python Basics and Data Structure - Pluralsight - Lab - 30/12/24

    - Building a digital cookbook app
    - Data Types
    - Designing the Recipe Data Structure (name, ingredients, instructions)
    - Putting it all together

                 ## Listing recipes
                          - for loops: listing the entire recipe book recipe by recipe
                 ## Query recipes(searching for recipe by name)
                          - upon execution, the user will be promped to enter a recipe name. The goal is to filter the existing recipes and retrieve those that match the user-provided name, populating the results into the found_recipes variable
                 ## Searching by ingredients

---

4.  Python Standard Library - Pluralsight - Lab - 30/12/24

    - Understand data serialization and its importance
    - Explore the Pickle module in Python for data serialisation
    - Implement and handle errors during pickling and unpickling
    - Enhance a recipe book application for data persistence between sessions

                 ## Data Serialization
                            -  The process of converting in - memory objects into a format that can be saved to disk or transmitted over a network, and later reconstructed.
                 ## Pickle Module
                            - A Python module that provides functionalities for serializing and deserializing Python objects
                 ## Implementing Load and Save Functions
                            - Created functions to handle the loading and saving of data to ensure the persistence of application state.
                 ## Pickling without a File
                            - How to serialize and deserialize data to and from bytes objects, which is useful in scenarios such as network transmission or database storage
                 ## Modifying the Main Function
                            - Incorporrated loading and saving recipes in the main function to ensure data persistence across different runs of the application

---

5.  Build a Library System with Python - Pluralsight - Lab - 30/12/24

    - In this hands-on project, we will construct an object-oriented "library system" with Python
    - We design 3 core classes: Book, Borrower and Library to stimulate fundamental librery operations, such as adding books, schecking out, and returning items.
    - Interactions between objects: as we developed these classes, we had also implement methods that allow these objects to interact.

---

6.  Regex Foundations and Essentials - Pluralsight - Lab - 31/12/24

    - Understanding the foundations of Regex and how to implement it in the pythoon programming language
    - Regex is a short regular expressions and it's a means of creating a pattern that can be used to match a specific type fo data. Example: phone number. Using Regex we can take any piece of information with a distinct pattern and create code that can parse data and collect anything matching that pattern.

      - Exercises:

        - First_Scripts
        - Input_Validation
        - Log_Search
        - Filtered_Log_Data
        - Final_Project

                 ## Common Matching Pattern
                            - \d: This caharacter matches any digit [0-9]
                            - \w: Matches any word character [a-z or A-Z]
                            - \s: Any white space character
                 ## Common Quantitative Patterns
                            - '+': Matches one or more of a pattern. E.g \d+means one or more digits
                            - '?': Means zero or one of a pattern
                            - '*': Means zero or more of a pattern
                 ## Escape Characters

    [REGEX]
    (https://regex101.com)

    The list of Regex: Certainly! Below is a list of common regex metacharacters and character classes used in Python regular expressions, similar to `\d`, `\s`, and `\w`.

### Common Regex Metacharacters and Character Classes:

1. **`\d`**: Matches any digit, equivalent to `[0-9]`.
2. **`\D`**: Matches any non-digit character, equivalent to `[^0-9]`.
3. **`\s`**: Matches any whitespace character (space, tab, newline, etc.), equivalent to `[ \t\n\r\f\v]`.
4. **`\S`**: Matches any non-whitespace character, equivalent to `[^ \t\n\r\f\v]`.
5. **`\w`**: Matches any word character (alphanumeric and underscore), equivalent to `[a-zA-Z0-9_]`.
6. **`\W`**: Matches any non-word character, equivalent to `[^a-zA-Z0-9_]`.

### Additional Useful Metacharacters and Character Classes:

7. **`.`**: Matches any character except a newline.
8. **`^`**: Matches the start of the string.
9. **`$`**: Matches the end of the string.
10. **`\b`**: Matches a word boundary.
11. **`\B`**: Matches a non-word boundary.
12. **`\A`**: Matches the start of the string (similar to `^` but not affected by multiline mode).
13. **`\Z`**: Matches the end of the string (similar to `$` but not affected by multiline mode).
14. **`\`**: Escapes a special character, allowing it to be used as a literal character.

### Quantifiers:

15. **`*`**: Matches 0 or more repetitions of the preceding pattern.
16. **`+`**: Matches 1 or more repetitions of the preceding pattern.
17. **`?`**: Matches 0 or 1 repetition of the preceding pattern.
18. **`{n}`**: Matches exactly `n` repetitions of the preceding pattern.
19. **`{n,}`**: Matches `n` or more repetitions of the preceding pattern.
20. **`{n,m}`**: Matches between `n` and `m` repetitions of the preceding pattern.

### Groups and Alternation:

21. **`(abc)`**: Matches the exact string "abc".
22. **`(a|b|c)`**: Matches any one of the alternatives, "a", "b", or "c".
23. **`(?:...)`**: Non-capturing group, groups the pattern without capturing.
24. **`(?P<name>...)`**: Named capturing group, captures the matched text into a group named `name`.

### Lookahead and Lookbehind:

25. **`(?=...)`**: Positive lookahead, asserts that what follows the position is `...`.
26. **`(?!...)`**: Negative lookahead, asserts that what follows the position is not `...`.
27. **`(?<=...)`**: Positive lookbehind, asserts that what precedes the position is `...`.
28. **`(?<!...)`**: Negative lookbehind, asserts that what precedes the position is not `...`.

### Character Classes:

29. **`[abc]`**: Matches any one of the characters "a", "b", or "c".
30. **`[^abc]`**: Matches any character except "a", "b", or "c".
31. **`[a-z]`**: Matches any character in the range "a" to "z".
32. **`[A-Z]`**: Matches any character in the range "A" to "Z".
33. **`[0-9]`**: Matches any digit in the range "0" to "9".

### Escape Sequences for Special Characters:

34. **`\n`**: Matches a newline character.
35. **`\r`**: Matches a carriage return character.
36. **`\t`**: Matches a tab character.
37. **`\f`**: Matches a form feed character.
38. **`\v`**: Matches a vertical tab character.
39. **`\xhh`**: Matches the character with the hexadecimal value `hh`.
40. **`\uhhhh`**: Matches the Unicode character with the hexadecimal value `hhhh`.

These metacharacters and character classes are the building blocks of regular expressions in Python. They allow you to create powerful patterns for matching and manipulating text.
