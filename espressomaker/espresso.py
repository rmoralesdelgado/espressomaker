#!/usr/bin/env python3
# coding: utf-8

# The espressomaker Project

# Standard library imports:
from contextlib import contextmanager
import os
import platform
import re
from shlex import split
import subprocess
import time

# Third-party imports:
# None

# Local application imports:
# None


def _OS_check():

    if platform.system() == 'Darwin':
        return True
    else:
        return False


def _caffeinate_check():

    caffeinate_search = re.compile('.*/caffeinate.*')
    cmd_check = subprocess.run(['which', 'caffeinate'], stdout = subprocess.PIPE).stdout.decode()

    if caffeinate_search.match(cmd_check):
        return True
    else:
        return False


while True:
    try:
        if _OS_check() is False: raise RuntimeError
    except RuntimeError:
        raise RuntimeError('This module only runs on MacOS. Failed to load "espresso".') from None
    else:
        break


while True:
    try:
        if _caffeinate_check() is False: raise RuntimeError
    except RuntimeError:
        raise RuntimeError('"caffeinate" not found on this Mac. Failed to load "espresso".') from None
    else:
        break


class Espresso:

    # Setting default "verbose" mode:
    verbose = True


    # Creating a temporal pid variable
    _temp_pid = None


    # Method to initialize the instance:
    def __init__(self):
        self.pid = os.getpid()
        self.ppid = os.getppid()


    # Method to run "caffeinate":
    def _opentab(self, display_on, pid = None):
        self.display_on = display_on
        if pid == None:
            pid = self.pid
        else:
            pid = pid
        if display_on == True:
            _caffeinate_on_cmd = split('caffeinate -dis -w ' + str(pid))
            self._caffeinate = subprocess.Popen(_caffeinate_on_cmd)
        elif display_on == False:
            _caffeinate_on_cmd = split('caffeinate -is -w ' + str(pid))
            self._caffeinate = subprocess.Popen(_caffeinate_on_cmd)
        print(_caffeinate_on_cmd, 'ERASE ME LATER')
        return self._caffeinate.pid


    # Method to kill "caffeinate":
    def _closetab(self, pid = None):
        if pid == None:
            self._caffeinate.kill()
        else:
            _kill_pid_on_cmd = split('kill ' + str(pid))
            subprocess.Popen(_kill_pid_on_cmd)


    # Method to find "caffeinate" processes being run by this kernel:
    def _status(self):
        '''
        espressomaker.espresso()._status()

        This private method was created to detect if a "caffeinate" child process of this kernel
        exists. In this sense, it's main purpose is to:
            a) Detect any running "caffeinate" processes in the system;
            b) Find the "caffeinate" process pid and return it only if it is a child of current
               kernel pid.

        The main problematic behind this resides in the "opentab()" and "closetab()" class-methods.
        The first method creates a child process, "caffeinate", and assigns its pid to a temporal
        class variable, which can be resetted if the kernel or module is reloaded. If this happens,
        the "closetab()" method finds no "caffeinate" pid to kill, thus generating an AttributeError
        exception.

        To prevent this, the "_status()" method finds the pid of the child "caffeinate" process and:
        a) Avoids "opentab()" to start running a second child "caffeinate" process; and,
        b) Helps "closetab()" get the current child "caffeinate" process pid so that it can kill it.

        Returns:
            Tuple of length 2, where index 0 is the "Status" and index 1 is the child's pid (only
            for Status = 1)

            Status:
                * 0: No Espresso tabs ("caffeinate" processes) were found in this kernel nor in the system.
                * 1: A Espresso tab ("caffeinate" processes) dependent of this kernel was found.
                * 2: No Espresso tabs ("caffeinate" processes) were found in this kernel, but "caffeinate"
                     processes were found in the system.
        '''

        _p_list = subprocess.run(split('ps -A -o user,ppid,pid,command'), stdout = subprocess.PIPE).stdout.decode()
        _p_list = _p_list.split('\n')
        ps_search = re.compile('.*[^(]caffeinate.*')
        if not any([ps_search.match(i) for i in _p_list]):
            print('[espressomaker _status]')
            return (0, None) # Status 0: 'None in kernel nor in system.'
        else:
            for i in _p_list:
                if ps_search.match(i):
                    _single_p = i.split() # Where [1] is ppid (kernel pid) and [2] is pid (caffeinate pid)
                    if str(os.getpid()) == _single_p[1]:
                        print('[espressomaker _status]') # Status 1: 'Found one dependent of this kernel.'
                        return (1, _single_p[2])
                    else:
                        print('[espressomaker _status]')
                        return (2, None) # Status 2: 'None in kernel, yes in system.'


    # Method to open and kill "caffeinate" with a context manager:
    @contextmanager
    def _shot(self, display_on):
        try:
            self._opentab(display_on = display_on)
            if self.verbose == True:
                print('[espressomaker] display_on is', self.display_on, 'verbose is', self.verbose, 'pid is', self.pid, 'caff pid is', self._caffeinate.pid)
            yield

        finally:
            self._closetab()
            if self.verbose == True:
                print('[espressomaker] display_on is', self.display_on, 'verbose is', self.verbose, 'pid is', self.pid, 'caff pid is', self._caffeinate.pid)


    # Class-method to run "_opentab()" via "Espresso.opentab()":
    @classmethod
    def opentab(cls, display_on = True):
        '''

        PENDING!

        '''
        status = cls()._status()

        if status[0] == 1:
            print('[espressomaker] There is a current tab opened. To close, run "Espresso.closetab()".')
        elif (status[0] == 0) or (status[0] == 2):
            cls._temp_pid = cls()._opentab(display_on)
            print('[espressomaker] Espresso tab opened.')


    # Class-method to run "_closetab()" via "Espresso.closetab()":
    @classmethod
    def closetab(cls):
        '''

        PENDING!

        '''

        # If, for some reason, Espresso is reloaded, the temporal variable holding the "pid" started by
        # Espresso.opentab() will be lost. In that sense, the following try-except block tries to catch
        # a possible AttributeError (in case said variable was lost), and proceeds to look for the
        # parent "pid" (the kernel's one) and then kills the "caffeine" corresponding to that kernel.

        try:
            cls()._closetab(pid = cls._temp_pid)
            print('[espressomaker] Espresso tab closed.')

        except AttributeError:

            status = cls()._status()

            if status[0] == 0:
                print('[espressomaker] No "caffeinate" processes related to this kernel (nor system) were found.')
            elif status[0] == 1:
                cls()._closetab(pid = status[1])
                print('[espressomaker] Espresso tab closed.')
            elif status[0] == 2:
                print('[espressomaker] No "caffeinate" processes related to this kernel were found\nbut there are other "caffeinate" processes running on this machine.')
        except:
            print('Unexpected error. If you still have any "caffeinate" processes open, run "Espresso.killall()".')

        finally:
            cls._temp_pid = None


    # Class-method to run context manager "_shot()" via "Espresso.shot()":
    @classmethod
    def shot(cls, display_on = True):
        '''

        PENDING!

        '''
        return cls()._shot(display_on)


    @staticmethod
    def opentabs():
        '''

        PENDING!

        '''
        _p_list = subprocess.run(split('ps -A -o user,pid,command'), stdout = subprocess.PIPE).stdout.decode()
        _p_list = _p_list.split('\n')
        ps_search = re.compile('.*[^(]caffeinate.*')
        if not any([ps_search.match(i) for i in _p_list]):
            print('[espressomaker] No "caffeinate" processes found.')
        else:
            print('The following open tabs were found:')
            print(_p_list[0])
            for i in _p_list:
                if ps_search.match(i):
                    print(i)

    @staticmethod
    def killall():
        '''

        PENDING!

        '''
        _killall_caffeinate_on_cmd = split('killall caffeinate')
        subprocess.Popen(_killall_caffeinate_on_cmd)
