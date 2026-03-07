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

from typing import Dict, Optional, Any
from .synstate import State
from .synsignal import Signal


class Actor:
    """
    Actor Scope Isolation: Oyun nesnelerinin temel sınıfı.
    
    Her actor, kendi izole ad alanında (scope) yaşar.
    Diğer actor'lar ile iletişim Signal aracılığıyla gerçekleşir.
    
    Attributes:
        current_state (Optional[State]): Aktif state (None ise state yok)
        _states (Dict[str, State]): Tüm state'lerin haritası
        _signals (Dict[str, Signal]): Tüm signal'lerin haritası
    
    Example:
        ```synscript
        actor PlayerCharacter:
            var health = 100
            signal health_changed(old: int, new: int)
            
            state Healthy:
                fn tick(delta):
                    pass
        ```
    """
    
    def __init__(self, name: str = "Actor"):
        """
        Actor'u ilklendir.
        
        Args:
            name (str): Actor adı
        """
        self.name = name
        self.current_state: Optional[State] = None
        self._states: Dict[str, State] = {}
        self._signals: Dict[str, Signal] = {}
    
    def add_state(self, state_name: str, state: State) -> None:
        """
        State'i actor'a ekle.
        
        Args:
            state_name (str): State'in adı
            state (State): State örneği
        """
        state.parent = self
        self._states[state_name] = state
    
    def change_state(self, state_name: str) -> bool:
        """
        Aktif state'i değiştir.
        
        Args:
            state_name (str): Hedef state'in adı
        
        Returns:
            bool: State değiştirildi mi?
        """
        if state_name not in self._states:
            print(f"[SynScript] State '{state_name}' bulunamadı")
            return False
        
        # Eski state'ten çık
        if self.current_state is not None:
            self.current_state.exit()
        
        # Yeni state'e gir
        self.current_state = self._states[state_name]
        self.current_state.enter()
        return True
    
    def add_signal(self, signal_name: str, signal: Signal) -> None:
        """
        Signal'i actor'a ekle.
        
        Args:
            signal_name (str): Signal'in adı
            signal (Signal): Signal örneği
        """
        signal.name = signal_name
        self._signals[signal_name] = signal
    
    def emit_signal(self, signal_name: str, *args: Any, **kwargs: Any) -> None:
        """
        Signal'i tetikle.
        
        Args:
            signal_name (str): Tetiklenecek signal'in adı
            *args: Signal callback'lerine iletilecek argümanlar
        
        Example:
            ```python
            player.emit_signal("health_changed", 100, 75)
            ```
        """
        if signal_name not in self._signals:
            print(f"[SynScript] Signal '{signal_name}' bulunamadı")
            return
        
        self._signals[signal_name].emit(*args, **kwargs)
    
    def get_signal(self, signal_name: str) -> Optional[Signal]:
        """
        Signal'i ada göre al.
        
        Args:
            signal_name (str): Signal'in adı
        
        Returns:
            Optional[Signal]: Signal veya None
        """
        return self._signals.get(signal_name)
    
    def update(self, delta: float) -> None:
        """
        Actor'u güncelle (state'in tick'ini çağır).
        
        Args:
            delta (float): Son frame'den beri geçen zaman (saniye)
        """
        if self.current_state is not None:
            self.current_state.update(delta)
    
    def get_state(self, state_name: str) -> Optional[State]:
        """
        State'i ada göre al.
        
        Args:
            state_name (str): State'in adı
        
        Returns:
            Optional[State]: State veya None
        """
        return self._states.get(state_name)
    
    @property
    def state_count(self) -> int:
        """State sayısı."""
        return len(self._states)
    
    @property
    def signal_count(self) -> int:
        """Signal sayısı."""
        return len(self._signals)
    
    def __repr__(self) -> str:
        state_name = self.current_state.name if self.current_state else "None"
        return f"<Actor '{self.name}' (state: {state_name}, {self.state_count} states, {self.signal_count} signals)>"
