About:
-> It is an automated setup script that creates a fresh, isolated Python virtual environment and links our local project packages together so we can developing and testing.

Flow:
1. Check requirements ( needs uv, no active .venv)
2. Delete old .venv
3. Create new .venv using python 3.12
4. Install the local egpt, agno & product libraries in editable mode
5. Print the activation commands.

Why this?
-> Ensure every developer works in exact same environment.
-> we would pollute our global system Python, deal with missing dependencies, or struggle with ModuleNotFoundErrors

How will i know it's working?
-> It is working when the .venv folder exists, activates without errors, and running pytest product/tests/test_landing_contract.py -q successfully executes and passes the tests.

Execution logs:

SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ pytest product/tests/test_landing_contract.py -q
.........................................................                                                                                                            [100%]
57 passed in 0.26s
(.venv)

Problems faced during execution:
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ ./scripts/dev_setup.sh


     █████╗  ██████╗ ███╗   ██╗ ██████╗
    ██╔══██╗██╔════╝ ████╗  ██║██╔═══██╗
    ███████║██║  ███╗██╔██╗ ██║██║   ██║
    ██╔══██║██║   ██║██║╚██╗██║██║   ██║
    ██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝

    Development Setup

    Removing old environment...
    > rm -rf /c/Saturam/saturam-agent-framework/.venv

    Creating Python 3.12 venv...
    > uv venv /c/Saturam/saturam-agent-framework/.venv --python 3.12

    Installing egptctl[dev], egpt[dev] and egpt-retail[dev] in editable mode...
    > uv pip install -e libs/egptctl[dev] -e libs/agno[dev] -e product[dev]
error: Distribution not found at: file:///C:/c/Saturam/saturam-agent-framework/libs/egptctl

-> Git Bash converts the working directory to a Unix-style path (`/c/Saturam/...`). When it passes this absolute path to `uv` (a native Windows executable), `uv` incorrectly prepends `C:/` to it, creating a broken, nonexistent path.
-> The script successfully created the `.venv` folder before crashing. I bypassed the absolute path bug by activating the environment manually and running the `uv pip install` command using relative paths:

Commands used:
source .venv/Scripts/activate
uv pip install -e libs/egptctl[dev] -e libs/agno[dev] -e product[dev]


About project-step up:

dev_setup.sh:
The script automates the creation of a clean Python workspace so you do not have to configure it manually
1. Verifies that you have the uv package manager installed and ensures you are not already inside an active virtual environment.
2. Deletes any existing .venv folder in the project directory to prevent conflicts from old setups.
3. Uses uv to build a brand new Python 3.12 virtual environment.
4. Installs the project's three internal libraries (egptctl, agno, and product) along with their development tools (like pytest) in "editable" mode (-e). 
5. This means any code changes you make to the files take effect immediately without needing reinstallation.