# semantic-persona-builder-1B
# Round 1B - Map Personas Project

## 🔍 Problem Statement
The goal of this round is to develop a solution that maps user personas based on the given data. The application takes input data, processes it, and generates corresponding persona maps using predefined logic.

perl
Copy
Edit

## 🧠 How It Works

1. map_personas.py reads the input CSV file and processes it.
2. It uses logic defined in utils.py to determine the persona for each record.
3. The output is stored in JSON format in the output/ folder.

## 🛠 Setup Instructions

### 1. Clone the Repository
bash
git clone https://github.com/yourusername/round1b.git
cd round1b
### 2. Create Virtual Environment (Optional but Recommended)
bash
python -m venv vnv
source vnv/bin/activate  # On Windows: vnv\Scripts\activate
### 3. Install Dependencies
bash
pip install -r requirements.txt
## 4. Run the Program
bash
python map_personas.py --input data/input.csv --output output/output.json
# 🐳 Docker Usage
   ### Build Docker Image
     bash
        docker build -t round1b-app .
      ## Run Docker Container
     bash
        docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/output:/app/output round1b-app
##📝 Notes
 Input should be in the specified CSV format.
Output will be generated as a JSON file mapping personas.
