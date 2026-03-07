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

from typing import Callable, List, Any


class Signal:
    """
    Signal/Slot event sistemi (Observer pattern).
    
    Signal'ler olayları (event) temsil eder.
    Slot'lar (connect edilen fonksiyonlar) bu olaylara yanıt verir.
    
    Example:
        ```synscript
        signal health_changed(old_value: int, new_value: int)
        
        fn take_damage(amount: int):
            old_hp = health
            health -= amount
            emit_signal("health_changed", old_hp, health)
        ```
    
    Attributes:
        _slots (List[Callable]): Bağlı callback fonksiyonları
    """
    
    def __init__(self, name: str = ""):
        """
        Signal'i ilklendir.
        
        Args:
            name (str): Signal adı (hata ayıklama için)
        """
        self.name = name
        self._slots: List[Callable] = []
    
    def connect(self, callback: Callable) -> None:
        """
        Callback'i bu signal'e bağla.
        
        Args:
            callback (Callable): Tetiklendiğinde çağrılacak fonksiyon
        
        Example:
            ```python
            health_changed.connect(ui.update_health_bar)
            ```
        """
        if callback not in self._slots:
            self._slots.append(callback)
    
    def disconnect(self, callback: Callable) -> None:
        """
        Callback'i bu signal'den ayır.
        
        Args:
            callback (Callable): Ayıklanacak fonksiyon
        """
        if callback in self._slots:
            self._slots.remove(callback)
    
    def emit(self, *args: Any, **kwargs: Any) -> None:
        """
        Signal'i tetikle (tüm bağlı callback'leri çağır).
        
        Args:
            *args: Callback'lere iletilecek pozisyonel argümanlar
            **kwargs: Callback'lere iletilecek anahtar argümanlar
        
        Example:
            ```python
            health_changed.emit(100, 75)  # old_value=100, new_value=75
            ```
        """
        for callback in self._slots:
            try:
                callback(*args, **kwargs)
            except Exception as e:
                print(f"[SynScript] Signal '{self.name}' callback hatası: {e}")
    
    def clear(self) -> None:
        """Tüm bağlantıları temizle."""
        self._slots.clear()
    
    @property
    def connected_count(self) -> int:
        """Bağlı callback sayısı."""
        return len(self._slots)
    
    # Syntactic sugar: signal => callback
    def __rshift__(self, callback: Callable) -> 'Signal':
        """
        => operatörü için destek.
        signal => callback  ≡  signal.connect(callback)
        """
        self.connect(callback)
        return self
    
    def __eq__(self, other: Any) -> bool:
        """Signal'leri compare et (testing için)."""
        return isinstance(other, Signal) and self.name == other.name
    
    def __repr__(self) -> str:
        return f"<Signal '{self.name}' ({self.connected_count} bağlantı)>"
