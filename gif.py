import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Configuración de estilo
plt.rcParams['figure.facecolor'] = 'black'

def update_progress(num, ax):
    ax.clear()
    ax.set_aspect('equal')
    
    # Datos: El sector que se llena y el resto (vacío)
    percentage = num
    remaining = 100 - num
    
    # Colores: Un degradado de azul neón a oscuro
    colors = ['#00d4ff', '#222222']
    
    # Crear el gráfico de sectores
    wedges, _ = ax.pie([percentage, remaining], 
                        colors=colors, 
                        startangle=90, 
                        counterclock=False,
                        wedgeprops={'width': 0.2, 'edgecolor': 'none'})

    # Texto central
    ax.text(0, 0, f"{percentage}%", ha='center', va='center', 
            color='white', fontsize=25, fontweight='bold', family='sans-serif')
    
    ax.set_title("Cargando Repositorio...", color='white', pad=20)

# Crear la figura
fig, ax = plt.subplots(figsize=(5, 5))

# Crear la animación (de 0 a 100)
ani = animation.FuncAnimation(fig, update_progress, frames=range(0, 101, 2), 
                              fargs=(ax,), interval=50)

# Guardar como GIF
print("Generando GIF...")
ani.save('progreso_circular.gif', writer='pillow', fps=20)
print("¡Listo! Archivo 'progreso_circular.gif' creado.")
