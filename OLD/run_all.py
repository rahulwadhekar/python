import os

folder_path = os.path.dirname(os.path.abspath(__file__))

print("🚀 Running all Python files...\n")

for file in sorted(os.listdir(folder_path)):
    if file.startswith("question_") and file.endswith(".py"):
        print(f"\n▶ Running {file}")
        os.system(f"python {file}")

print("\n✅ All files executed successfully!")