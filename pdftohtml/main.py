import PyPDF2

# 读取PDF文件

file = open('example.pdf', 'rb')

# 创建一个PDF文件阅读器对象
reader = PyPDF2.PdfReader(file)

# 打印PDF文件的页数
print(len(reader.pages))
pageNum = len(reader.pages)

# 打印PDF文件的标题
print(reader.metadata.title)

text = ''
# 循环获取PDF文件的每一页内容
for i in range(0, pageNum):
    text += reader.pages[i].extract_text()

# 将文本内容写入HTML
html_content = f"<html><body><p>{text}</p></body></html>"

with open('output.html', 'w') as html_file:
    html_file.write(html_content)
