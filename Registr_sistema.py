import time as tm



class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode = False, time_now = 0):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __len__(self):
        return self.duration


class UrTube:

    def __init__(self, users, videos):
        self.users = users
        self.videos = videos
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
                return(f"Пользователь {nickname} авторизован.")
        return ('Логин или пароль введен неверно.')

    def register(self, nickname, password, age):
        for user in self.users:
             if user.nickname == nickname:
                 print(f"Пользователь {nickname} уже существует")
                 break
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        print(f"Пользователь {nickname} зарегистрирован.")
        self.current_user = new_user

    def log_out(self):
        if self.current_user != None:
            print(f"Пользователь {self.current_user.nickname} выходит")
        self.current_user = None

    def add(self, array):
        for v in array:
            if not isinstance(v, Video):
                print('Несоответствие типа данных')
                break
            self.videos.append(v)

    def get_videos(self, request):
        result = []
        for video in self.videos:
            if request.lower() in video.title.lower():
                result.append(video.title)
        return (f"Видео  <{request}>: {result}")

    def watch_video(self, request):
        if self.current_user == None:
            return ("Войдите в аккаунт, чтобы смотреть видео")
        for video in self.videos:
            if request == video.title:
                if video.adult_mode == True:
                    print (f"Видео <{request}> содержит контент для взрослых")
                    if self.current_user.age < 18:
                        return ("Вам нет 18 лет, пожалуйста покиньте страницу")
                for i in range(video.duration):
                    print(f"Видео воспроизводиться на {i} cукнде")
                return (f"Воспроизведение остановлено на {video.duration}-й сек.")
        return (f"Видео <{request}> не найдено")

Nikita = User("Nikita", hash("qwerty"), 41)
Dominika = User("Dominika", hash("зфыыцщкв"), 28)
v1 = Video('Лучший язык программирования 2024 года', 10)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur = UrTube([Nikita], [v1, v2])
print(ur.log_in("Nikita", hash("qwerty")))
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print(ur.log_out())
print(ur.log_in("petrushka", hash("12345")))
new_ur = UrTube(ur.users, ur.videos)
new_ur.add([v2])
new_ur.register("petrushka", hash("12345"), 17)
print(new_ur.watch_video("Лучший язык программирования 2024 года"))
print(new_ur.watch_video("Лучший"))