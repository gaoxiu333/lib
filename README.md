


```python
with open('example.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    # 读取每一页的文本
    text = ""
    print(reader.pages)
    for page in range(reader.pages):
        text += reader.getPage(page).extractText()
    html_content = f"<html><body><p>{text}</p></body></html>"

with open('output.html', 'w') as html_file:
    html_file.write(html_content)

```