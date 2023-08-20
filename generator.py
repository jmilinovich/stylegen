import constants
import os
import json
import replicate

# for best practice, create a file keys.py and add your API token there and uncomment the following 2 lines
# import keys
# api_token = keys.REPLICATE_API_TOKEN
##
##
# for the quick start, uncomment the following line and add your API token
# api_token = "YOUR_REPLICATE_API_TOKEN"
os.environ['REPLICATE_API_TOKEN'] = api_token

CONCEPTS = constants.CONCEPTS
STYLES = constants.STYLES
MODEL_URL = constants.MODEL_URL
NUM_OUTPUTS = constants.NUM_OUTPUTS

class ImageGenerator:
    def __init__(self, concepts, styles, model_url, num_outputs):
        self.concepts = concepts
        self.styles = styles
        self.model_url = model_url
        self.num_outputs = num_outputs

    def generate_image(self, concept, style):
        prompt = style.replace("[concept]", concept)
        images = replicate.run(
            self.model_url,
            input={"prompt": prompt, "num_outputs": self.num_outputs})
        return {
            "CONCEPT": concept,
            "URLs": images
        }

    def generate_images_for_style(self, style):
        results = {
            "BASE_STYLE": style,
            "CONCEPTS": []
        }
        for concept in self.concepts:
            print(f"Generating image for concept: {concept}")
            result = self.generate_image(concept, style)
            results["CONCEPTS"].append(result)
        return results

    def generate_and_save_all_images(self):
        output_dir = 'styles'
        os.makedirs(output_dir, exist_ok=True)
        for style_name, style in self.styles.items():
            print(f"Generating images for style: {style_name}")
            result_json = self.generate_images_for_style(style)
            filename = os.path.join(output_dir, f'{style_name}.json')
            with open(filename, 'w') as file:
                json.dump(result_json, file, indent=4)

image_generator = ImageGenerator(CONCEPTS, STYLES, MODEL_URL, NUM_OUTPUTS)
image_generator.generate_and_save_all_images()