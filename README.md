# How it's working?
As input, function takes 1 or 2 variables, depends on version. 
In both examples, You need to provide path to JSON file.
In second version, extra variable is integer with number of 
statement. I read that it's possible to have multiple policies
in one file and i decide to treat this as one of the edge cases.
</br> With variables provided, function returns False when field
"Resouces" contains is '*' and True in any other case. 
</br> Also, it should print some extra informations if something
is wrong with file: for example if it's format is wrong or some 
fields are missing.


# How to run code?
1. Clone repository.
2. Open terminal in main catalogue of project.
3. Run one of the following commands:
</br>
</br> If you want to check policy for standard file (with 1 policy) or just first policy, try:

```console
python.exe .\One_statement.py --File PATH
```

If You have muliple policies and want to check one of them, try:

```console
python.exe .\Many_statements.py --File PATH --Stat POLICY_NUMBER
```
# Unit tests and edge cases

I decided to provide two types of unit tests. First were those with random 
inputs in "Resource" field ("monkey testing"). Code for them is in *random_unit_tests.py*.
</br> Also, I do some test for edge cases. JSON files for them are in *Edge_cases_test*.
Code for this test is in *Edge_cases.py* file. Those edge cases were:
- Asterisk saved in binary ASCII,
- Empty file,
- Empty Resource field,
- Many asterisks,
- Wrong file structure (something is missing),
- Very long input.
</br>Unit tests are manual in this example. I decided to write them because
there is only one function and input. I saw only few edge cases and generally, in
this particular situation they didn't take a lot of time.
