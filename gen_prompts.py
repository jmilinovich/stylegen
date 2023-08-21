import constants
import json

STYLES = constants.STYLES
CONCEPTS = constants.CONCEPTS

# Create a list to hold the organized prompts
organized_prompts = []

for style_name, style_description in STYLES.items():
    # Create a list to hold the prompts for this style
    prompts_for_style = []
    for concept in CONCEPTS:
        prompt = style_description.replace("[concept]", concept)
        prompts_for_style.append(prompt)

    # Add the style and its prompts to the organized list
    organized_prompts.append({
        "STYLE": style_name,
        "PROMPTS": prompts_for_style
    })

# Save the organized prompts to a JSON file
with open("prompts.json", "w") as file:
    json.dump(organized_prompts, file, indent=4)

print('successfully wrote all prompts to prompts.json')