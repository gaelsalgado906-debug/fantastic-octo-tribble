import gifos
from datetime import datetime

# Configuración de la fuente
# Asegúrate de que el archivo se llame font.ttf y esté dentro de la carpeta /fonts
FONT_FILE = "./fonts/font.ttf" 

def main():
    # 1. Inicializar la terminal (Ancho, Alto, margen_x, margen_y, fuente, tamaño)
    # Ajustamos a 700x400 para que se vea bien en el perfil de GitHub
    t = gifos.Terminal(700, 400, 20, 20, FONT_FILE, 15)
    t.set_fps(15) # Velocidad de la animación
    
    # 2. Configurar el Prompt (gael@github:~$)
    # \x1b[1;32m es verde, \x1b[1;34m es azul, \x1b[0m vuelve al blanco
    t.set_prompt("\x1b[1;32mgael\x1b[0m@\x1b[1;34mgithub\x1b[0m:~\x1b[1;33m$\x1b[0m ")
    t.gen_prompt(1)
    
    # 3. Efecto de escritura inicial
    t.gen_typing_text("gael comenzo...", 1, contin=True)
    t.clone_frame(10) # Pausa de medio segundo
    
    # 4. Escribir comando de ejecución
    t.gen_prompt(3)
    t.gen_typing_text("python3 start_coding.py --user gael", 3, contin=True)
    t.clone_frame(5)
    
    # 5. Texto de estado
    t.gen_text("Iniciando secuencia de escritura y proceso...", 5)
    
    # 6. Animación de carga (Círculo y Barra de Progreso)
    # Usaremos los caracteres clásicos de terminal: -, \, |, /
    spinner = ['-', '\\', '|', '/']
    total_pasos = 20
    
    for i in range(total_pasos + 1):
        porcentaje = (i * 100) // total_pasos
        # Creamos la barra: █ para lo lleno, ░ para lo vacío
        num_bloques = i // 2
        barra = "█" * num_bloques + "░" * (10 - num_bloques)
        
        # Seleccionamos el carácter del círculo animado
        char_anim = spinner[i % 4]
        
        # Borramos la línea 7 y escribimos el nuevo estado
        t.delete_row(7)
        # \x1b[36m es color Cian
        t.gen_text(f"\x1b[36m{char_anim}\x1b[0m Escribiendo codigo: [{barra}] {porcentaje}%", 7)
        t.clone_frame(2) # Frames por cada paso de carga

    # 7. Finalización
    t.gen_text("\x1b[1;32m[SUCCESS]\x1b[0m Proceso de Gael finalizado correctamente.", 9)
    t.gen_prompt(11)
    
    # 8. Pausa larga al final (4 segundos) para que se pueda leer antes de reiniciar
    t.clone_frame(60)
    
    # 9. Generar el archivo output.gif
    t.gen_gif()

if __name__ == "__main__":
    main()
