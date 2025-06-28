__app_name__ = "ask"
__version__ = "0.0.1"

(
    SUCCESS,
    ERROR
) = range(2)

ERRORS = {
    "GROQ_API_KEY_INVALID": "GROQ_API_KEY environment variable is set, but is invalid. Please check your API key.",
    "GROQ_API_KEY_MISSING": "GROQ_API_KEY environment variable is missing. Please set it in your .env file.",
    "ERROR": "An unknown error occurred. Please check your input and try again."
}
