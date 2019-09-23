
# espressomaker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`espressomaker` is a Python module that provides a context manager (and other functionalities) to modify the power management settings on a MacOS X system so that running processes (e.g. a machine learning training algorithm) can run uninterruptedly.

More specifically, `espressomaker` is a wrapper of `caffeinate`, a shell command in MacOS X distributions that allows users to create assertions that alter the system's sleep behavior. In this sense. `espressomaker` runs `caffeinate` subprocesses from the Python 3 or iPython kernel from which `espressomaker` is being executed and allows to control it through a simple and intuitive set of Python commands.

<h2>Table of Contents<span class="tocSkip"></span></h2>
<div class="toc"><ul class="toc-item"><li><span><a href="#1-Objective" data-toc-modified-id="1.-Objective-1">1. Objective</a></span></li><li><span><a href="#2-Introduction" data-toc-modified-id="2.-Introduction-2">2. Introduction</a></span></li><li><span><a href="#3-Installation" data-toc-modified-id="3.-Installation-3">3. Installation</a></span></li><li><span><a href="#4-User-guide" data-toc-modified-id="4.-User-guide-4">4. User-guide</a></span><ul class="toc-item"><li><span><a href="#41-Working-principle" data-toc-modified-id="4.1-Working-principle-4.1">4.1 Working principle</a></span></li><li><span><a href="#42-Importing-the-module" data-toc-modified-id="4.2-Importing-the-module-4.2">4.2 Importing the module</a></span></li><li><span><a href="#43-Using-as-a-context-manager-(Espresso.shot())" data-toc-modified-id="4.3-Using-as-a-context-manager-(Espresso.shot())-4.3">4.3 Using as a context manager (<code>Espresso.shot()</code>)</a></span></li><li><span><a href="#44-Manually-opening-and-closing-tabs" data-toc-modified-id="4.4-Manually-opening-and-closing-tabs-4.4">4.4 Manually opening and closing tabs</a></span></li><li><span><a href="#45-Viewing-open-tabs" data-toc-modified-id="4.5-Viewing-open-tabs-4.5">4.5 Viewing open tabs</a></span></li><li><span><a href="#46-Killing-all-caffeinate-processes" data-toc-modified-id="4.6-Killing-all-caffeinate-processes-4.6">4.6 Killing all <code>caffeinate</code> processes</a></span></li></ul></li></ul></div>

## 1. Objective

Do not let your Mac sleep when you are running a code block. 

## 2. Introduction

Many applications that run on Python may take hours to finish, like machine learning training algorithms. If a block of code is actively running on a Python 3 kernel and the system goes to sleep, the running processes of the kernel will be interrupted and all the progress related to that block of code will be lost. 

To avoid that, `espressomaker` provides a handful of functionalities, including a useful context manager to run blocks of code, like this:
```python
from espressomaker import Espresso

with Espresso.shot():
    function_1()
    function_2()
    ...
```

The context manager will allow you to use `Espresso`, a module of `espressomaker`, to temporarily change the power management settings of your Mac while the indented block of code runs. Once the code is done running, the settings will return to its default state.

`espressomaker` is a module that intends to facilitate dealing with long running Python jobs such that the user can, in a single line of code, forget about dealing interrupted processes.

## 3. Installation

To install `espressomaker`, run on your terminal:
```bash
$ pip install espressomaker
```

**Important note**

If when importing an `ModuleNotFoundError` shows up, it could be possible that your current kernel is **not** including the directory where `espressomaker` is installed at. Usually, the `pip` installation process will place the packages contents at `/Users/<your_username>/.local/lib/pythonX.Y/site-packages`, where X.Y is your current Python version. You can check if this directory is considered by Python's system path by running:
```python
import sys
sys.path
```

If it is not included, run:
```python
sys.path.append('/Users/<your_username>/.local/lib/pythonX.Y/site-packages')
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

### 4.4 Manually opening and closing tabs

Pending.

### 4.5 Viewing open tabs

Pending.

### 4.6 Killing all `caffeinate` processes

Pending.

start-formatting
end-formatting
Formatting passed and completed.
