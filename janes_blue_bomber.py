import base64
import os
import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Create log file
log_filename = datetime.datetime.now().strftime('logs/log_%Y%m%d_%H%M%S.txt')
def log(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_filename, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")

# Define custom colors
PURPLE = Fore.MAGENTA  # Light purple
GREEN = Fore.GREEN     # Matrix green
YELLOW = Fore.YELLOW

def show_banner():
    print(PURPLE + Style.BRIGHT + "\n=== Base64 Tool Menu ===")
    print(PURPLE + "Hellsing Academy Tech Division Production, produced by Mun & Hellsing!\n")

def encode_text():
    text = input(GREEN + "Enter text to encode: ")
    encoded = base64.b64encode(text.encode()).decode()
    print(GREEN + "Encoded text:\n" + encoded)
    log(f"Encoded text: '{text}' -> '{encoded}'")

def decode_text():
    b64_text = input(GREEN + "Enter Base64 text to decode: ").strip()
    b64_text = b64_text.replace('\n', '').replace('\r', '').replace(' ', '')
    missing_padding = len(b64_text) % 4
    if missing_padding:
        b64_text += '=' * (4 - missing_padding)

    try:
        decoded = base64.b64decode(b64_text).decode()
        print(GREEN + "Decoded text:\n" + decoded)
        log(f"Decoded text: '{b64_text}' -> '{decoded}'")
    except UnicodeDecodeError:
        decoded_bytes = base64.b64decode(b64_text)
        print(GREEN + "Decoded bytes (not UTF-8 text):\n", decoded_bytes)
        log(f"Decoded non-UTF8 bytes from: '{b64_text}'")
    except Exception:
        try:
            decoded = base64.urlsafe_b64decode(b64_text).decode()
            print(GREEN + "Decoded text (URL-safe):\n" + decoded)
            log(f"URL-safe decoded text: '{b64_text}' -> '{decoded}'")
        except UnicodeDecodeError:
            decoded_bytes = base64.urlsafe_b64decode(b64_text)
            print(GREEN + "Decoded bytes (URL-safe, not UTF-8 text):\n", decoded_bytes)
            log(f"URL-safe decoded non-UTF8 bytes from: '{b64_text}'")
        except Exception as e:
            print(Fore.RED + "Error decoding text:", e)
            log(f"Error decoding text '{b64_text}': {e}")

def encode_file():
    input_path = input(GREEN + "Enter input file path: ")
    output_path = input(GREEN + "Enter output file path: ")
    if os.path.exists(input_path):
        with open(input_path, 'rb') as f:
            encoded = base64.b64encode(f.read())
        with open(output_path, 'wb') as f:
            f.write(encoded)
        print(GREEN + f"File encoded and saved to {output_path}")
        log(f"Encoded file '{input_path}' -> '{output_path}'")
    else:
        print(Fore.RED + "Input file does not exist.")
        log(f"Failed to encode file: '{input_path}' does not exist")

def decode_file():
    input_path = input(GREEN + "Enter input Base64 file path: ")
    output_path = input(GREEN + "Enter output file path: ")
    if os.path.exists(input_path):
        try:
            with open(input_path, 'rb') as f:
                decoded = base64.b64decode(f.read())
            with open(output_path, 'wb') as f:
                f.write(decoded)
            print(GREEN + f"File decoded and saved to {output_path}")
            log(f"Decoded file '{input_path}' -> '{output_path}'")
        except Exception as e:
            print(Fore.RED + "Error decoding file:", e)
            log(f"Error decoding file '{input_path}': {e}")
    else:
        print(Fore.RED + "Input file does not exist.")
        log(f"Failed to decode file: '{input_path}' does not exist")

def menu():
    while True:
        show_banner()
        print(PURPLE + "1. Encode text")
        print("2. Decode text")
        print(PURPLE +"3. Encode file")
        print("4. Decode file")
        print("5. Exit")
        choice = input(PURPLE + "Choose an option (1-5): ")

        if choice == '1':
            encode_text()
        elif choice == '2':
            decode_text()
        elif choice == '3':
            encode_file()
        elif choice == '4':
            decode_file()
        elif choice == '5':
            print(PURPLE + "Goodbye, Chairman Hellsing!")
            log("Exited program")
            break
        else:
            print(Fore.RED + "Invalid choice, please select from 1 to 5.")
            log(f"Invalid choice: '{choice}'")

if __name__ == "__main__":
    menu()
