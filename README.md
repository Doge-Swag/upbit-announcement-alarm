# upbit-announcement-alarm

upbit 개발자 Announcement를 1시간마다 확인하고 새 뉴스가 있으면 Slack alarm으로 알려주는 모듈입니다.

## 사용법
myToken.txt에 자신의 Slack Chennel의 token을 적으면 됩니다.

## 작동원리
1. python bs4를 통해 웹 스크랩을 진행
2. memory.txt에 저장된 뉴스 타이틀과 변화가 있는지를 확인
3. 만일 변화가 있다면 새 뉴스 타이틀을 memory.txt에 덮어쓰고,  
   Slack bot에 새 뉴스 타이틀과 해당하는 링크를 즉시 보냅니다.
4. 위 과정을 1시간 마다 반복합니다.

## 참고자료
Slack alarm은 다음의 repository를 참고하여 구성하였습니다.  
https://github.com/SongDaeSun/slack-bot-assistant

upbit 개발자 Announcement 웹사이트는 다음과 같습니다.  
https://docs.upbit.com/changelog
