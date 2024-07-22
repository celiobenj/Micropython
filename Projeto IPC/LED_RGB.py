from machine import Pin, PWM

class LED_RGB:
    def __init__(self, 
                 r_pin: int, 
                 g_pin: int, 
                 b_pin: int, 
                 freq: int = 60
                 ) -> None:
        """Configurações iniciais dos pinos do LED"""
        self.PWM_r = PWM(Pin(r_pin))
        self.PWM_g = PWM(Pin(g_pin))
        self.PWM_b = PWM(Pin(b_pin))
        
        self.PWM_r.freq(freq)
        self.PWM_g.freq(freq)
        self.PWM_b.freq(freq)
    
    
    def rgb(self, 
            r: int, 
            g: int, 
            b: int
            ) -> None:
        """Especifica o `duty` (PWM) de cada pino do led. Contorla a intensidade de cada cor do led: vermelho (`r: int`), verde (`g: int`) e azul (`b: int`), respectivamente.
        
        Todos os parâmetros variam de 0 a 1023 (taxa de resolução de 10 bits do PWM da ESP32).
        """
        print(f"r: {r}, g: {g}, b: {b}\n")
        self.red(r)
        self.green(g)
        self.blue(b)
        
        
    def red(self, 
            duty: int) -> None:
        """Especifica o `duty` (PWM) do led vermelho (`r: int`).
        
        O parâmetro varia de 0 a 1023 (taxa de resolução de 10 bits do PWM da ESP32)."""
        self.PWM_r.duty(duty)
    
    
    def green(self, 
              duty: int) -> None:
        """Especifica o `duty` (PWM) do led verde (`g: int`).
        
        O parâmetro varia de 0 a 1023 (taxa de resolução de 10 bits do PWM da ESP32)."""
        self.PWM_g.duty(duty)
    
    
    def blue(self,
             duty: int) -> None:
        """Especifica o `duty` (PWM) do led azul (`b: int`).
        
        O parâmetro varia de 0 a 1023 (taxa de resolução de 10 bits do PWM da ESP32)."""
        self.PWM_b.duty(duty)
        
        
    def off(self) -> None:
        """Desliga o led."""
        self.rgb(0, 0, 0)
