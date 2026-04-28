import tkinter as tk
from tkinter import ttk, scrolledtext
import algorithms

class CrawlerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Crawler Search Simulator")
        self.root.geometry("950x700")
        self.root.configure(bg="#f8f9fa")

        # Custom Styling
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Color Palette
        self.bg_color = "#f8f9fa"
        self.primary_blue = "#1a73e8"
        self.terminal_bg = "#1e1e1e"
        self.terminal_fg = "#d4d4d4"

        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), foreground=self.primary_blue, background=self.bg_color)
        self.style.configure("TLabel", background=self.bg_color, font=("Segoe UI", 10))
        self.style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=5)
        
        self.create_widgets()

    def create_widgets(self):
        # --- Header Section ---
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=20)
        ttk.Label(header_frame, text="Web Crawler Search Simulator", style="Header.TLabel").pack()

        # --- Control Panel ---
        control_frame = ttk.LabelFrame(self.root, text=" Configuration ", padding=15)
        control_frame.pack(padx=25, fill="x")

        # Start Node Input
        ttk.Label(control_frame, text="Start Node:").grid(row=0, column=0, padx=5, sticky="w")
        self.start_url = ttk.Entry(control_frame, width=15)
        self.start_url.insert(0, "home")
        self.start_url.grid(row=0, column=1, padx=10)

        # Algorithm Selection
        ttk.Label(control_frame, text="Algorithm:").grid(row=0, column=2, padx=5, sticky="w")
        self.algo_choice = ttk.Combobox(control_frame, values=["BFS", "DFS", "DLS"], state="readonly", width=10)
        self.algo_choice.current(0)
        self.algo_choice.grid(row=0, column=3, padx=10)
        self.algo_choice.bind("<<ComboboxSelected>>", self.toggle_depth)

        # Depth Limit (DLS only)
        ttk.Label(control_frame, text="Depth Limit:").grid(row=0, column=4, padx=5, sticky="w")
        self.depth_val = tk.IntVar(value=3)
        self.depth_limit = tk.Spinbox(control_frame, from_=1, to=10, width=5, textvariable=self.depth_val, state="disabled")
        self.depth_limit.grid(row=0, column=5, padx=10)

        # Action Button
        self.btn_start = ttk.Button(control_frame, text="RUN CRAWLER", command=self.start_crawl)
        self.btn_start.grid(row=0, column=6, padx=20)

        # --- Main Display Area ---
        main_container = ttk.Frame(self.root)
        main_container.pack(expand=True, fill="both", padx=25, pady=20)

        # Left Column: Terminal Log
        log_frame = ttk.LabelFrame(main_container, text=" Crawl Log (Real-time Progress) ", padding=10)
        log_frame.pack(side="left", expand=True, fill="both", padx=(0, 10))
        
        self.log_area = scrolledtext.ScrolledText(log_frame, bg=self.terminal_bg, fg=self.terminal_fg, 
                                                 insertbackground="white", font=("Consolas", 10), padx=10, pady=10)
        self.log_area.pack(expand=True, fill="both")

        # Right Column: Data Structures Visualization
        side_frame = ttk.Frame(main_container)
        side_frame.pack(side="right", fill="y")

        # Frontier Listbox
        ttk.Label(side_frame, text="Frontier (Open List):", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.frontier_list = tk.Listbox(side_frame, height=10, width=30, bg="white", borderwidth=0, highlightthickness=1)
        self.frontier_list.pack(pady=(0, 15))

        # Visited Listbox
        ttk.Label(side_frame, text="Visited (Closed List):", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.visited_list = tk.Listbox(side_frame, height=10, width=30, bg="#e8f0fe", borderwidth=0, highlightthickness=1)
        self.visited_list.pack()

    def toggle_depth(self, event):
        """Enables/Disables depth input based on algorithm choice."""
        if self.algo_choice.get() == "DLS":
            self.depth_limit.config(state="normal")
        else:
            self.depth_limit.config(state="disabled")

    def log(self, message):
        """Helper to print to the simulation console."""
        self.log_area.insert(tk.END, f"> {message}\n")
        self.log_area.see(tk.END)

    def run_step(self, generator):
        """Iterates the generator and schedules the next update."""
        try:
            frontier, visited, message = next(generator)
            
            # Update UI Lists
            self.frontier_list.delete(0, tk.END)
            for item in frontier:
                self.frontier_list.insert(tk.END, item)
            
            self.visited_list.delete(0, tk.END)
            for item in visited:
                self.visited_list.insert(tk.END, item)
            
            self.log(message)
            
            # Schedule next step in 700ms for readability
            self.root.after(700, lambda: self.run_step(generator))
        except StopIteration:
            self.log("Simulation Finished: Target found or all accessible nodes explored.")
            self.btn_start.config(state="normal")

    def start_crawl(self):
        """Prepares the UI and starts the generator loop."""
        # Clear UI components
        self.log_area.delete('1.0', tk.END)
        self.frontier_list.delete(0, tk.END)
        self.visited_list.delete(0, tk.END)
        
        algo = self.algo_choice.get()
        start = self.start_url.get()
        
        self.log(f"Initializing {algo} Simulation...")
        self.btn_start.config(state="disabled") # Prevent multiple clicks during run

        # Select the correct generator from algorithms.py
        if algo == "BFS":
            gen = algorithms.bfs(start)
        elif algo == "DFS":
            gen = algorithms.dfs(start)
        elif algo == "DLS":
            limit = self.depth_val.get()
            self.log(f"Depth limit set to: {limit}")
            gen = algorithms.dls(start, limit)
        
        # Start the recursive update loop
        self.run_step(gen)

if __name__ == "__main__":
    root = tk.Tk()
    app = CrawlerGUI(root)
    root.mainloop()