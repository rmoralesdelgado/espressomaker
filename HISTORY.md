
<h2>Release History</h2>

### v0.1a1

Basic skeleton of the package ready for shipping to TestPyPI.

### v0.1a2

* Automated file exporting from .ipynb to .py and standardized the formatting.
* Automated file exporting from .ipynb to .md and standardized the formatting.
* Improved variable handling on instance methods.
* Added a message for the user to recognize the current kernel when using opentabs().
* Added debugging tracers for all private methods.
* Finished class- and static- methods docstrings.
* Updated setup.py.

### v0.1b1

* Improved HISTORY.md title formatting.
* Updated "classifiers" of setup.py.
* Changed opentabs() classmethod to check() in espresso.py.
* Successfully ran manual tests in all APIs.

### v0.1b2

* Added PyPI version and GitHub issues badges to README.md.
* Ran installation test using `$ pip install espressomaker`.
* Added config() classmethod to allow user modify Espresso class-level settings. Returns current settings.
* Added parameters to shot() and opentab() to allow user override "display_on" class-level setting.
* Repositioned status retrieval in closetab() classmethod.
* Added return message for killall() staticmethod.
* Added atexit.register call to closetab() (to be used when using opentab() in a .py script and not using closetab() at the end; however, killing the parent process should kill the "caffeinate" subprocess anyway).
* Finished User Guide in README.md.

### v0.1rc1
* Corrected numbering and hrefs on README.md to work correctly on GitHub.

### TODO

* Finish unittest.
