from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  end_text = ""
  if direction == "decode":
    shift *= -1
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {direction}d result:\n {end_text}")

print(logo)

should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caesar(text=text, shift=shift, direction=direction)

  restart = input("Restart? Type 'Yes' or 'No'\n").lower()
  if restart == "no":
    should_end = True
    print("Goodbye")