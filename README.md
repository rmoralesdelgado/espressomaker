
<p align="center">
    <a href="https://pypi.org/project/espressomaker/" alt="PyPI version">
        <img src="https://img.shields.io/pypi/v/espressomaker" /></a>
    <a href="https://github.com/rmoralesdelgado/espressomaker/issues" alt="GitHub: Open Issues">
        <img src="https://img.shields.io/github/issues/rmoralesdelgado/espressomaker" /></a>
    <a href="https://github.com/rmoralesdelgado/espressomaker/blob/master/LICENSE" alt="License: MIT">
        <img src="https://img.shields.io/badge/License-MIT-yellow.svg" /></a>
</p>

# espressomaker

`espressomaker` is a Python 3 module that provides a context manager — and other functionalities — to modify the power management settings on a MacOS X system so that lengthy tasks (e.g. a machine learning training algorithm) can run uninterruptedly — without your Mac going to sleep.

More specifically, `espressomaker` is a wrapper of `caffeinate`, a shell command in MacOS X distributions that allows users to alter the system's sleep behavior. In this sense, `espressomaker` runs `caffeinate` subprocesses from the Python 3 interpreter or the IPython kernel from where it was imported and allows to control your Mac's sleep settings through a simple and intuitive set of Python commands.

<h2>Table of Contents<span class="tocSkip"></span></h2>
<div class="toc"><ul class="toc-item"><li><span><a href="#1-Quick-Start" data-toc-modified-id="1.-Quick-Start-1">1. Quick Start</a></span></li><li><span><a href="#2-Purpose" data-toc-modified-id="2.-Purpose-2">2. Purpose</a></span></li><li><span><a href="#3-Installation" data-toc-modified-id="3.-Installation-3">3. Installation</a></span></li><li><span><a href="#4-User-guide" data-toc-modified-id="4.-User-guide-4">4. User guide</a></span><ul class="toc-item"><li><span><a href="#41-Working-principle" data-toc-modified-id="4.1-Working-principle-4.1">4.1 Working principle</a></span></li><li><span><a href="#42-Importing-the-module" data-toc-modified-id="4.2-Importing-the-module-4.2">4.2 Importing the module</a></span></li><li><span><a href="#43-Default-settings" data-toc-modified-id="4.3-Default-settings-4.3">4.3 Default settings</a></span></li><li><span><a href="#43-Using-the-context-manager-—-Espresso.shot()" data-toc-modified-id="4.3-Using-the-context-manager-—-Espresso.shot()-4.4">4.3 Using the context manager — <code>Espresso.shot()</code></a></span></li><li><span><a href="#44-Manually-opening-and-closing-tabs-—-Espresso.opentab()-and-Espresso.closetab()" data-toc-modified-id="4.4-Manually-opening-and-closing-tabs-—-Espresso.opentab()-and-Espresso.closetab()-4.5">4.4 Manually opening and closing tabs — <code>Espresso.opentab()</code> and <code>Espresso.closetab()</code></a></span></li><li><span><a href="#45-Checking-the-tabs-—-Espresso.check()" data-toc-modified-id="4.5-Checking-the-tabs-—-Espresso.check()-4.6">4.5 Checking the tabs — <code>Espresso.check()</code></a></span></li><li><span><a href="#46-Killing-all-caffeinate-processes-—-Espresso.killall()" data-toc-modified-id="4.6-Killing-all-caffeinate-processes-—-Espresso.killall()-4.7">4.6 Killing all <code>caffeinate</code> processes — <code>Espresso.killall()</code></a></span></li></ul></li></ul></div>

## 1. Quick Start

To install `espressomaker`, run the following on your Terminal:
```bash
$ pip install espressomaker
```

To use `espressomaker` as a context manager for a block of code, run on a Python 3 interpreter or an IPython kernel:
```python
from espressomaker import Espresso

with Espresso.shot():
    function_1()
    function_2()
    ...
```

The indented code will be run using the context manager of `espressomaker`, `Espresso.shot()`. While this code is running, your Mac won't go to sleep.

## 2. Purpose

`espressomaker` provides a Python 3 module that prevents your Mac from sleep when you are running lengthy tasks — blocks of code that take a long time to finish.

Many applications that run on Python may take hours to finish, like machine learning training algorithms. If a task is actively running on a Python 3 interpreter — e.g. a Python script — or an iPython kernel — e.g. a Jupyter notebook — and the system goes to sleep, the running processes will be interrupted and all the progress related to that block of code will be lost. 

To avoid that, `espressomaker` provides a handful of functionalities, including a useful context manager to run blocks of code. The context manager will allow you to use `Espresso`, a module of `espressomaker`, to temporarily change the power management settings of your Mac while the indented block of code is running. Once the task is done, the settings will return to its default state.

`espressomaker` is a package that intends to facilitate dealing with lengthy Python tasks such that the user can, in a single line of code, forget about dealing with interrupted processes.

## 3. Installation

To install `espressomaker`, run on your terminal:
```bash
$ pip install espressomaker
```

You can find the package's PyPI link [here](https://pypi.org/project/espressomaker/).

**Troubleshooting**

The installation process using `pip` should be uneventful. After the installation, the package should be located at:
* `/Users/<your_username>/.local/lib/pythonX.Y/site-packages/`, if you use `pip` as the default package manager; or,
* `/Users/<your_username>/anaconda3/lib/pythonX.Y/site-packages/`, if you use `conda` as a package manager;

where X.Y is your current Python version (root environment). You can check if these directories are considered by Python's system's path by running:
```python
import sys
sys.path
```

However, if when importing a `ModuleNotFoundError` occurs, it could be possible that your current kernel is **not** including the directory where `espressomaker` is installed at. Although this is unlikely, you can find the current location of the package by running on your Terminal:
```bash
$ find /Users/ -type d -name 'espressomaker' 2>/dev/null | grep ".*python.*"
```

The previous command will search for a folder called `espressomaker` in the `Users/` directory and only print the matches that belong to a `python` subdirectory. If the directory found is not on `sys.path`, you can manually add it in Python using:
```python
sys.path.append('<path>')
```

## 4. User guide

### 4.1 Working principle

The `Espresso` module from `espressomaker` allows you to run `caffeinate` subprocesses — child processes of your current Python interpreter or IPython kernel. `caffeinate` is a shell command available on MacOS distributions that allows to prevent a computer from sleeping by creating assertions.

The `Espresso` module offers two ways to run `caffeinate` subprocesses:
1. As a context manager for a task — a block of code —, using the `shot()` method, or;
1. As a manual method call, using the `opentab()` and `closetab()` methods (i.e. the user defines when to start running the subprocess and when to finish it).

In either way, your Mac will not sleep until the task is completed — when using the context manager mode — or until you manually *close the tab*.

### 4.2 Importing the module

To import the functionalities of `espressomaker` to Python, run:
```python
from espressomaker import Espresso
```

### 4.3 Default settings

The `Espresso` module has two class-level settings: `verbose` and `display_on`. The `verbose` parameter enables messages related to the status of the module when using the `shot()` context manager. The `display_on` parameter determines whether the display of your Mac will remain on (if `display_on = True`) or if it will turn off (`display_on = False`) as per the current settings of your Mac.

The default class-level settings are the following and can be retrieved using `config()`:
```python
>>> Espresso.config()
Espresso(verbose = True, display_on = False)
```

To change these class-level settings — to set new default settings —, just pass in the parameters you want to change into `Espresso.config()`:
```python
>>> Espresso.config(display_on = True)
Espresso(verbose = True, display_on = True)
```

**Safety note**

For safety reasons, `espressomaker` only works when your Mac is connected to AC — it will not work if you are using battery power. 

### 4.3 Using the context manager — `Espresso.shot()`

One of the main advantages of the `Espresso` module is that it allows to run a task — a block of code — using a context manager. The context manager enables the `caffeinate` functionality — instantiates the subprocess — for the code inside it and then closes the process — kills the subprocess.

To use it, run:
```python
>>> with Espresso.shot(display_on = True):
...     function_1()
...     function_2()
        ...
```

As shown above, you can always override the `display_on` default settings by passing in a new value for that argument, which will only work for that instance.

### 4.4 Manually opening and closing tabs — `Espresso.opentab()` and `Espresso.closetab()`

Also, `Espresso` provides a manual way to instantiate a "caffeinate" subprocess in the current interpreter or kernel. The `opentab()` and `closetab()` methods allow you to instantiate and kill the `caffeinate` subprocess, respectively. 
```python
>>> Espresso.opentab()
[espressomaker] Espresso tab opened on Mon, 23/Sep/2019 10:38:46 (display_on = False).

# Your work

>>> Espresso.closetab()
[espressomaker] Espresso tab closed.
```

The `Espresso` module will prevent you from opening more than one `caffeinate` subprocess for the same parent process — e.g. the Python interpreter, the IPython kernel. Moreover, you can always run `Espresso` in multiple interpreters or kernels and check which `caffeinate` subprocess belongs to your current interpreter or kernel by running `Espresso.check()`.

**Warning**

Opening more than one `caffeinate` subprocess from a single parent process might not let `closetab()` to close all the running subprocesses. When you kill the parent process — e.g. close the Jupyter notebook — all the child process are killed along. If for some reason you suspect a `caffeinate` process is still running, you can try to pinpoint it using `Espresso.check()` or kill all the `caffeinate` processes running `Espresso.killall()`.

### 4.5 Checking the tabs — `Espresso.check()`

`Espresso.check()` allows you to retrieve a list of all running `caffeinate` processes in your Mac. If you have one running in your current interpreter or kernel, it will be explicitly indicated:
```python
>>> Espresso.check()
[espressomaker] The following "caffeinate" processes were found:
USER               PID COMMAND
<your_username>  62900 caffeinate -is -w 5531 (This kernel)
```

### 4.6 Killing all `caffeinate` processes — `Espresso.killall()`

The `killall()` method will kill **all** `caffeinate` processes running in the system. Before running it, be sure that you don't have other `caffeinate` active processes that you might need.

Formatting passed and completed.
