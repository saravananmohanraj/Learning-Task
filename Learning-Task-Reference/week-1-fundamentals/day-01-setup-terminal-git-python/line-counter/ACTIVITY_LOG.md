About script:
-> Python script reads a text file and counts exactly how many lines contains a specific target word.

Flow for script:
1. The script takes two inputs from the user: the file path and the target word to search for.
2. It initializes a counter variable at 0.
3. It opens the text file in read mode.
4. It loops through the file one line at a time.
5. For each line, it checks if the target word is present. If it is, the counter goes up by 1.

Why this?
-> Using above one, easily count the specific words like automating the process.
-> Without this, manual work occurs and will take more time to find it.

How will i know it is working or not? what i have checked.
-> By running automated unit tests using pytest for two specific scenarios.
-> First, it increments the count of the word if this is there. Second, it is safely returns 0 if not there.

Output:

line_counter.py

C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\line-counter>python line_counter.py sample.txt spark
3

test_line_counter.py
C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\line-counter>pytest test_line_counter.py -v
C:\Users\Orcon\AppData\Local\Programs\Python\Python310\lib\site-packages\pytest_asyncio\plugin.py:207: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
================================================= test session starts =================================================
platform win32 -- Python 3.10.11, pytest-8.3.4, pluggy-1.6.0 -- C:\Users\Orcon\AppData\Local\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Orcon\Downloads\Learning-Task-Reference\Learning-Task-Reference\week-1-fundamentals\day-01-setup-terminal-git-python\line-counter
plugins: anyio-4.11.0, Faker-22.0.0, langsmith-0.4.55, asyncio-0.25.0
asyncio: mode=strict, asyncio_default_fixture_loop_scope=None
collected 2 items

test_line_counter.py::test_word_found_multiple_times PASSED                                                      [ 50%]
test_line_counter.py::test_word_not_found PASSED                                                                 [100%]

================================================== 2 passed in 0.38s ==================================================

