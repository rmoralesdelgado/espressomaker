
# espressomaker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`espressomaker` is a Python module that provides a context manager (and other functionalities) to modify the power management settings on a MacOS X system so that running processes (e.g. a machine learning training algorithm) can run uninterruptedly.

More specifically, `espressomaker` is a wrapper of `caffeinate`, a shell command in MacOS X distributions that allows users to create assertions that alter the system's sleep behavior. In this sense. `espressomaker` runs `caffeinate` subprocesses from the Python 3 or iPython kernel from which `espressomaker` is being executed and allows to control them through a simple and intuitive set of Python commands.

<h2>Table of Contents<span class="tocSkip"></span></h2>
<div class="toc"><ul class="toc-item"><li><span><a href="#1-Quick-Start" data-toc-modified-id="1.-Quick-Start-1">1. Quick Start</a></span></li><li><span><a href="#2-Purpose" data-toc-modified-id="2.-Purpose-2">2. Purpose</a></span></li><li><span><a href="#3-Installation" data-toc-modified-id="3.-Installation-3">3. Installation</a></span></li><li><span><a href="#4-User-guide" data-toc-modified-id="4.-User-guide-4">4. User-guide</a></span><ul class="toc-item"><li><span><a href="#41-Working-principle" data-toc-modified-id="4.1-Working-principle-4.1">4.1 Working principle</a></span></li><li><span><a href="#42-Importing-the-module" data-toc-modified-id="4.2-Importing-the-module-4.2">4.2 Importing the module</a></span></li><li><span><a href="#43-Using-as-a-context-manager-(Espresso.shot())" data-toc-modified-id="4.3-Using-as-a-context-manager-(Espresso.shot())-4.3">4.3 Using as a context manager (<code>Espresso.shot()</code>)</a></span></li><li><span><a href="#44-Manually-opening-and-closing-tabs" data-toc-modified-id="4.4-Manually-opening-and-closing-tabs-4.4">4.4 Manually opening and closing tabs</a></span></li><li><span><a href="#45-Viewing-open-tabs" data-toc-modified-id="4.5-Viewing-open-tabs-4.5">4.5 Viewing open tabs</a></span></li><li><span><a href="#46-Killing-all-caffeinate-processes" data-toc-modified-id="4.6-Killing-all-caffeinate-processes-4.6">4.6 Killing all <code>caffeinate</code> processes</a></span></li></ul></li></ul></div>

## 1. Quick Start

To install `espressomaker`, run the following on your Terminal:
```bash
$ pip install espressomaker
```

To execute `espressomaker` as a context manager for a block of code, run on a Python 3 or an iPython kernel:
```python
from espressomaker import Espresso

with Espresso.shot():
    function_1()
    function_2()
    ...
```

The indented code will be run using the context manager of `espressomaker`, `Espresso.shot()`. While this code is running, your Mac won't go to sleep.

## 2. Purpose

`espressomaker` is a Python 3 module that does not let your Mac sleep when you are running a block of code.

Many applications that run on Python may take hours to finish, like machine learning training algorithms. If a block of code is actively running on a Python 3 kernel and the system goes to sleep, the running processes of the kernel will be interrupted and all the progress related to that block of code will be lost. 

To avoid that, `espressomaker` provides a handful of functionalities, including a useful context manager to run blocks of code. The context manager will allow you to use `Espresso`, a module of `espressomaker`, to temporarily change the power management settings of your Mac while the indented block of code runs. Once the code is done running, the settings will return to its default state.

`espressomaker` is a package that intends to facilitate dealing with lengthy Python jobs such that the user can, in a single line of code, forget about dealing interrupted processes.

## 3. Installation

To install `espressomaker`, run on your terminal:
```bash
$ pip install espressomaker
```

**Important note**

Installation using `pip` should be uneventful. However, if when importing a `ModuleNotFoundError` occurs, it could be possible that your current kernel is **not** including the directory where `espressomaker` is installed at. Usually, the `pip` installation process will place the packages contents at:
* `/Users/<your_username>/.local/lib/pythonX.Y/site-packages/`; or,
* `/Users/<your_username>/anaconda3/lib/pythonX.Y/site-packages/`, if using Anaconda;

where X.Y is your current Python version (root environment). You can check if these directories are considered by Python's system's path by running:
```python
import sys
sys.path
```

If it is not included, or if you chose to install it in a specific directory, add its path by running:
```python
sys.path.append('<path>')
```

## 4. User-guide

### 4.1 Working principle

`espressomaker` is a Python 3 package whose `Espresso` module allows to run `caffeinate` subprocesses from the running Python 3 kernel (e.g. a Jupyter Notebook, a `.py` script). The main go as subprocess as a context manager for a block of code or as a manual method call (i.e. the user defines when to start running the assertion and when to finish it). When a function of `Espresso` is called, an assertion that prevents a MacOS X system from sleeping is 

### 4.2 Importing the module

To import the functionalities of `espressomaker` to Python, run:
```python
from espressomaker import Espresso
```

### 4.3 Using as a context manager (`Espresso.shot()`)

One of the main advantages of `espressomaker` is that its `Espresso` module allows to run a given piece of code using a context manager. The context manager enables the `caffeinate` functionality for the code inside it and then closes the process — kills the `caffeinate` subprocess.

To use this functionality, run:
```python
with Espresso.shot(display_on = True):
    function_1()
    function_2()
    ...
```

### 4.4 Manually opening and closing tabs (`Espresso.opentab()` and `Espresso.closetab()`)

Pending.

### 4.5 Viewing open tabs — `caffeinate` running processes (`Espresso.check()`)

Pending.

### 4.6 Killing all `caffeinate` processes (`Espresso.killall()`)

Pending.

start-formatting
end-formatting
Formatting passed and completed.
