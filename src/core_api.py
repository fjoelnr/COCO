from src.python.python_analyzer import analyze_python_code

def analyze_code(code, language):
    if language == "python":
        return analyze_python_code(code)
    else:
        raise ValueError("Unsupported programming language: {}".format(language))
