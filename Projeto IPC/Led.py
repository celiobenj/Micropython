from LED_RGB import LED_RGB as led
from time import sleep_ms

# Herdando a classe LED_RGB para a classe Led
class Led(led):
    def cicle(self, 
              preset: int = 1,
              delay: int = 50, 
              loop: int = 1,
              hex_list: list[str] = []
              ) -> None:
        """Método do padrão de ciclo do LED
        
        * `preset: int`: Determina o preset do ciclo em questão. Presets disponíveis: {1}. Caso `preset` seja algum inteiro diferente dos disponíveis, especifique a `hex_list`.
        
        * `delay: int`: Tempo em milisegundos de pausa entre as iterações. Aplicada na função `sleep_ms()`.
        
        * `loop: int`: Quantidade de repetições que o ciclo fará.
        
        * `hex_list: list[str]`: Lista contendo a string do código hexadecimal (hex, base 16, por exemplo `'#FFFFFF'`) que armazena a cor que o LED assumirá em cada iteração.
        """
        
        if preset == 1:
            delay = 250
            loop = 2
            hex_list = [ 
                "#000000", # black (off)
                "#0000FF", # blue
                "#00FF00", # green
                "#00FFFF", # green + blue = cyan
                "#FF0000", # red
                "#FF00FF", # red + blue = purple
                "#FFFF00", # red + green = yellow
                "#FFFFFF", # red + green + blue = white (on)
            ]
            
        elif preset == 2:
            delay = 100
            loop = 4
            hex_list = [
                "#0000FF", # blue
                "#00FF00", # green
                "#00FFFF", # green + blue = cyan
                "#00FF00", # green
                "#0000FF", # blue
            ]
        
        elif preset == 3:
            delay = 250
            loop = 5
            hex_list = [ 
                "#0000FF", # blue
                "#FF0000", # red
            ]
            
        for _ in range(loop):
            for h in hex_list:
                h = list(h)

                r = int(h[1] + h[2], 16)*4
                g = int(h[3] + h[4], 16)*4
                b = int(h[5] + h[6], 16)*4
                
                led.rgb(self, r, g, b)
                sleep_ms(delay)
    
    def transition(self, 
                   delay: int, 
                   step: int = 64
                   ) -> None:
        """Método do padrão de transição do LED
        
        * `delay: int`: Tempo em milisegundos de pausa entre as iterações da transição. Aplicada na função `sleep_ms()`.
        
        * `step: int`: Passo entre cada iteração. Padrão = 256. Se alterada, muda a resolução da transição das cores do LED.
        """
        
        # Estado inicial de r, g e b (definido arbitrariamente)
        r, g, b = 1023, 0, 0

        led.rgb(self, r, g, b)

        # r = 1023, g aumenta de 0 para 1023, b = 0
        while g < 1023:
            g += step
            g = 1023 if g > 1023 else g

            led.rgb(self, r, g, b)        
            sleep_ms(delay)

            if g > 1023: break


        # r diminui de 1023 para 0, g = 1023, b = 0
        while r > 0:
            r -= step
            r = 0 if r < 0 else r

            led.rgb(self, r, g, b)
            sleep_ms(delay)

            if r < 0: break


        # g = 1023, b aumenta de 0 para 1023, r = 0
        while b < 1023:
            b += step
            b = 1023 if b > 1023 else b

            led.rgb(self, r, g, b)
            sleep_ms(delay)

            if b > 1023: break


        # g diminui de 1023 para 0, b = 1023, r = 0
        while g > 0:
            g -= step
            g = 0 if g < 0 else g

            led.rgb(self, r, g, b)
            sleep_ms(delay)

            if g < 0: break


        # r aumenta de 0 para 1023, g = 0, b = 1023
        while r < 1023:
            r += step
            r = 1023 if r > 1023 else r

            led.rgb(self, r, g, b)
            sleep_ms(delay)

            if r > 1023: break


        # b diminui de 1023 para 0, r = 1023, g = 0
        while b > 255:
            b -= step
            b = 255 if b < 255 else b

            led.rgb(self, r, g, b)
            sleep_ms(delay)
            
            if b < 255: break
