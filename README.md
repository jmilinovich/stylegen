# StyleGen, A python library for generating cohesive Stable Diffusion Prompts

One of the key difficulties in creating cohesive styles using Stable Diffusion is ensuring that a style-oriented prompt can generalize across a wide range of concepts. 

StyleGen is a flexible python library for generating high quality prompts for stable diffusion xl. For a given set of style prompts and concepts, it combinatorially generates all permutations of styles x concepts and then produces a set of html pages to visualize these outputs. 

![](https://github.com/jmilinovich/public/blob/main/stylegen.gif)

## Overview

There are 5 main files in this repo:
- **constants.py**, which defines the list of styles and concepts to iterate through
- **generator.py**, which generates images for all combinations of styles and concepts then stores the results in a json file
- **pagemaker.py**, which generates html pages for each of the json payloads created in generator.py
- **runner.py**, which runs generator.py then pagemaker and opens the resulting html in the browser
- **gen_prompts.pt**, which can be used to generate a json file of prompts if the user would prefer not to use Replicate

## Getting Started

To get started with StyleGen:
1. Clone this repo to your local environment
2. Add your [Replicate API key](https://replicate.com/account/api-tokens) to the top of generator.py
3. Update constants.py with your desired styles and concepts
4. Execute runner.py, which will also install all dependencies from `requirements.txt` (ie, replicate)
5. Enjoy the results and star this repo 😇

## Defining your concepts and styles

- `CONCEPTS` are the subject matter of your images. Concepts are entities such as "the golden gate bridge" or "an old man sitting on a subway bench".
- `STYLES` are visual treatments to represent a subject matter. Styles are things like "water color" or "cyberpunk".

When you define your styles in constants.py, use the `[concept]` placeholder in the body of the prompt to make it clear where to interpolate the list of styles. Pick a representative name for your style, as this will be the name of the output json and html files.

## Generating prompts for use beyond Replicate

If you would like to use another instance of Stable Diffusion XL instead of Replicate, you can still use stylegen to help you create your prompts. When running stylegen, simply pass the flag `--prompts_only` and stylegen will create a new file, `prompts.json`, which you can then use downstream for any image models.

Example: `python3 stylegen.py --prompts_only`

## Feedback

If you enjoy this repo, please add a ⭐️ to help others find it in the future. If you have any questions or feedback, please feel free to open any Issues or [Tweet me](https://twitter.com/jmilinovich). 
