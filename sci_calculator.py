# sci_calculator.py
import math

def calculate_sci(expression):
    """Processes scientific math strings and returns results."""
    if not expression:
        return "0"
    
    # Pre-processing human symbols to Python math symbols
    clean_input = expression.replace('(-)', '-').replace('^', '**').replace('π', 'math.pi').replace('e', 'math.e')
    
    # Map of allowed functions
    safe_dict = {
        "sin": math.sin, "cos": math.cos, "tan": math.tan,
        "sqrt": math.sqrt, "log": math.log10, "ln": math.log,
        "pi": math.pi, "e": math.e, "abs": abs
    }

    try:
        # Evaluate within a restricted environment
        result = eval(clean_input, {"__builtins__": None}, safe_dict)
        
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        return f"{result:.8g}" # Up to 8 digits for scientific precision
        
    except (ZeroDivisionError, ValueError):
        return "Math Error"
    except Exception:
        return "Error"