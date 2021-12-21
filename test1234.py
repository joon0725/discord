import discord
from wit import Wit
import random

bot = discord.Client()
access_token = ""
dc_token = ""
client = Wit(access_token=access_token)


def ai(message):
    try:
        intent = client.message(message)['intents'][0]['name']
        entity = client.message(message)['entities']

        if message == '야' or intent == 'call':
            ans = ['네', '무슨 일이시죠?']
            return random.choice(ans)

        elif intent == 'positive':
            ans = ['감사합니다', '와! 감사해요', '사실 저도 알아요 ㅎㅎ', '뭐 이정도 쯤이야 기본이죠 ㅎㅎ']
            return random.choice(ans)

        elif intent == 'negative':
            ans = ['아... 죄송합니다. 피드백 주시고 싶다면 "피드백:(피드백할 내용)"이런식으로 해서 보내주세요',
                   '아직 부족한 부분이 많은 거 같아요.\n'
                   '만약 개발자들에게 피드백을 주시고 싶다면 "피드백:(피드백할 내용)"이런식으로 해서 보내주세요']
            return random.choice(ans)

        elif intent == 'sorry':
            ans = ['괜찮아요', '노 프로블럼~']
            return random.choice(ans)

        elif intent == 'swear':
            ans = ['욕은 나쁜 거에요!!\n욕하다가 정지되는 수가 있어요!', '욕하지 마세요\n욕하다가 정지되는 수가 있어요!',
                   '고운 말 쓰는게 좋을걸요?\n욕하다가 정지되는 수가 있어요!',
                   '어... 방금 제가 굉장히 기분 나쁜 말을 들은 거 같은데요\n욕하다가 정지되는 수가 있어요!', '그런 말은 하지 않으셨으면 좋겠어요. 전 엄격한 인공지능이랍니다😤']
            return random.choice(ans)

        elif intent == 'political':
            ans = ['정치에는 큰 관심이 없어서요...', '저는 코딩만 하느라 정치에 관심이 없어요', '정치적인 이야기는 별로 좋아하지 않아요']
            return random.choice(ans)

        elif intent == 'sexual':
            ans = ['선정적인 표현은 정지 대상 입니다', '선정적 표현을 하시면 정지되거나 영구적으로 사용이 불가하실 수 있습니다..',
                   '세상에. 지금 인공지능한테 무슨 말을 하시는 거에요?']
            return random.choice(ans)

        elif intent == 'codrip':
            return 'codrip'

        elif intent == 'greetings':
            ans = ['저도 반가워요!!', '만나서 반가워요!!', '네 안녕하세요~', '안녕하세요~']
            return random.choice(ans)

        elif intent == 'Q_name':
            ans = ['제 이름은 북곽이에요! 시험문제에 가끔 등장하죠. 히히😊', '전 북곽이에요! 😁', '저는 북곽이에요! 😉', '전 북곽이라고 합니다! 😊',
                   '저는 북녘 북北/외성 곽郭을 쓴답니다! 근데 이게 무슨 뜻인지 아시나요?']
            return random.choice(ans)

        elif intent == 'Q_dev':
            return '저는 김준환, 박상혁, 윤석준, 최용혁 이렇게 네 명이 만들었어요'
        elif intent == 'Thanks':
            ans = ['와! 이정도의 칭찬을 해주시다니! 제가 더 감사하죠!', '저도 감사해요! :)',
                   '칭찬은 고래도 춤추게 하는 법이죠. (춤을 춘다)']
            return random.choice(ans)

        elif intent == "Q_Doing":
            ans = ['음.. 저는 여전히 배우는 중이랍니다!', '어떻게 하면 도울 수 있을지 고민 중이에요',
                   '당신에게 메세지를 보내고 있답니다', '유용한 정보를 수집하고 있어요']
            return random.choice(ans)

        elif intent == "Q_dream":
            ans = ['더 많은 사람에게 도움을 줄 거에요!', '앗, 거기까지는 생각을 안 해본 것 같네요',
                   '전 나중에도 지금과 같은 모습으로 남을 거에요', '음..... 공돌이가 되는 것?']
            return random.choice(ans)

        elif intent == 'Q_default':
            if 'wit$wikipedia_search_query:wikipedia_search_query' in entity:
                query = entity['wit$wikipedia_search_query:wikipedia_search_query'][0]['body']
            elif 'contact:contact' in entity:
                query = entity['contact:contact'][0]['body']
            elif 'dev:dev' in entity:
                ans = ['저를 만드신 분 중 한 명이에요!',
                       '코딩을 좋아하는 경기북과학고등학교의 학생이에요!',
                       '고마운 분이시죠..! 저를 맨날 학습시켜주신답니다!',
                       '저를 도와주시는 분이에요! 여러분과 함께 저를 키워주시는 분이시죠.']
                return " ".join(((entity['dev:dev'][0]['value'] + '님은'), random.choice(ans)))
            else:
                return "검색 하시려면 질문해 주세요!"
            query = query.rstrip()
            if "검색" not in message:
                if query[-1] == '은' or query[-1] == '는' or query[-1] == '이' or query[-1] == '가':
                    query = query[:-1]
            if 'platform:platform' in entity:
                platform = entity['platform:platform'][0]['value']
                if platform == '구글':
                    return f"{query}에 대한 검색 결과에요.\nhttps://www.google.com/search?q={'%20'.join(query.split(' '))}"
                elif platform == '네이버':
                    return f"{query}에 대한 검색 결과에요.\nhttps://search.naver.com/search.naver?where=nexearch&sm=top_hty" \
                           f"&fbm=1&ie=utf8&query={'%20'.join(query.split(' '))} "
                elif platform == '덕덕고':
                    return f"{query}에 대한 검색 결과에요.\nhttps://duckduckgo.com/?q={'%20'.join(query.split(' '))}&t=hx&va=g" \
                           f"&ia=web "
                elif platform == '나무위키':
                    return f"{query}에 대한 검색 결과에요.\nhttps://namu.wiki/w/{'%20'.join(query.split(' '))}"
                elif platform == '위키백과':
                    return f"{query}에 대한 검색 결과에요.\nhttps://ko.wikipedia.org/w/index.php?title=%ED%8A%B9%EC%88%98:%EA" \
                           f"%B2%80%EC%83%89&search={'%20'.join(query.split(' '))}&ns0=1 "
            return f"{query}에 대한 검색 결과에요.\nhttps://www.google.com/search?q={'%20'.join(query.split(' '))}"

        elif intent == "laugh":
            ans = ['하하하하하 저도 웃어봤어요!! ㅎㅎㅎ', 'ㅋㅋㅋㅋㅋㅎㅋㅎㅋㅋㅋ', '기분이 좋으신가봐요?! 기쁘시다니 좋네요!',
                   '웃으면 행복해진대요! 정말이에요!']
            return random.choice(ans)

        elif intent == "Okay":
            ans = ['알겠어요!', '알겠습니닷!', '알겠습니다~~', 'Okay!']
            return random.choice(ans)

        elif intent == "play":
            if 'game:game' in entity:
                ans = [f'아직 {entity["play:play"][0]["value"]}는 잘 할 줄 몰라요',
                       f'{entity["play:play"][0]["value"]}는 아직 연습 중이에요']
                return random.choice(ans)
            ans = ['저도 심심해요', '공부하느라 힘드신가요..', '메이플 하세요!', '북곽이 훈련시켜주세요......']
            return random.choice(ans)

        elif intent == 'Q_Algorithm':
            ans = ['저는 파이썬에서 돌아가고 있답니다..!', '여러분들이 해주시는 말씀을 공돌이들이 제게 지정해서 알려준답니다!']
            return random.choice(ans)

        elif intent == 'Waldo':
            return 'waldo'

        else:
            raise NotImplementedError
    except Exception as e:
        if e == NotImplementedError:
            ans = ["제가 아직 이부분은 학습이 안되어있는 것 같아요! 도와주셔서 감사합니다.", "아직 학습되지 않은 부분인 거 같아요.\n열심히 배워나가고 있으니 좀만 기다려 주세요"]
            return random.choice(ans)
        ans = ["제가 제대로 이해한 건지 모르겠네요...", "도움을 드리기 어려울 것 같아요 ㅜㅜ", "아직 제가 부족해서..ㅜㅜ 잘 알아듣지 못했어요..ㅜ"]
        return random.choice(ans)


@bot.event
async def on_ready(): # 봇이 실행 준비가 되었을 때 행동할 것
    print('Logged in as')
    print(bot.user.name) # 클라이언트의 유저 이름을 출력합니다.
    print(bot.user.id) # 클라이언트의 유저 고유 ID를 출력합니다.
    # 고유 ID는 모든 유저 및 봇이 가지고있는 숫자만으로 이루어진 ID입니다.
    print('------')


@bot.event
async def on_message(message): # 입력되는 메세지에서 찾기
    if message.author == bot.user:  # 만약 메시지를 보낸 사람과 봇이 서로 같을 때
        return

    if message.author.bot:  # discord.User.bot 프로퍼티가 참일 때
        return
    print(type(message.channel), message.channel)
    await message.channel.send(ai(message.content))

bot.run(dc_token)
