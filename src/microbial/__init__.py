"""Microbial

Utilities for modeling various microbiological systems.
"""
# ─── import statements ────────────────────────────────────────────────── ✦✦ ─
from . import (
    bacteria, fungi, frameworks, genomics, phylogeny, simulator, viruses
)

from .phylogeny import Phylogeny

from .bacteria import Bacterium
from .fungi import Fungus
from .genomics import Genome, BacterialGenome, FungalGenome, ViralGenome
from .simulator import Simulator
from .viruses import Virus

from .frameworks import (
    environment, events, executor, queue, scheduler, simulation
)
from .frameworks.environment import Environment
from .frameworks.executor import Executor
from .frameworks.events import Event, Eventful, MutationEvent, ReplicationEvent
from .frameworks.queue import Queue
from .frameworks.scheduler import Scheduler
from .frameworks.simulation import Simulation

__all__ = [
    # ─── modules ─────────────────────────────────────────────────────────────
    "bacteria",
    "environment",
    "events",
    "executor",
    "frameworks",
    "fungi",
    "genomics",
    "phylogeny",
    "scheduler",
    "simulation",
    "simulator",
    "queue",
    "viruses",

    # ─── classes ─────────────────────────────────────────────────────────────
    "BacterialGenome",
    "Bacterium",
    "Environment",
    "Event",
    "Eventful",
    "Executor",
    "FungalGenome",
    "Fungus",
    "Genome",
    "MutationEvent",
    "Queue",
    "ReplicationEvent",
    "Scheduler",
    "Simulation",
    "Simulator",
    "Phylogeny",
    "ViralGenome",
    "Virus"
]
