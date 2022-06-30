import json
import os

beta_posts = []
strip_character = "-"
final_output = []
formatted_beta_posts = []

f = open("src/main/content/blog_tags.json", "r")
content = json.loads(f.read())
tags = content['blog_tags']

def remove_duplicates(beta_posts):
    for beta_post_name in beta_posts:
        date = strip_character.join(beta_post_name.split(strip_character)[:3])
        for idx, x in enumerate(date.split('-')):
            date = addLeadingZero(date,idx,str(x).zfill(2))
        beta_post_name_after_date_split = strip_character.join(beta_post_name.split(strip_character)[3:])
        date = "/".join(date.split(strip_character))
        beta_post_name = date +'/'+beta_post_name_after_date_split
        formatted_beta_posts.append(beta_post_name)
        final_output.append(beta_post_name_after_date_split)
    res = [idx for idx, item in enumerate(final_output) if item in final_output[:idx]]
    for i in sorted(res, reverse=True):
        del formatted_beta_posts[i]
    return formatted_beta_posts

def addLeadingZero(date,index,addZero):
    date = date.split('-')
    date[index] = addZero
    date = strip_character.join(date)
    return date

for tag in tags:
    tag_name = tag['name']
    posts = tag['posts']
    for post_name in posts:
        for file_name in os.listdir("src/main/content/_posts/"):            
            if os.path.isfile("src/main/content/_posts/" + file_name) and file_name.endswith(post_name + '.adoc'):
                f_post = open("src/main/content/_posts/" + file_name)
                data = f_post.readlines()
                if tag_name == "beta":
                    if file_name.endswith(post_name + '.adoc'):
                        beta_posts.append(file_name.replace(".adoc", ".html"))
                # Check if there is already a tags front-matter from a previous tag
                line_num = 0
                tags_line = -1
                for line in data:
                    if line.startswith('tags: '):
                        tags_line = line_num
                        break
                    line_num += 1
                if tags_line != -1:
                    data[tags_line] = data[tags_line].replace(']', '').rstrip('\n') # Remove end bracket and initial newline
                    data[tags_line] = data[tags_line] + ', "' + tag_name + '"]\n'
                else:
                    # Otherwise, add the tags after the first line of front-matter
                    data[2] = 'tags: ["' + tag_name + '"]\n' + data[2] 

                with open("src/main/content/_posts/" + file_name, 'w') as f_write:
                    f_write.writelines(data)
                    f_write.close()
    if tag_name == "beta":
        beta_posts.sort(reverse = True)
        after_format_beta_links = remove_duplicates(beta_posts)
        tag["beta_post_links"] = after_format_beta_links
with open("src/main/content/blog_tags.json", 'w') as json_out_file:
    json.dump(content, json_out_file)
f.close()
