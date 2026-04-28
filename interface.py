import tkinter as tk
from tkinter import ttk, scrolledtext
import algorithms
import datetime

class CrawlerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TERMINAL: WEB_CRAWLER_V1.0")
        self.root.geometry("1000x750")
        
        # --- Hacker Color Palette ---
        self.bg_black = "#0a0a0a"       # Deep Black
        self.neon_green = "#00ff41"     # Classic Matrix Green
        self.dark_green = "#003b00"     # Dim Green for borders
        self.terminal_bg = "#050505"    # Slightly lighter black
        self.text_white = "#e0e0e0"     # Muted white for labels
        
        self.root.configure(bg=self.bg_black)

        # Custom Styling
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Override TTK Styles for Hacker Theme
        self.style.configure("TFrame", background=self.bg_black)
        self.style.configure("TLabel", background=self.bg_black, foreground=self.neon_green, font=("Courier", 10, "bold"))
        self.style.configure("Header.TLabel", font=("Courier", 20, "bold"), foreground=self.neon_green, background=self.bg_black)
        
        self.style.configure("TLabelframe", background=self.bg_black, foreground=self.neon_green, bordercolor=self.dark_green)
        self.style.configure("TLabelframe.Label", background=self.bg_black, foreground=self.neon_green, font=("Courier", 10, "bold"))

        # Button Style
        self.style.configure("TButton", font=("Courier", 10, "bold"), background=self.dark_green, foreground=self.neon_green)
        self.style.map("TButton", background=[('active', self.neon_green)], foreground=[('active', self.bg_black)])

        self.create_widgets()

    def create_widgets(self):
        # --- Header Section ---
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=20)
        ttk.Label(header_frame, text="> WEB_CRAWLER_SIMULATION_SYSTEM", style="Header.TLabel").pack()

        # --- Control Panel ---
        control_frame = ttk.LabelFrame(self.root, text=" [ SYSTEM_CONFIG ] ", padding=15)
        control_frame.pack(padx=25, fill="x")

        # Start Node Input
        ttk.Label(control_frame, text="ROOT_NODE:").grid(row=0, column=0, padx=5, sticky="w")
        self.start_url = tk.Entry(control_frame, width=15, bg=self.terminal_bg, fg=self.neon_green, insertbackground=self.neon_green, font=("Courier", 10))
        self.start_url.insert(0, "home")
        self.start_url.grid(row=0, column=1, padx=10)

        # Algorithm Selection
        ttk.Label(control_frame, text="PROTOCOL:").grid(row=0, column=2, padx=5, sticky="w")
        self.algo_choice = ttk.Combobox(control_frame, values=["BFS", "DFS", "DLS"], state="readonly", width=10)
        self.algo_choice.current(0)
        self.algo_choice.grid(row=0, column=3, padx=10)
        self.algo_choice.bind("<<ComboboxSelected>>", self.toggle_depth)

        # Depth Limit (DLS only)
        ttk.Label(control_frame, text="DEPTH_MAX:").grid(row=0, column=4, padx=5, sticky="w")
        self.depth_val = tk.IntVar(value=3)
        self.depth_limit = tk.Spinbox(control_frame, from_=1, to=10, width=5, textvariable=self.depth_val, 
                                      state="disabled", bg=self.terminal_bg, fg=self.neon_green, buttonbackground=self.dark_green)
        self.depth_limit.grid(row=0, column=5, padx=10)

        # Action Button
        self.btn_start = ttk.Button(control_frame, text="EXECUTE", command=self.start_crawl)
        self.btn_start.grid(row=0, column=6, padx=20)

        # --- Main Display Area ---
        main_container = ttk.Frame(self.root)
        main_container.pack(expand=True, fill="both", padx=25, pady=20)

        # Left Column: Terminal Log
        log_frame = ttk.LabelFrame(main_container, text=" [ LOG_STREAM ] ", padding=10)
        log_frame.pack(side="left", expand=True, fill="both", padx=(0, 10))
        
        self.log_area = scrolledtext.ScrolledText(log_frame, bg=self.terminal_bg, fg=self.neon_green, 
                                                 insertbackground=self.neon_green, font=("Courier", 11), padx=10, pady=10)
        self.log_area.pack(expand=True, fill="both")

        # Right Column: Data Structures Visualization
        side_frame = ttk.Frame(main_container)
        side_frame.pack(side="right", fill="y")

        # Frontier Listbox
        ttk.Label(side_frame, text="FRONTIER_BUFFER:", font=("Courier", 10, "bold")).pack(anchor="w")
        self.frontier_list = tk.Listbox(side_frame, height=10, width=30, bg=self.terminal_bg, fg=self.neon_green, 
                                       borderwidth=1, highlightcolor=self.neon_green, font=("Courier", 9))
        self.frontier_list.pack(pady=(0, 15))

        # Visited Listbox
        ttk.Label(side_frame, text="INDEXED_NODES:", font=("Courier", 10, "bold")).pack(anchor="w")
        self.visited_list = tk.Listbox(side_frame, height=10, width=30, bg=self.terminal_bg, fg=self.text_white, 
                                      borderwidth=1, highlightcolor=self.dark_green, font=("Courier", 9))
        self.visited_list.pack()

    def toggle_depth(self, event):
        if self.algo_choice.get() == "DLS":
            self.depth_limit.config(state="normal")
        else:
            self.depth_limit.config(state="disabled")

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        ip_sim = "192.168.1.101"
        self.log_area.insert(tk.END, f"[{timestamp}] {ip_sim} >> {message}\n")
        self.log_area.see(tk.END)

    def run_step(self, generator):
        try:
            frontier, visited, message = next(generator)
            
            self.frontier_list.delete(0, tk.END)
            for item in frontier:
                self.frontier_list.insert(tk.END, f">> {item}")
            
            self.visited_list.delete(0, tk.END)
            for item in visited:
                self.visited_list.insert(tk.END, f"* {item}")
            
            self.log(message)
            self.root.after(700, lambda: self.run_step(generator))
        except StopIteration:
            self.log("TASK_COMPLETE: ALL REACHABLE NODES INDEXED.")
            self.btn_start.config(state="normal")

    def start_crawl(self):
        self.log_area.delete('1.0', tk.END)
        self.frontier_list.delete(0, tk.END)
        self.visited_list.delete(0, tk.END)
        
        algo = self.algo_choice.get()
        start = self.start_url.get()
        
        self.log(f"BOOTING {algo}_PROTOCOL...")
        self.btn_start.config(state="disabled")

        if algo == "BFS":
            gen = algorithms.bfs(start)
        elif algo == "DFS":
            gen = algorithms.dfs(start)
        elif algo == "DLS":
            limit = self.depth_val.get()
            gen = algorithms.dls(start, limit)
        
        self.run_step(gen)

if __name__ == "__main__":
    root = tk.Tk()
    app = CrawlerGUI(root)
    root.mainloop()