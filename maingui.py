# maingui.py
import customtkinter as ctk
import os
from PIL import Image, ImageOps
from tools.basic_calc_frame import BasicCalcFrame
from tools.sci_calc_frame import SciCalcFrame

#Colors
import config



class MathApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("failure-404's Mega Conculator")
        self.geometry("700x500")
        
        # 1. Load Icons
        self.backspace_icon = self.load_inverted_icon("backspace.png")
        
        # 2. Main Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(self.sidebar, text="Tools", font=("Arial", 20, "bold")).grid(row=0, column=0, padx=20, pady=20)
        
        ctk.CTkButton(self.sidebar, text="Basic Calculator", fg_color=config.DestructiveColor, hover_color=config.DestructiveHoverColor, command=self.show_basic_calc).grid(row=1, column=0, padx=20, pady=5)

        ctk.CTkButton(self.sidebar, text="Scientific Calculator", fg_color=config.DestructiveColor, hover_color=config.DestructiveHoverColor, command=self.show_sci_calc).grid(row=2, column=0, padx=20, pady=5)

        self.container = ctk.CTkFrame(self, corner_radius=10)
        self.container.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        self.current_tool = None

    def load_inverted_icon(self, filename):
        try:
            path = os.path.join(os.path.dirname(__file__), "maingui_assets", filename)
            img = Image.open(path).convert("RGBA")
            r, g, b, alpha = img.split()
            inverted = ImageOps.invert(Image.merge('RGB', (r, g, b)))
            final = Image.merge('RGBA', (*inverted.split(), alpha))
            return ctk.CTkImage(dark_image=final, size=(25, 25))
        except: return None

    def show_basic_calc(self):
        if self.current_tool: self.current_tool.destroy()
        self.current_tool = BasicCalcFrame(self.container, backspace_icon=self.backspace_icon, fg_color="transparent")
        self.current_tool.pack(fill="both", expand=True)

    def show_sci_calc(self):
        if self.current_tool: self.current_tool.destroy()
        self.current_tool = SciCalcFrame(self.container, backspace_icon=self.backspace_icon, fg_color="transparent")
        self.current_tool.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MathApp()
    app.mainloop()