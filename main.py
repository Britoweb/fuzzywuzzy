## importing the module from the fuzzywuzzy library
from fuzzywuzzy import fuzz
## 100 for same strings
print(f"Equal Strings:- {fuzz.ratio('tutorialspoint', 'tutorialspoint')}")
## random score for slight changes in the strings
print(f"Slight Changed Strings:- {fuzz.ratio('tutorialspoint', 'TutorialsPoint')}")
print(f"Slight Changed Strings:- {fuzz.ratio('tutorialspoint', 'Tutorials Point')}"
)
## complete different strings
print(f"Different Strings:- {fuzz.ratio('abcd', 'efgh')}")