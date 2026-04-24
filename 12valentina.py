import tkinter as tk
from tkinter import messagebox, ttk

class Usuario:
    def __init__(self):
        self._usuario = "programacion"
        self._password = "programacion"

    def validar(self, usuario_ingresado, password_ingresada):
        return (usuario_ingresado == self._usuario and 
                password_ingresada == self._password)

class BicicletaTaller:
    def __init__(self, serial, hora_ingreso, costo_por_hora):
        self._serial = str(serial)
        self._hora_ingreso = float(hora_ingreso)
        self._costo_por_hora = float(costo_por_hora)
        self._hora_salida = None

    def registrar_salida(self, hora_salida):
        hora_salida_float = float(hora_salida)
        if hora_salida_float > self._hora_ingreso:
            self._hora_salida = hora_salida_float
            return True
        return False

    def calcular_total(self):
        if self._hora_salida is not None:
            return (self._hora_salida - self._hora_ingreso) * self._costo_por_hora
        return 0.0

    def obtener_serial(self):
        return self._serial

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

class BikeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bike Workshop Management System")
        self.user_session = Usuario()
        self.bikes_list = []
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.show_login()

    def show_login(self):
        self.clear_screen()
        center_window(self.root, 350, 250)
        
        ttk.Label(self.root, text="SYSTEM ACCESS", font=('Arial', 16, 'bold')).pack(pady=20)
        login_frame = ttk.Frame(self.root, padding="10")
        login_frame.pack()
        
        ttk.Label(login_frame, text="Username:").grid(row=0, column=0, sticky="w", pady=5)
        self.ent_user = ttk.Entry(login_frame)
        self.ent_user.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(login_frame, text="Password:").grid(row=1, column=0, sticky="w", pady=5)
        self.ent_pass = ttk.Entry(login_frame, show="•")
        self.ent_pass.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(self.root, text="Login", command=self.process_login, width=15).pack(pady=20)

    def process_login(self):
        u = self.ent_user.get().strip()
        p = self.ent_pass.get()
        if self.user_session.validar(u, p):
            messagebox.showinfo("Success", "Access granted.")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid credentials.")
            self.ent_pass.delete(0, 'end')

    def show_main_menu(self):
        self.clear_screen()
        center_window(self.root, 550, 480)
        
        ttk.Label(self.root, text="BIKE WORKSHOP SYSTEM", font=('Arial', 16, 'bold')).pack(pady=15)

        reg_frame = ttk.LabelFrame(self.root, text="Register Entry", padding="15")
        reg_frame.pack(pady=10, fill="x", padx=25)

        ttk.Label(reg_frame, text="Serial:").grid(row=0, column=0, sticky="w")
        self.ent_serial = ttk.Entry(reg_frame, width=25)
        self.ent_serial.grid(row=0, column=1, padx=5, pady=3)

        ttk.Label(reg_frame, text="Entry Hour:").grid(row=1, column=0, sticky="w")
        self.ent_entry_h = ttk.Entry(reg_frame, width=25)
        self.ent_entry_h.grid(row=1, column=1, padx=5, pady=3)

        ttk.Label(reg_frame, text="Cost/Hour:").grid(row=2, column=0, sticky="w")
        self.ent_cost = ttk.Entry(reg_frame, width=25)
        self.ent_cost.grid(row=2, column=1, padx=5, pady=3)

        ttk.Button(reg_frame, text="Add Bike", command=self.add_bike).grid(row=3, columnspan=2, pady=10)

        calc_frame = ttk.LabelFrame(self.root, text="Process Exit", padding="15")
        calc_frame.pack(pady=15, fill="x", padx=25)

        ttk.Label(calc_frame, text="Select Bike:").pack()
        self.combo_bikes = ttk.Combobox(calc_frame, state="readonly", width=30)
        self.combo_bikes.pack(pady=5)

        ttk.Label(calc_frame, text="Exit Hour:").pack()
        self.ent_exit_h = ttk.Entry(calc_frame, width=15)
        self.ent_exit_h.pack(pady=5)

        ttk.Button(calc_frame, text="Calculate & Exit", command=self.process_exit).pack(pady=10)

    def add_bike(self):
        try:
            bike = BicicletaTaller(self.ent_serial.get(), self.ent_entry_h.get(), self.ent_cost.get())
            self.bikes_list.append(bike)
            self.update_combo()
            self.ent_serial.delete(0, 'end')
            self.ent_entry_h.delete(0, 'end')
            self.ent_cost.delete(0, 'end')
            messagebox.showinfo("Success", "Bike registered.")
        except:
            messagebox.showerror("Error", "Invalid data.")

    def process_exit(self):
        idx = self.combo_bikes.current()
        h_out = self.ent_exit_h.get()
        if idx != -1 and h_out:
            bike = self.bikes_list[idx]
            if bike.registrar_salida(h_out):
                total = bike.calcular_total()
                messagebox.showinfo("Receipt", f"Serial: {bike.obtener_serial()}\nTotal: ${total:.2f}")
                self.bikes_list.pop(idx)
                self.update_combo()
                self.ent_exit_h.delete(0, 'end')
            else:
                messagebox.showerror("Error", "Exit hour must be > entry hour.")

    def update_combo(self):
        self.combo_bikes['values'] = [b.obtener_serial() for b in self.bikes_list]
        self.combo_bikes.set('')

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BikeApp(root)
    root.mainloop()
