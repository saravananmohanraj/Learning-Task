About env:
-> System for creating isolated python workspaces so package versions don't conflicts across projects,
-> paired with testing framework that automaticaaly runs and verification code.

Flow:
1. python -m venv creates a folder containing a standalone Python binary. 
2. Activating it modifies your shell's PATH to use that binary instead of the system Python. 
3. pytest then scans directories for files named test_*.py.
4. Executes any functions inside them starting with test_.

Why env?
-> Without virtual environments, updating a package for one project might break another project sharing the global python installations.
-> Without pytest, developers would have to manually execute every test script and visually inspect prints to verify logic.

How will i know it's working?
-> Running which python will point to the environment's folder rather than the global installation.
-> pip list will show only isolated packages.
-> pytest will output a summary of passed and failed test cases.


Execution logs:

1. Python venv, activation
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ which python
/c/Users/Orcon/AppData/Local/Programs/Python/Python312/python


SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ source .venv/Scripts/activate
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ pip list
Package                   Version
------------------------- --------
annotated-types           0.8.0
anyio                     4.16.0
attrs                     26.1.0
cffi                      2.1.1
claude-agent-sdk          0.2.176
click                     8.5.0
cryptography              50.0.2
h11                       0.16.0
httpcore2                 2.16.0
httpx2                    2.16.0
idna                      3.20
jsonschema                4.26.0
jsonschema-specifications 2025.9.1
mcp                       2.3.0
mcp-types                 2.3.0
opentelemetry-api         1.45.2
pip                       25.0.1
pycparser                 3.12
pydantic                  2.14.2
pydantic_core             2.50.2
PyJWT                     2.15.1
python-multipart          0.0.33
pywin32                   312
referencing               0.37.0
rpds-py                   2026.9.1
sniffio                   1.3.1
sse-starlette             3.6.0
starlette                 1.10.0
truststore                0.10.5
typing_extensions         4.16.0
typing-inspection         0.4.4
uvicorn                   0.54.0
(.venv)


SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ pip install requests
Collecting requests
  Using cached requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Downloading charset_normalizer-3.5.2-cp312-cp312-win_amd64.whl.metadata (47 kB)
Requirement already satisfied: idna<4,>=2.5 in c:\users\orcon\appdata\local\programs\python\python312\lib\site-packages (from requests) (3.20)
Collecting urllib3<3,>=1.26 (from requests)
  Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
Collecting certifi>=2023.5.7 (from requests)
  Downloading certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)
Using cached requests-2.34.2-py3-none-any.whl (73 kB)
Downloading certifi-2026.10.23-py3-none-any.whl (135 kB)
Downloading charset_normalizer-3.5.2-cp312-cp312-win_amd64.whl (207 kB)
Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)
Installing collected packages: urllib3, charset_normalizer, certifi, requests
Successfully installed certifi-2026.10.23 charset_normalizer-3.5.2 requests-2.34.2 urllib3-2.8.0

[notice] A new release of pip is available: 25.0.1 -> 26.2.2
[notice] To update, run: C:\Users\Orcon\AppData\Local\Programs\Python\Python312\python.exe -m pip install --upgrade pip
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ pip freeze > requirements.txt
(.venv)


SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ cat requirements.txt
annotated-types==0.8.0
anyio==4.16.0
attrs==26.1.0
certifi==2026.10.23
cffi==2.1.1
charset-normalizer==3.5.2
claude-agent-sdk==0.2.176
click==8.5.0
cryptography==50.0.2
h11==0.16.0
httpcore2==2.16.0
httpx2==2.16.0
idna==3.20
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
mcp==2.3.0
mcp-types==2.3.0
opentelemetry-api==1.45.2
pycparser==3.12
pydantic==2.14.2
pydantic_core==2.50.2
PyJWT==2.15.1
python-multipart==0.0.33
pywin32==312
referencing==0.37.0
requests==2.34.2
rpds-py==2026.9.1
sniffio==1.3.1
sse-starlette==3.6.0
starlette==1.10.0
truststore==0.10.5
typing-inspection==0.4.4
typing_extensions==4.16.0
urllib3==2.8.0
uvicorn==0.54.0
(.venv)

2. Running a module vs running a file:

echo "print('Hello from the script')" > hello.py
python hello.py
python -m hello

python file.py runs by exact file path, while python -m module searches the Python environment path for the module name.

3. Pytest dicovery rules:

SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ pytest product/tests/test_landing_contract.py -q
.........................................................                                                                                                            [100%]
57 passed in 0.11s
(.venv)


SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ pytest product/tests/test_landing_contract.py -v
=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.7.0 -- C:\Saturam\saturam-agent-framework\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Saturam\saturam-agent-framework\product
configfile: pyproject.toml
plugins: anyio-4.16.0, platformdirs-4.14.5, asyncio-1.4.0, cov-7.1.0, mock-3.15.1, timeout-2.4.0, xdist-3.8.0, typeguard-4.6.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 57 items

product\tests\test_landing_contract.py::test_schema_rejects_empty_stream_id PASSED                                                                                   [  1%]
product\tests\test_landing_contract.py::test_schema_rejects_empty_key_columns PASSED                                                                                 [  3%]
product\tests\test_landing_contract.py::test_schema_rejects_key_column_not_in_required PASSED                                                                        [  5%]
product\tests\test_landing_contract.py::test_schema_rejects_watermark_not_in_required PASSED                                                                         [  7%]
product\tests\test_landing_contract.py::test_schema_rejects_nullable_key_or_watermark PASSED                                                                         [  8%]
product\tests\test_landing_contract.py::test_schema_rejects_nullable_column_not_required PASSED                                                                      [ 10%]
product\tests\test_landing_contract.py::test_schema_rejects_timestamp_column_not_required PASSED                                                                     [ 12%]
product\tests\test_landing_contract.py::test_schema_rejects_watermark_in_timestamp_columns PASSED                                                                    [ 14%]
product\tests\test_landing_contract.py::test_schema_rejects_superseded_watermark_equal_to_watermark PASSED                                                           [ 15%]
product\tests\test_landing_contract.py::test_schema_rejects_superseded_watermark_not_required PASSED                                                                 [ 17%]
product\tests\test_landing_contract.py::test_landing_schemas_is_immutable PASSED                                                                                     [ 19%]
product\tests\test_landing_contract.py::test_session_replay_watermark_is_last_updated_not_session_start PASSED                                                       [ 21%]
product\tests\test_landing_contract.py::test_validate_row_accepts_both_pulls_of_a_corrected_session_replay_row PASSED                                                [ 22%]
product\tests\test_landing_contract.py::test_validate_row_rejects_malformed_non_watermark_timestamp_column[session_replay.session-row0-session_start_at] PASSED      [ 24%]
product\tests\test_landing_contract.py::test_validate_row_rejects_malformed_non_watermark_timestamp_column[crm.deal_stage_history-row1-entered_at] PASSED            [ 26%]
product\tests\test_landing_contract.py::test_validate_row_distinguishes_pre_1_1_0_session_replay_row_from_malformed PASSED                                           [ 28%]
product\tests\test_landing_contract.py::test_validate_row_reports_generic_missing_watermark_when_no_superseded_value PASSED                                          [ 29%]
product\tests\test_landing_contract.py::test_validate_row_rejects_non_mapping_row PASSED                                                                             [ 31%]
product\tests\test_landing_contract.py::test_validate_row_rejects_non_scalar_key_value[bad_value0] PASSED                                                            [ 33%]
product\tests\test_landing_contract.py::test_validate_row_rejects_non_scalar_key_value[bad_value1] PASSED                                                            [ 35%]
product\tests\test_landing_contract.py::test_validate_row_rejects_non_string_key_value[True] PASSED                                                                  [ 36%]
product\tests\test_landing_contract.py::test_validate_row_rejects_non_string_key_value[12345] PASSED                                                                 [ 38%]
product\tests\test_landing_contract.py::test_validate_row_rejects_non_string_key_value[3.14] PASSED                                                                  [ 40%]
product\tests\test_landing_contract.py::test_validate_row_treats_blank_string_like_null PASSED                                                                       [ 42%]
product\tests\test_landing_contract.py::test_validate_row_rejects_blank_key_value PASSED                                                                             [ 43%]
product\tests\test_landing_contract.py::test_validate_row_does_not_double_report_blank_key_and_watermark_column PASSED                                               [ 45%]
product\tests\test_landing_contract.py::test_validate_row_does_not_double_report_key_and_watermark_column PASSED                                                     [ 47%]
product\tests\test_landing_contract.py::test_validate_row_does_not_double_report_non_scalar_key_and_watermark_column PASSED                                          [ 49%]
product\tests\test_landing_contract.py::test_validate_row_still_checks_watermark_parseability_when_also_a_key PASSED                                                 [ 50%]
product\tests\test_landing_contract.py::test_validate_row_rejects_naive_watermark_timestamp PASSED                                                                   [ 52%]
product\tests\test_landing_contract.py::test_validate_row_rejects_non_utc_offset_watermark_timestamp PASSED                                                          [ 54%]
product\tests\test_landing_contract.py::test_non_utc_offset_timestamp_sorts_lexically_wrong_against_a_z_suffixed_one PASSED                                          [ 56%]
product\tests\test_landing_contract.py::test_validate_row_accepts_a_conforming_row PASSED                                                                            [ 57%]
product\tests\test_landing_contract.py::test_validate_row_reports_missing_required_column PASSED                                                                     [ 59%]
product\tests\test_landing_contract.py::test_validate_row_rejects_non_scalar_required_column_value PASSED                                                            [ 61%]
product\tests\test_landing_contract.py::test_validate_row_rejects_non_scalar_required_column_value_on_session_replay PASSED                                          [ 63%]
product\tests\test_landing_contract.py::test_validate_row_requires_brand_on_deal PASSED                                                                              [ 64%]
product\tests\test_landing_contract.py::test_validate_row_rejects_null_brand_on_deal PASSED                                                                          [ 66%]
product\tests\test_landing_contract.py::test_validate_row_accepts_null_quote_request_source_url_on_deal PASSED                                                       [ 68%]
product\tests\test_landing_contract.py::test_validate_row_suppresses_defect_for_nullable_column PASSED                                                               [ 70%]
product\tests\test_landing_contract.py::test_validate_row_reports_missing_identity_key PASSED                                                                        [ 71%]
product\tests\test_landing_contract.py::test_resolve_stream_id_rejects_non_mapping_row PASSED                                                                        [ 73%]
product\tests\test_landing_contract.py::test_resolve_stream_id_rejects_missing_or_unknown_record_type PASSED                                                         [ 75%]
product\tests\test_landing_contract.py::test_resolve_stream_id_single_stream_sources_ignore_row_content PASSED                                                       [ 77%]
product\tests\test_landing_contract.py::test_landing_path_rejects_naive_datetime PASSED                                                                              [ 78%]
product\tests\test_landing_contract.py::test_landing_path_is_stable_across_input_timezones PASSED                                                                    [ 80%]
product\tests\test_landing_contract.py::test_parse_landing_path_rejects_adversarial_input[raw/crm/dt=2026-09-01/analytics-20260901T060000Z.ndjson] PASSED            [ 82%]
product\tests\test_landing_contract.py::test_parse_landing_path_rejects_adversarial_input[raw/../../etc/passwd] PASSED                                               [ 84%]
product\tests\test_landing_contract.py::test_parse_landing_path_rejects_adversarial_input[raw/CRM/dt=2026-09-01/CRM-20260901T060000Z.ndjson] PASSED                  [ 85%]
product\tests\test_landing_contract.py::test_parse_landing_path_rejects_adversarial_input[raw/quantum/dt=2026-09-01/quantum-20260901T060000Z.ndjson] PASSED          [ 87%]
product\tests\test_landing_contract.py::test_parse_landing_path_rejects_adversarial_input[raw/crm/dt=2026-09-01/crm-20260901T060000Z.csv] PASSED                     [ 89%]
product\tests\test_landing_contract.py::test_parse_landing_path_rejects_adversarial_input[raw/crm/dt=2026-09-01/crm-2026-09-01T06:00:00Z.ndjson] PASSED              [ 91%]
product\tests\test_landing_contract.py::test_parse_landing_path_rejects_adversarial_input[raw/crm/dt=2026-13-40/crm-20260901T060000Z.ndjson] PASSED                  [ 92%]
product\tests\test_landing_contract.py::test_parse_landing_path_rejects_adversarial_input[not/even/the/right/shape.ndjson] PASSED                                    [ 94%]
product\tests\test_landing_contract.py::test_parse_landing_path_rejects_adversarial_input[] PASSED                                                                   [ 96%]
product\tests\test_landing_contract.py::test_parse_landing_path_round_trips_landing_path PASSED                                                                      [ 98%]
product\tests\test_landing_contract.py::test_landing_fixtures_are_covered_by_package_data_glob PASSED                                                                [100%]

=========================================================================== 57 passed in 0.13s ============================================================================
(.venv)


SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ pytest product/tests/test_landing_contract.py -k "naive"
=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.7.0
rootdir: C:\Saturam\saturam-agent-framework\product
configfile: pyproject.toml
plugins: anyio-4.16.0, platformdirs-4.14.5, asyncio-1.4.0, cov-7.1.0, mock-3.15.1, timeout-2.4.0, xdist-3.8.0, typeguard-4.6.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 57 items / 55 deselected / 2 selected

product\tests\test_landing_contract.py ..                                                                                                                            [100%]

==================================================================== 2 passed, 55 deselected in 0.05s =====================================================================
(.venv)


SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ pytest product/tests/test_landing_contract.py -q
................................F........................                                                                                                            [100%]
================================================================================ FAILURES =================================================================================
_______________________________________________________________ test_validate_row_accepts_a_conforming_row ________________________________________________________________

    def test_validate_row_accepts_a_conforming_row():
        row = {
            "record_type": "contact",
            "object_id": "c_500",
            "last_modified_at": "2026-09-01T07:00:00Z",
            "email": "a@example.com",
            "brand": "Blodgett",
            "identity_key": None,
        }
>       assert validate_row("crm.contact", row) == (fake_error,)
                                                    ^^^^^^^^^^
E       NameError: name 'fake_error' is not defined

product\tests\test_landing_contract.py:511: NameError
========================================================================= short test summary info =========================================================================
FAILED product\tests\test_landing_contract.py::test_validate_row_accepts_a_conforming_row - NameError: name 'fake_error' is not defined
1 failed, 56 passed in 0.22s
(.venv)
