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

from typing import Any, Optional, Type, Union, get_type_hints
import inspect


class TypeInference:
    """
    SynScript optional typing sistemi.
    
    Statik analiz ve runtime tip kontrolü sağlar.
    
    Features:
        - Type hints (opsiyonel): var x: int = 5
        - Duck typing (opsiyonel): var x = 5
        - Type checking: check_type(value, expected_type)
        - Type conversion: convert_type(value, target_type)
    
    Example:
        ```synscript
        # Tip belirtmeden (duck typing)
        var x = 5
        var name = "Player"
        
        # Tip belirterek (static)
        var health: int = 100
        var position: Vector2 = Vector2(0, 0)
        ```
    """
    
    # Desteklenen tip dönüşümleri
    TYPE_CONVERSIONS = {
        (int, float): float,
        (float, int): int,
        (int, str): str,
        (str, int): int,
        (bool, int): int,
        (int, bool): bool,
    }
    
    @staticmethod
    def check_type(value: Any, expected_type: Type, strict: bool = False) -> bool:
        """
        Değerin istenen tip'te olup olmadığını kontrol et.
        
        Args:
            value (Any): Kontrol edilecek değer
            expected_type (Type): Beklenen tip
            strict (bool): Strict modu (duck typing yok, tam eşleşme gerek)
        
        Returns:
            bool: Tip uyuşüyor mu?
        
        Example:
            ```python
            check_type(5, int)  # True
            check_type("hello", str)  # True
            check_type(5, float)  # False (strict=True)
            ```
        """
        if expected_type is Any:
            return True
        
        # Union types (int | float, etc.)
        if hasattr(expected_type, '__origin__'):
            if expected_type.__origin__ is Union:
                return any(
                    TypeInference.check_type(value, t, strict)
                    for t in expected_type.__args__
                )
        
        if strict:
            return type(value) is expected_type
        else:
            return isinstance(value, expected_type)
    
    @staticmethod
    def convert_type(value: Any, target_type: Type) -> Any:
        """
        Değeri hedef tip'e dönüştür.
        
        Args:
            value (Any): Dönüştürülecek değer
            target_type (Type): Hedef tip
        
        Returns:
            Any: Dönüştürülen değer (başarısız olursa orijinal)
        
        Example:
            ```python
            convert_type(5, float)  # 5.0
            convert_type("123", int)  # 123
            convert_type(5.7, int)  # 5
            ```
        """
        if type(value) is target_type:
            return value
        
        if target_type is int:
            return int(value)
        elif target_type is float:
            return float(value)
        elif target_type is str:
            return str(value)
        elif target_type is bool:
            return bool(value)
        else:
            return value
    
    @staticmethod
    def infer_type(value: Any) -> Type:
        """
        Değerin tip'ini otomatik tespit et.
        
        Args:
            value (Any): Tip tespit edilecek değer
        
        Returns:
            Type: Tespit edilen tip
        
        Example:
            ```python
            infer_type(5)  # <class 'int'>
            infer_type("hello")  # <class 'str'>
            infer_type([1, 2, 3])  # <class 'list'>
            ```
        """
        return type(value)
    
    @staticmethod
    def validate_function_args(
        func: Any,
        args: tuple,
        kwargs: dict,
        strict: bool = False
    ) -> bool:
        """
        Fonksiyon argümanlarını type hints'e (ipuçlarına) göre kontrol et.
        
        Args:
            func (Any): Fonksiyon
            args (tuple): Pozisyonel argümanlar
            kwargs (dict): Anahtar argümanlar
            strict (bool): Strict modu
        
        Returns:
            bool: Argümanlar uyuşuyor mu?
        
        Example:
            ```python
            def add(a: int, b: int) -> int:
                return a + b
            
            validate_function_args(add, (5, 3), {})  # True
            validate_function_args(add, ("5", 3), {})  # False (strict=True)
            ```
        """
        try:
            hints = get_type_hints(func)
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            
            for param_name, param_value in bound.arguments.items():
                if param_name in hints:
                    expected = hints[param_name]
                    if not TypeInference.check_type(param_value, expected, strict):
                        return False
            
            return True
        except Exception:
            return False


# Kolaylaştırılmış fonksiyonlar
def is_int(value: Any) -> bool:
    """Değer int mi?"""
    return isinstance(value, int) and not isinstance(value, bool)


def is_float(value: Any) -> bool:
    """Değer float mu?"""
    return isinstance(value, float)


def is_string(value: Any) -> bool:
    """Değer string mi?"""
    return isinstance(value, str)


def is_bool(value: Any) -> bool:
    """Değer bool mu?"""
    return isinstance(value, bool)


def is_list(value: Any) -> bool:
    """Değer list mi?"""
    return isinstance(value, list)


def is_dict(value: Any) -> bool:
    """Değer dict mi?"""
    return isinstance(value, dict)


def is_none(value: Any) -> bool:
    """Değer None mu?"""
    return value is None


def type_name(value: Any) -> str:
    """Değerin tip adını string olarak döndür."""
    return type(value).__name__
