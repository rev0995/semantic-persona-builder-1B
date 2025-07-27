import json
import os

def map_personas(text):
    text = text.lower()
    personas = []

    if any(keyword in text for keyword in ["introduction", "overview", "future", "strategy"]):
        personas.append("Executive")
    if any(keyword in text for keyword in ["ai", "analytics", "data", "report", "insight"]):
        personas.append("Data Analyst")
    if any(keyword in text for keyword in ["developer", "architecture", "implementation", "api"]):
        personas.append("Developer")
    if any(keyword in text for keyword in ["customer", "journey", "personalization", "marketing"]):
        personas.append("Marketer")
    if "design" in text or "creative" in text:
        personas.append("Creative Professional")
    if "tourism" in text or "travel" in text:
        personas.append("Tourism Industry Expert")

    return personas if personas else ["General Reader"]

def main():
    input_path = "output/sample.json"  # ✅ Local path
    output_path = "output/mapped_personas.json"

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    mappings = []
    for item in data.get("outline", []):
        personas = map_personas(item["text"])
        mappings.append({
            "text": item["text"],
            "page": item["page"],
            "personas": personas
        })

    result = {
        "title": data.get("title"),
        "mappings": mappings
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print("✅ mapped_personas.json generated successfully.")

if __name__ == "__main__":
    main()
