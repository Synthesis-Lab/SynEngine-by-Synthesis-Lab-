# Copyright © 2026 Synthesis Lab
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
SynScript Standard Library
Oyun geliştirme için temel kütüphaneler
"""

from .synmath import SynMath
from .syncolor import SynColor
from .syntimer import SynTimer, DeltaTimer
from .synvector import Vector2, Vector3
from .synstate import State
from .synsignal import Signal
from .synactor import Actor
from .syntyping import TypeInference

__all__ = [
    'SynMath',
    'SynColor',
    'SynTimer',
    'DeltaTimer',
    'Vector2',
    'Vector3',
    'State',
    'Signal',
    'Actor',
    'TypeInference',
]
