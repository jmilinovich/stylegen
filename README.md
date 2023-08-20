# StyleGen, A python library for generating cohesive Stable Diffusion Prompts

One of the key difficulties in creating cohesive styles using Stable Diffusion is ensuring that a style-oriented prompt can generalize across a wide range of concepts. 

StyleGen is a flexible python library for generating high quality prompts for stable diffusion xl. For a given set of style prompts and concepts, it combinatorially generates all permutations of styles x concepts and then produces a set of html pages to visualize these outputs. 

![](https://github.com/jmilinovich/public/blob/main/stylegen.gif)

## Overview

There are four main files in this repo:
-- **constants.py**, which defines the list of styles and concepts to iterate through
-- **generator.py**, which generates images for all combinations of styles and concepts then stores the results in a json file
-- **pagemaker.py**, which generates html pages for each of the json payloads created in generator.py
-- **runner.py**, which runs generator.py then pagemaker and opens the resulting html in the browser

## Getting Started

To get started with StyleGen:
1. Clone this repo to your local environment
2. Add your [Replicate API key](https://replicate.com/account/api-tokens) to the top of generator.py
3. Update constants.py with your desired styles and concepts
4. Execute runner.py and enjoy the results

## Defining your styles

When you define your styles in constants.py, use the `[concept]` placeholder in the body of the prompt to make it clear where to interpolate the list of styles. Pick a representative name for your style, as this will be the name of the output json and html files.

## Feedback

If you enjoy this repo, please add a ⭐️ to help others find it in the future. If you have any questions or feedback, please feel free to open any Issues or [Tweet me](https://twitter.com/jmilinovich). 