from pathlib import Path
import os
# Load score
try:
    #print(os.getcwd())
    #score_file = os.getcwd()
    score_file = Path.cwd() / "score.txt"
    with open(score_file, "r") as file:
        score = int(file.read())
except FileNotFoundError:
    score = 0

print("Current score:", score)

# --- Game ---
# Example: player earns 10 points
score += 10

print("New score:", score)

# Save updated score
with open(score_file, "w") as file:
    file.write(str(score))
    

