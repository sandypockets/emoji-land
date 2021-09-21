from generate_land import ask_for_number, generate_land
import os


os.makedirs("outputs", exist_ok=True)

for i in range(1, 11):
    output = generate_land(200, 200)

    filename = os.path.join("outputs", f"test-{i}.txt")

    with open(filename, "w") as f:
        f.write(output)
