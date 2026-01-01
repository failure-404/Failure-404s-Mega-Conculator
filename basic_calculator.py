# basic_calculator.py

def calculate_expression(expression):
    """Handles the math logic and returns a string result."""
    if not expression:
        return "0"
    
    # Replace the visual (-) with a computer-readable -
    clean_input = expression.replace('(-)', '-')
    
    try:
        # Safety: restrict access to built-in functions
        result = eval(clean_input, {"__builtins__": None}, {})
        
        # Clean up float decimals (e.g., 5.0 -> 5)
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        return str(result)
        
    except ZeroDivisionError:
        return "Error: Div by 0"
    except Exception:
        return "Error"