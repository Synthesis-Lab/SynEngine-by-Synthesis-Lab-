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
SynScript Standard Library - Math Module
Oyun geliştirme için optimized matematiksel işlevler
"""

import math as _math

class SynMath:
    """SynScript matematiği"""
    
    PI = _math.pi
    TAU = _math.tau
    E = _math.e
    
    @staticmethod
    def sin(angle: float) -> float:
        """Sinüs (radyan cinsinden)"""
        return _math.sin(angle)
    
    @staticmethod
    def cos(angle: float) -> float:
        """Kosinüs (radyan cinsinden)"""
        return _math.cos(angle)
    
    @staticmethod
    def tan(angle: float) -> float:
        """Tanjant (radyan cinsinden)"""
        return _math.tan(angle)
    
    @staticmethod
    def sqrt(x: float) -> float:
        """Karekök"""
        return _math.sqrt(x)
    
    @staticmethod
    def abs(x: float) -> float:
        """Mutlak değer"""
        return abs(x)
    
    @staticmethod
    def pow(base: float, exp: float) -> float:
        """Üs alma"""
        return base ** exp
    
    @staticmethod
    def clamp(value: float, min_val: float, max_val: float) -> float:
        """Değeri min ve max arasında sınırla"""
        return max(min_val, min(value, max_val))
    
    @staticmethod
    def lerp(a: float, b: float, t: float) -> float:
        """Doğrusal interpolasyon (0.0 ile 1.0 arasında)"""
        return a + (b - a) * t
    
    @staticmethod
    def distance(x1: float, y1: float, x2: float, y2: float) -> float:
        """İki nokta arasındaki mesafe"""
        return _math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    @staticmethod
    def angle_between(x1: float, y1: float, x2: float, y2: float) -> float:
        """İki nokta arasındaki açı (radyan)"""
        return _math.atan2(y2 - y1, x2 - x1)
    
    @staticmethod
    def degrees_to_radians(degrees: float) -> float:
        """Derece to radyan"""
        return degrees * (_math.pi / 180.0)
    
    @staticmethod
    def radians_to_degrees(radians: float) -> float:
        """Radyan to derece"""
        return radians * (180.0 / _math.pi)
