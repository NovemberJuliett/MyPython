import os
import smtplib
site_name = 'https://dvmn.org/referrals/f5ZfmRAHLPobficTeGhR7BjpCcT6OumPj2dv6Rx7/'
friend_name = 'Стас'
sender_name = 'Юлия'
letter = '''\
From: AllThoseMomentsWillBeLost@yandex.ru
To: izmaylovajulia@yandex.ru
Subject: Давай учиться
Content-Type: text/plain; charset="UTF-8";
\n\n
Привет, {friend}! {sender} приглашает тебя на сайт {site}!
\n
{site} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 
\n
Как будет проходить ваше обучение на {site}? 
\n
→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 
\n
Регистрируйся → {site}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''.format(friend = friend_name, site = site_name, sender = sender_name)
letter = letter.encode("UTF-8")
my_secret = os.environ['MAIL_PASSWORD']
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login('AllThoseMomentsWillBeLost', my_secret)
server.sendmail("AllThoseMomentsWillBeLost@yandex.ru", "izmaylovajulia@yandex.ru", letter)
server.quit()



