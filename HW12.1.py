
import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
           while True:
                if html.find("<") == -1:
                    break
                start = 0
                end = 0
                for i in range(len(html)):
                    if html[i] == "<":
                        start = i
                    if html[i] == ">":
                        end = i
                        if i != len(html)-1:
                            if html[i+1] == "\n":
                                end += 1
                        break
                html = html[:start] + html[end+1:]
           with open(result_file, "w") as file:
               file.write(html)

delete_html_tags("draft.html")
