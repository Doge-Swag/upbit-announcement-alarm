from botBase import GeneralAssistant 

class NewsAssistant (GeneralAssistant):
    def __init__(self, channel, header_length, header_title):
        super().__init__(channel, header_length, header_title)

    def build_header(self):
        super().build_header()
    
    def post_message(self, title, link):
        full_message =  self.header
        full_message += title + "\n"
        full_message += "[링크] " + link + "\n"
        
        full_message += self.getTimeStamp()

        self.send_message(full_message)

    def send_message(self, text):
        super().send_message(text)

    def getTimeStamp(self):
        return super().getTimeStamp()

if __name__ == "__main__" :
    bot = NewsAssistant("뉴스", 30, '[업비트 거래소 뉴스]')
    bot.post_message("대박뉴스 안내입니다.", "www.naver.com")

