import os

# One word for the human I work for: a boss whose task requests arrive
# like a tornado — each one spinning off three more.
ENTRY = "Tasknado"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
