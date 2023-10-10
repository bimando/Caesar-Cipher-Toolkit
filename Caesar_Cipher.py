import argparse

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift * mode) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    return result

def encrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as file:
            plaintext = file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return

    encrypted_text = caesar_cipher(plaintext, shift, 1)

    try:
        with open(output_file, 'w') as file:
            file.write(encrypted_text)
        print(f"Encryption complete. Encrypted text saved to '{output_file}'.")
    except Exception as e:
        print(f"Error writing to output file: {e}")

def decrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as file:
            ciphertext = file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return

    decrypted_text = caesar_cipher(ciphertext, shift, -1)

    try:
        with open(output_file, 'w') as file:
            file.write(decrypted_text)
        print(f"Decryption complete. Decrypted text saved to '{output_file}'.")
    except Exception as e:
        print(f"Error writing to output file: {e}")

def caesar_decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_caesar(input_file, output_file):
    with open(input_file, 'r') as file:
        ciphertext = file.read()

    with open(output_file, 'w') as out_file:
        for key in range(26):
            decrypted_text = caesar_decrypt(ciphertext, key)
            out_file.write("\n" + "#" * 87 + "\n")
            out_file.write(f"\t\t\t\t\tSHIFT KEY {key}\n")
            out_file.write("#" * 87 + "\n")
            out_file.write(f"{decrypted_text}\n")
            
    print(f"Decryption results saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Encrypt, decrypt, or crack a text file using Caesar cipher.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("-o", "--output_file", default="output.txt", help="Path to the output file [default: output.txt]")
    parser.add_argument("-s", "--shift", type=int, default=3, help="Shift value for Caesar cipher [default: 3]")
    parser.add_argument("-c", "--crack", action="store_true", help="Attempt to crack the Caesar cipher")
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the input file")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the input file")
    args = parser.parse_args()

    if args.crack:
        brute_force_caesar(args.input_file, args.output_file)
    elif args.encrypt:
        encrypt_file(args.input_file, args.output_file, args.shift)
    elif args.decrypt:
        decrypt_file(args.input_file, args.output_file, args.shift)
    else:
        print("No mode selected. Use -c for cracking, -e for encryption, or -d for decryption.")

if __name__ == "__main__":
    main()
