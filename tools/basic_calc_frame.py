# tools/basic_calc_frame.py
import customtkinter as ctk
import basic_calculator  # Import our math logic
import config


class BasicCalcFrame(ctk.CTkFrame):
    def __init__(self, master, backspace_icon=None, **kwargs):
        super().__init__(master, **kwargs)
        
        # 1. THE LCD DISPLAY CONTAINER
        display_container = ctk.CTkFrame(self, fg_color=config.ComputingColor, corner_radius=10)
        display_container.pack(pady=(30,0), padx=20, fill="x")

        # 2. ENTRY (Top of LCD)
        self.entry = ctk.CTkEntry(
            display_container, 
            width=350, height=50, font=("Arial", 30), 
            justify="right", fg_color="transparent", border_width=0
        )
        self.entry.pack(side="top", fill="x", padx=10, pady=(10, 0))
        self.entry.bind("<KeyRelease>", lambda e: self.update_result_preview())

        # 3. RESULT LABEL (Bottom Right of LCD)
        self.result_label = ctk.CTkLabel(
            display_container, 
            text="0", font=("Arial", 20), 
            text_color="#888888", anchor="e"
        )
        self.result_label.pack(side="bottom", fill="x", padx=15, pady=(0, 5))

        # --- BUTTON GRID ---
        self.grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_frame.pack(pady=10, fill="both", expand=True)

        for i in range(5): self.grid_frame.columnconfigure(i, weight=1)
        for i in range(5): self.grid_frame.rowconfigure(i, weight=1)

        # Row 0 Buttons
        ctk.CTkButton(self.grid_frame, text='CLEAR', fg_color=config.DestructiveColor, hover_color=config.DestructiveHoverColor, command=lambda: self.on_button_click('CLEAR')).grid(row=0, column=0, padx=3, pady=3, sticky="nsew")
        ctk.CTkButton(self.grid_frame, text='', image=backspace_icon, fg_color=config.DestructiveColor, hover_color=config.DestructiveHoverColor, command=lambda: self.on_button_click('BCKSP')).grid(row=0, column=1, padx=3, pady=3, sticky="nsew")
        ctk.CTkButton(self.grid_frame, text='DEL', fg_color=config.DestructiveColor, hover_color=config.DestructiveHoverColor, command=lambda: self.on_button_click('DEL')).grid(row=0, column=2, padx=3, pady=3, sticky="nsew")
        ctk.CTkButton(self.grid_frame, text='<', fg_color=config.ComputingColor, hover_color=config.ComputingHoverColor, command=lambda: self.on_button_click('<')).grid(row=0, column=3, padx=3, pady=3, sticky="nsew")
        ctk.CTkButton(self.grid_frame, text='>', fg_color=config.ComputingColor, hover_color=config.ComputingHoverColor, command=lambda: self.on_button_click('>')).grid(row=0, column=4, padx=3, pady=3, sticky="nsew")

        # Number Pad
        mid_buttons = ['7', '8', '9', '(', ')', '4', '5', '6', '*', '/', '1', '2', '3', '-', '+']
        for i, button in enumerate(mid_buttons):
            r, c = (i // 5) + 1, i % 5
            color = config.DigitColor if button.isdigit() else config.OperatorColor
            hovercolor = config.DigitHoverColor if button.isdigit() else config.OperatorHoverColor
            ctk.CTkButton(self.grid_frame, text=button, fg_color=color, hover_color=hovercolor, command=lambda b=button: self.on_button_click(b)).grid(row=r, column=c, padx=3, pady=3, sticky="nsew")

        # Bottom Row
        ctk.CTkButton(self.grid_frame, text='.', fg_color=config.OperatorColor, hover_color=config.OperatorHoverColor, command=lambda: self.on_button_click('.')).grid(row=4, column=0, padx=3, pady=3, sticky="nsew")
        ctk.CTkButton(self.grid_frame, text='0', fg_color=config.DigitColor, hover_color=config.DigitHoverColor, command=lambda: self.on_button_click('0')).grid(row=4, column=1, padx=3, pady=3, sticky="nsew")
        ctk.CTkButton(self.grid_frame, text='(-)', fg_color=config.OperatorColor, hover_color=config.OperatorHoverColor, command=lambda: self.on_button_click('(-)')).grid(row=4, column=2, padx=3, pady=3, sticky="nsew")
        ctk.CTkButton(self.grid_frame, text='=', fg_color=config.ComputingColor, hover_color=config.ComputingHoverColor, command=lambda: self.run_final()).grid(row=4, column=3, columnspan=2, padx=3, pady=3, sticky="nsew")

    def on_button_click(self, char):
        if char == "CLEAR": self.entry.delete(0, 'end')
        elif char == "BCKSP": 
            pos = self.entry.index('insert')
            self.entry.delete(pos-1, pos)
        elif char == "DEL":
            pos = self.entry.index('insert')
            self.entry.delete(pos, pos+1)
        elif char == "<": self.entry.icursor(self.entry.index('insert')-1)
        elif char == ">": self.entry.icursor(self.entry.index('insert')+1)
        else: self.entry.insert('insert', char)
        self.update_result_preview()

    def update_result_preview(self):
        res = basic_calculator.calculate_expression(self.entry.get())
        if "Error" not in res:
            self.result_label.configure(text=res, text_color="#888888")

    def run_final(self):
        res = basic_calculator.calculate_expression(self.entry.get())
        color = "red" if "Error" in res else "white"
        self.result_label.configure(text=res, text_color=color, font=("Arial", 24, "bold"))