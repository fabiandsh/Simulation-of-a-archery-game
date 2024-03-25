import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from gameManager import GameManager

import tkinter as tk

class GUI:
    def __init__(self):
        self.num_simulations = 0  # Variable global para almacenar el número de simulaciones
        self.gameManager = None
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Monte Carlo Simulation")

        # Create and pack the top frame
        self.frameTop = tk.Frame(self.root, width=800, height=200, bg="#3f334d")
        self.frameTop.pack(side=tk.TOP, expand=True)

        # Labels and entry fields for the additional fields
        self.sim_label = tk.Label(self.frameTop, text="Enter number of simulations:")
        self.sim_label.grid(row=0, column=0, padx=5, pady=5)
        self.sim_entry = tk.Entry(self.frameTop)
        self.sim_entry.grid(row=0, column=1, padx=5, pady=5)

        self.men_label = tk.Label(self.frameTop, text="Number of men who won:")
        self.men_label.grid(row=1, column=0, padx=5, pady=5)
        self.men_count = tk.Label(self.frameTop, text="")  # Empty label for men count
        self.men_count.grid(row=1, column=1, padx=5, pady=5)

        self.women_label = tk.Label(self.frameTop, text="Number of women who won:")
        self.women_label.grid(row=2, column=0, padx=5, pady=5)
        self.women_count = tk.Label(self.frameTop, text="")  # Empty label for women count
        self.women_count.grid(row=2, column=1, padx=5, pady=5)

        # Additional buttons
        self.exp_button = tk.Button(self.frameTop, text="Show players with most experience", command=self.show_experience)
        self.exp_button.grid(row=3, column=0, padx=5, pady=5)
        self.luck_button = tk.Button(self.frameTop, text="Show players with most luck", command=self.show_luck)
        self.luck_button.grid(row=3, column=1, padx=5, pady=5)
        self.groups_button = tk.Button(self.frameTop, text="Show winning groups", command=self.show_groups)
        self.groups_button.grid(row=3, column=2, padx=5, pady=5)

        # Start Simulation Button
        self.simulation_button = tk.Button(self.frameTop, text="Start Simulation", command=self.start_simulation)
        self.simulation_button.grid(row=4, columnspan=3, padx=5, pady=5)



        # Run the window
        self.root.mainloop()

    # Define functions for the additional buttons
    def show_experience(self):
        if self.gameManager is not None:
            # Crear una nueva ventana emergente
            experience_window = tk.Toplevel(self.root)
            experience_window.title("Experience Log")

            # Crear un widget de texto para mostrar el registro de experiencia
            experience_text = tk.Text(experience_window, height=20, width=50)
            experience_text.pack()

            # Insertar los registros de experiencia en el widget de texto
            for record in self.gameManager.players_with_better_experience:
                experience_text.insert(tk.END, record + "\n")
        else:
            print("No hay registros de experiencia disponibles")

    def show_luck(self):
        if self.gameManager is not None:
            # Crear una nueva ventana emergente
            lucky_window = tk.Toplevel(self.root)
            lucky_window.title("Lucky Log")

            # Crear un widget de texto para mostrar el registro de experiencia
            lucky_text = tk.Text(lucky_window, height=20, width=50)
            lucky_text.pack()

            # Insertar los registros de experiencia en el widget de texto
            for record in self.gameManager.players_with_better_lucky:
                lucky_text.insert(tk.END, record + "\n")
        else:
            print("No hay registros de experiencia disponibles")

    def show_groups(self):
        if self.gameManager is not None:
            # Crear una nueva ventana emergente
            teams_window = tk.Toplevel(self.root)
            teams_window.title("Lucky Log")

            # Crear un widget de texto para mostrar el registro de experiencia
            lucky_text = tk.Text(teams_window, height=20, width=50)
            lucky_text.pack()

            # Insertar los registros de experiencia en el widget de texto
            for record in self.gameManager.teams_Winners:
                lucky_text.insert(tk.END, record + "\n")
        else:
            print("No hay registros de experiencia disponibles")

    def start_simulation(self):
        # Use num_simulations variable in your simulation logic
        self.num_simulations = int(self.sim_entry.get())
        print(f"Starting simulation with {self.num_simulations} simulations.")
        self.gameManager =GameManager(self.num_simulations)
        self.plot()
        self.men_count.config(text=f"{self.gameManager.count_men}")
        self.women_count.config(text=f"{self.gameManager.count_women}")


    def plot(self):
        if self.gameManager != None: 
            x = []
            for i in range(1, len(self.gameManager.players_scores[0])+1):
                x.append(f"J{i}")
            
            y = self.gameManager.players_scores[0]

            fig, ax = plt.subplots()
            ax.bar(x, y)  # Cambiar a ax.bar para un gráfico de barras
            ax.set_title('Gráfico de ejemplo')
            ax.set_xlabel('Eje X')
            ax.set_ylabel('Eje Y')

            # Clear previous plot if exists
            for widget in self.frameTop.winfo_children():
                if isinstance(widget, FigureCanvasTkAgg):
                    widget.get_tk_widget().destroy()

            canvas = FigureCanvasTkAgg(fig, master=self.frameTop)
            canvas.get_tk_widget().grid(row=5, columnspan=3, padx=5, pady=5)  # Use grid instead of pack
            canvas.draw()
        else:
            print("No se ha iniciado ninguna simulación")



if __name__ == "__main__":
    gui = GUI()
