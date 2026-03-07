"""
Apache License 2.0
Copyright (c) 2026 Synthesis Lab

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from typing import Optional, Any


class State:
    """
    State Machine'nin temel sınıfı.
    
    Tüm SynScript state blokları bu sınıftan türetilir.
    
    Attributes:
        parent (Optional[Any]): State'i içeren actor referansı
        is_active (bool): State şu anda çalışıyor mu?
    
    Methods:
        on_enter(): State'e girildiğinde çağrılır (ilkbaşlangıç)
        tick(delta): Her frame'de çağrılır (mantık)
        on_exit(): State'den çıkılmadan önce çağrılır (temizlik)
    """
    
    def __init__(self, parent: Optional[Any] = None):
        """State'i ilklendir."""
        self.parent = parent
        self.is_active = False
    
    def on_enter(self) -> None:
        """
        State'e girildiğinde çağrıldı.
        Alt sınıflar tarafından ezilir (override).
        """
        pass
    
    def tick(self, delta: float) -> None:
        """
        Her frame'de çağrılır.
        
        Args:
            delta (float): Son frame'den beri geçen zaman (saniye)
        """
        pass
    
    def on_exit(self) -> None:
        """
        State'den çıkılmadan önce çağrılır.
        Alt sınıflar tarafından ezilir (override).
        """
        pass
    
    def enter(self) -> None:
        """
        State'i etkinleştir ve on_enter() çağır.
        (İç kullanım için)
        """
        self.is_active = True
        self.on_enter()
    
    def update(self, delta: float) -> None:
        """
        State'i güncelle (tick çağrısı sarmalama).
        (İç kullanım için)
        """
        if self.is_active:
            self.tick(delta)
    
    def exit(self) -> None:
        """
        State'i devre dışı bırak ve on_exit() çağır.
        (İç kullanım için)
        """
        self.is_active = False
        self.on_exit()
