from blocks import markdown_to_html_node
import os
def extract_title(markdown):
    lines = markdown.split("\n\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No h1 tag")


def file_to_string(filename):
    with open(filename, 'r') as f:
        return f.read()
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generate page from {from_path} to {dest_path} using {template_path}")
    markdown = file_to_string(from_path)
    template = file_to_string(template_path)
    title = extract_title(markdown)
    html_string = markdown_to_html_node(markdown)
    template = template.replace("{{ Title }}", title)
    # print(html_string)
    template = template.replace("{{ Content }}", html_string.to_html())
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    dir = os.path.dirname(dest_path)
    with open(dest_path, "w") as html_page:
            html_page.write(template)

    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    list_of_contents = all_files(dir_path_content)
    for content in list_of_contents:
       list = content.split("/")
       index = list.index('content')
       final_path = os.path.join(dest_dir_path, "/".join(list[index+1:])).replace(".md", ".html")
       generate_page(content, template_path, final_path)
         


def all_files(path):
    files = []
    for file in os.listdir(path):
        new_path = os.path.join(path, file)
        if os.path.isfile(new_path):
              files.append(new_path)
        else:
             files.extend(all_files(new_path))
    return files 
                
   
# print(all_files("/home/deusvitae/workspace/github.com/SumDeusVitae/static_site_generator/content"))




# print(extract_title("/home/deusvitae/workspace/github.com/SumDeusVitae/static_site_generator/content/index.md"))