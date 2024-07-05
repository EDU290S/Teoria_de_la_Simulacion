import simpy
import tkinter as tk
from tkinter import scrolledtext

# Función de simulación
def customer(env, name, counter, log):
    log.insert(tk.END, f'{name} llega al tiempo {env.now}\n')
    with counter.request() as request:
        yield request
        log.insert(tk.END, f'{name} empieza a ser atendido al tiempo {env.now}\n')
        yield env.timeout(3)
        log.insert(tk.END, f'{name} termina al tiempo {env.now}\n')

def setup(env, num_customers, arrival_interval, log):
    counter = simpy.Resource(env, capacity=1)
    for i in range(num_customers):
        env.process(customer(env, f'Cliente {i+1}', counter, log))
        yield env.timeout(arrival_interval)

def run_simulation():
    # Crear entorno de simulación
    env = simpy.Environment()

    # Crear la ventana de tkinter
    root = tk.Tk()
    root.title("Simulación de Cola con SimPy")
    
    # Crear un widget de texto con desplazamiento
    log = scrolledtext.ScrolledText(root, width=50, height=20)
    log.pack()

    # Ejecutar la simulación
    env.process(setup(env, 30, 2, log))
    env.run(until=60)

    # Iniciar la interfaz gráfica
    root.mainloop()

if __name__ == "__main__":
    run_simulation()
