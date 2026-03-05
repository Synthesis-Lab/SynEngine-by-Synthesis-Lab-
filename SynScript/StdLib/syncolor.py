"""
SynScript Standard Library - Color Module
RGBA renk yönetimi ve işlemleri
"""

class SynColor:
    """SynScript renk sınıfı - RGBA formatı"""
    
    def __init__(self, r: float, g: float, b: float, a: float = 1.0):
        """
        Renk oluştur
        Args:
            r: Kırmızı (0.0 - 1.0)
            g: Yeşil (0.0 - 1.0)
            b: Mavi (0.0 - 1.0)
            a: Alfa (0.0 - 1.0), varsayılan 1.0 (tam opak)
        """
        self.r = self._clamp(r)
        self.g = self._clamp(g)
        self.b = self._clamp(b)
        self.a = self._clamp(a)
    
    @staticmethod
    def _clamp(value: float) -> float:
        """0.0 ile 1.0 arasında sınırla"""
        return max(0.0, min(1.0, value))
    
    def to_hex(self) -> str:
        """Hexadecimal formatına çevir (#RRGGBBAA)"""
        r_hex = format(int(self.r * 255), '02x')
        g_hex = format(int(self.g * 255), '02x')
        b_hex = format(int(self.b * 255), '02x')
        a_hex = format(int(self.a * 255), '02x')
        return f"#{r_hex}{g_hex}{b_hex}{a_hex}"
    
    @staticmethod
    def from_hex(hex_color: str) -> 'SynColor':
        """Hexadecimal'den renk oluştur"""
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 6:
            r, g, b, a = int(hex_color[0:2], 16) / 255, int(hex_color[2:4], 16) / 255, int(hex_color[4:6], 16) / 255, 1.0
        elif len(hex_color) == 8:
            r, g, b, a = int(hex_color[0:2], 16) / 255, int(hex_color[2:4], 16) / 255, int(hex_color[4:6], 16) / 255, int(hex_color[6:8], 16) / 255
        else:
            raise ValueError("Invalid hex color format")
        return SynColor(r, g, b, a)
    
    def blend(self, other: 'SynColor', alpha: float) -> 'SynColor':
        """İki renği karıştır"""
        alpha = SynColor._clamp(alpha)
        r = self.r * (1 - alpha) + other.r * alpha
        g = self.g * (1 - alpha) + other.g * alpha
        b = self.b * (1 - alpha) + other.b * alpha
        a = self.a * (1 - alpha) + other.a * alpha
        return SynColor(r, g, b, a)
    
    def __repr__(self) -> str:
        return f"SynColor(r={self.r:.2f}, g={self.g:.2f}, b={self.b:.2f}, a={self.a:.2f})"
    
    # Önceden tanımlanmış renkler
    @staticmethod
    def RED():
        return SynColor(1.0, 0.0, 0.0)
    
    @staticmethod
    def GREEN():
        return SynColor(0.0, 1.0, 0.0)
    
    @staticmethod
    def BLUE():
        return SynColor(0.0, 0.0, 1.0)
    
    @staticmethod
    def WHITE():
        return SynColor(1.0, 1.0, 1.0)
    
    @staticmethod
    def BLACK():
        return SynColor(0.0, 0.0, 0.0)
    
    @staticmethod
    def YELLOW():
        return SynColor(1.0, 1.0, 0.0)
    
    @staticmethod
    def CYAN():
        return SynColor(0.0, 1.0, 1.0)
    
    @staticmethod
    def MAGENTA():
        return SynColor(1.0, 0.0, 1.0)
