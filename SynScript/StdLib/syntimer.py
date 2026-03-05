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
SynScript Standard Library - Timer Module
Zaman yönetimi ve delta time işlemleri
"""

import time as _time

class SynTimer:
    """SynScript zamanlayıcı"""
    
    def __init__(self, duration: float, repeating: bool = False):
        """
        Zamanlayıcı oluştur
        Args:
            duration: Süre (saniye), 0.0 ile başla
            repeating: Zamanındır mı?
        """
        self.duration = duration
        self.repeating = repeating
        self.elapsed = 0.0
        self.is_finished = False
        self._start_time = None
    
    def start(self):
        """Zamanlayıcıyı başlat"""
        self._start_time = _time.time()
        self.elapsed = 0.0
        self.is_finished = False
    
    def stop(self):
        """Zamanlayıcıyı durdur"""
        self._start_time = None
    
    def tick(self, delta: float):
        """
        Zamanlayıcıyı güncelle
        Args:
            delta: Geçen zaman (saniye)
        """
        if self._start_time is None:
            return
        
        self.elapsed += delta
        
        if self.elapsed >= self.duration:
            self.is_finished = True
            if self.repeating:
                self.elapsed = 0.0
            else:
                self.stop()
    
    def get_progress(self) -> float:
        """İlerleme yüzdesi (0.0 - 1.0)"""
        if self.duration == 0.0:
            return 0.0
        return min(1.0, self.elapsed / self.duration)
    
    def reset(self):
        """Zamanlayıcıyı sıfırla"""
        self.elapsed = 0.0
        self.is_finished = False
    
    def __repr__(self) -> str:
        return f"SynTimer(duration={self.duration}, elapsed={self.elapsed:.2f}, finished={self.is_finished})"


class DeltaTimer:
    """FPS-bağımsız delta time hesaplama"""
    
    def __init__(self, target_fps: int = 60):
        """
        Delta timer oluştur
        Args:
            target_fps: Hedef FPS (başlangıç için)
        """
        self.target_fps = target_fps
        self.delta_time = 0.0
        self._last_time = _time.time()
    
    def tick(self) -> float:
        """
        Bir frame'i işle ve delta time'ı döndür
        Returns:
            delta_time (saniye)
        """
        current_time = _time.time()
        self.delta_time = current_time - self._last_time
        self._last_time = current_time
        
        # Maksimum delta time sınırı (physics hatasını önlemek için)
        max_delta = 1.0 / 10.0  # 0.1 saniye (10 FPS minimum)
        self.delta_time = min(self.delta_time, max_delta)
        
        return self.delta_time
    
    def get_fps(self) -> float:
        """Tahmini FPS"""
        if self.delta_time == 0.0:
            return 0.0
        return 1.0 / self.delta_time
