import PyPDF2
import pyttsx3

# pdf文件的路径
path = open('control.pdf', 'rb')

# 创建pdf阅读器对象
pdfReader = PyPDF2.PdfFileReader(path)

# 初始化语音对象
speak = pyttsx3.init()

# 设置中文声音【默认英语原声】
speak.setProperty('voice', 'com.apple.speech.synthesis.voice.mei-jia')

# 读取pdf的第9页到第101页
for i in range(8, 100):

    from_page = pdfReader.getPage(i)

    # 抽取出这一页的文字内容
    text = from_page.extractText()
    print("要读取的文章片段：")
    print(text)

    # 开始读取
    print("开始读取文章片段")
    speak.say(text)
    speak.runAndWait()

speak.stop()

