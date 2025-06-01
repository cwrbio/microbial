"""Executor Framework

This module provides the `Executor` class for managing and executing
the tasks scheduled and managed by the `Scheduler` class.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime as dt
from datetime import timedelta as td
from threading import Thread
from typing import Optional
from uuid import uuid4, UUID

from concurrent.futures import ThreadPoolExecutor

# ─── interfaces ───────────────────────────────────────────────────────── ✦✦ ──

class Executor(ABC):
    """Base class for task execution."""

    def __init__(self):
        self._id = None
        self._thread: Thread = Thread()


    # : properties

    @property
    def id(self) -> UUID:
        return self._id

    @id.setter
    def id(self, value: UUID) -> None:
        if not isinstance(value, UUID):
            raise TypeError("`Executor.id` must be an instance of `UUID`.")
        else:
            self._id = value

    @id.deleter
    def id(self) -> None:
        raise UserWarning("""\
⚠︎ Warning:

It is not recommended to delete executors' IDs, as they are integral to
the `microbial` event-handling framework's scheduling and management
mechanisms. If you need to change the ID, set it to a new instance of
`UUID`, rather than deleting it.
""")

    @property
    def thread(self) -> Thread:
        return self._thread

    @thread.setter
    def thread(self, value: Thread) -> None:
        if not isinstance(value, Thread):
            raise TypeError(
                "`Executor.thread` must be an instance of `Thread`."
            )
        else:
            self._thread = value

    @thread.deleter
    def thread(self) -> None:
        self._thread = None


    # : methods
    
    def execute(self, func, *args, **kwargs) -> None:
        """Execute a function in a separate thread."""
        if not callable(func):
            raise TypeError("`func` must be callable.")
        
        self.thread = Thread(target=func, args=args, kwargs=kwargs)
        self.thread.start()

