# tools/sci_calc_frame.py
import customtkinter as ctk
import os
import sys

# Path fix to see parent folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sci_calculator  # Updated to match your filename
import config

class SciCalcFrame(ctk.CTkFrame): # Updated to match your class name
    def __init__(self, master, backspace_icon=None, **kwargs):
        super().__init__(master, **kwargs)
        
        # 1. LCD DISPLAY
        display_container = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=10)
        display_container.pack(pady=(15, 0), padx=20, fill="x")

        self.entry = ctk.CTkEntry(
            display_container, width=400, height=55, font=("Arial", 28),
            justify="right", fg_color="transparent", border_width=0
        )
        self.entry.pack(side="top", fill="x", padx=10, pady=(10, 0))
        self.entry.bind("<KeyRelease>", lambda e: self.update_result_preview())

        self.result_label = ctk.CTkLabel(
            display_container, text="0", font=("Arial", 18),
            text_color="#888888", anchor="e"
        )
        self.result_label.pack(side="bottom", fill="x", padx=15, pady=(0, 5))

        # 2. BUTTON GRID (6-Column Layout)
        self.grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_frame.pack(pady=10, padx=10, fill="both", expand=True)
        for i in range(6): self.grid_frame.columnconfigure(i, weight=1)

        # Button groups
        sci_keys = [('sin', 'sin('), ('cos', 'cos('), ('tan', 'tan('), ('sqrt', 'sqrt('), ('log', 'log('), ('ln', 'ln(')]
        more_keys = [('π', 'π'), ('e', 'e'), ('^', '^'), ('abs', 'abs('), ('(', '('), (')', ')')]
        
        standard_keys = [
            '7', '8', '9', '/', 'DEL', 'CLEAR',
            '4', '5', '6', '*', '<', '>',
            '1', '2', '3', '-', '0', '.',
            '(-)', '+', '=', '=' # Last two for the double-wide '='
        ]

        # Place scientific rows
        for i, (txt, val) in enumerate(sci_keys):
            self.create_btn(txt, val, 0, i, config.OperatorColor, config.OperatorHoverColor)
        for i, (txt, val) in enumerate(more_keys):
            self.create_btn(txt, val, 1, i, config.OperatorColor, config.OperatorHoverColor)

        # Place standard grid
        for i, btn_text in enumerate(standard_keys):
            r, c = (i // 6) + 2, i % 6
            
            # Formatting logic
            if btn_text == '=':
                if c == 4: # Start of double wide
                    self.create_btn('=', '', r, 4, config.ComputingColor, config.ComputingHoverColor, col_span=2, cmd=self.run_final)
                continue # Skip col 5
            
            # Standard button types
            if btn_text.isdigit():
                bg, hov = config.DigitColor, config.DigitHoverColor
            elif btn_text in ['CLEAR', 'DEL']:
                bg, hov = config.DestructiveColor, config.DestructiveHoverColor
            elif btn_text in ['<', '>']:
                bg, hov = config.ComputingColor, config.ComputingHoverColor
            else:
                bg, hov = config.OperatorColor, config.OperatorHoverColor

            self.create_btn(btn_text, btn_text, r, c, bg, hov)

    def create_btn(self, text, val, r, c, bg, hov, col_span=1, cmd=None):
        if not cmd:
            cmd = lambda: self.handle_press(val)
        ctk.CTkButton(self.grid_frame, text=text, fg_color=bg, hover_color=hov, 
                      command=cmd).grid(row=r, column=c, padx=2, pady=2, sticky="nsew", columnspan=col_span)

    def handle_press(self, char):
        if char == 'CLEAR': self.entry.delete(0, 'end')
        elif char == 'DEL': self.entry.delete(self.entry.index('insert')-1, 'insert')
        elif char == '<': self.entry.icursor(self.entry.index('insert')-1)
        elif char == '>': self.entry.icursor(self.entry.index('insert')+1)
        else: self.entry.insert('insert', char)
        self.update_result_preview()

    def update_result_preview(self):
        res = sci_calculator.calculate_sci(self.entry.get())
        if "Error" not in res:
            self.result_label.configure(text=res, text_color="#888888")

    def run_final(self):
        res = sci_calculator.calculate_sci(self.entry.get())
        color = "red" if "Error" in res else "white"
        self.result_label.configure(text=res, text_color=color, font=("Arial", 22, "bold"))