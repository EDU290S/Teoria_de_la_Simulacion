import simpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Datos para la animación
times = []
queue_lengths = []

# Función de simulación
def customer(env, name, counter, log):
    log.insert(tk.END, f'{name} llega al tiempo {env.now}\n')
    with counter.request() as request:
        yield request
        log.insert(tk.END, f'{name} empieza a ser atendido al tiempo {env.now}\n')
        yield env.timeout(3)
        log.insert(tk.END, f'{name} termina al tiempo {env.now}\n')

def setup(env, num_customers, arrival_interval, counter, log):
    for i in range(num_customers):
        env.process(customer(env, f'Cliente {i+1}', counter, log))
        yield env.timeout(arrival_interval)

def run_simulation():
    # Crear entorno de simulación
    env = simpy.Environment()
    counter = simpy.Resource(env, capacity=1)

    # Crear la ventana de tkinter
    root = tk.Tk()
    root.title("Simulación de Cola con SimPy")
    
    # Crear un widget de texto con desplazamiento
    log = scrolledtext.ScrolledText(root, width=50, height=20)
    log.pack()

    # Función para actualizar datos para la animación
    def update_data(env):
        while True:
            times.append(env.now)
            queue_lengths.append(len(counter.queue))
            yield env.timeout(0.1)

    # Iniciar proceso de actualización de datos
    env.process(update_data(env))
    
    # Ejecutar la simulación
    env.process(setup(env, 30, 2, counter, log))
    env.run(until=60)

    # Iniciar la interfaz gráfica
    root.mainloop()

    # Crear la animación
    fig, ax = plt.subplots()
    ax.set_xlim(0, 60)
    ax.set_ylim(0, max(queue_lengths) + 1)
    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        line.set_data(times[:frame], queue_lengths[:frame])
        return line,

    ani = FuncAnimation(fig, update, frames=len(times), init_func=init, blit=True, interval=100)
    plt.xlabel('Tiempo (minutos)')
    plt.ylabel('Longitud de la cola')
    plt.title('Simulación de Cola')
    plt.show()

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import scrolledtext
    run_simulation()
