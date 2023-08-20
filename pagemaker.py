import os
import json

def generate_html(json_file_name, output_directory):
    with open(json_file_name, 'r') as file:
        data = json.load(file)

    base_style = data['BASE_STYLE']
    concepts = data['CONCEPTS']

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{base_style}</title>
        <style>
            .concept-images {{
                display: flex;
                flex-wrap: wrap;
                align-items: flex-start;
                margin-bottom: 20px;
            }}
            .concept-title {{
                font-weight: bold;
                margin-bottom: 10px;
            }}
            .concept-images img {{
                max-width: 360px;
                margin-right: 10px;
            }}
        </style>
    </head>
    <body>
        <h1>{base_style}</h1>
    """

    for concept in concepts:
        concept_name = concept['CONCEPT']
        urls = concept['URLs']
        html_content += f'<div class="concept-section">\n'
        html_content += f'    <p class="concept-title">{concept_name}</p>\n'
        html_content += '    <div class="concept-images">\n'
        for url in urls:
            html_content += f'        <img src="{url}" alt="{concept_name}">\n'
        html_content += '    </div>\n'
        html_content += '</div>\n'

    html_content += """
    </body>
    </html>
    """

    html_file_name = os.path.basename(json_file_name).replace('.json', '.html')
    html_file_path = os.path.join(output_directory, html_file_name)
    with open(html_file_path, 'w') as file:
        file.write(html_content)

    print(f"HTML page generated: {html_file_path}")
    return html_file_name

# Directory containing the JSON files
directory_path = 'styles/'

# Output directory for the HTML files
output_directory = 'pages'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# List to store the names of the generated HTML files
generated_html_files = []

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.json'):
        json_file_path = os.path.join(directory_path, filename)
        html_file_name = generate_html(json_file_path, output_directory)
        generated_html_files.append(html_file_name)

# Generate index.html
index_content = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n<title>Index</title>\n</head>\n<body>\n<h1>Index</h1>\n"
for html_file in generated_html_files:
    index_content += f"<a href='{html_file}'>{html_file}</a><br>\n"
index_content += "</body>\n</html>"

index_file_path = os.path.join(output_directory, 'index.html')
with open(index_file_path, 'w') as file:
    file.write(index_content)

print("All HTML pages generated successfully. Index created at index.html.")