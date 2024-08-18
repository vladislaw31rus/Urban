import time
class User:
    """
    класс пользователя, содержащий логин и пароль
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    """
    класс видео, содержит название, длительность, возрастное ограничение, время начала просмотра
    """
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Video((title="{self.title}", duration={self.duration}, adult_mode={self.adult_mode}))'


class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None
        self.current_age = None

    def log_in(self, nickname, password):
        if nickname in self.users:
            if self.users[nickname]['password'] == hash(password):
                # print(f'Вход выполнен, {nickname}')
                self.current_user = nickname
                self.current_age = int(self.users[nickname]['age'])
            else:
                print("Неверный пароль")
        else:
            print("Пользователь не найден")

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует.')
        else:
            self.users[nickname] = {'nickname': nickname, 'password': hash(password), 'age': age}
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self,  *videos):
        added_videos = []
        for video in videos:
            if isinstance(video, Video):
                if any(existing_video.title == video.title for existing_video in self.videos):
                    print(f'Видео с названием  "{video.title}" уже существует.')
                else:
                    self.videos.append(video)
                    added_videos.append(video.title)
                    # print(f'Видео добавлено  "{video.title}"')
            else:
                print("Передан объект не класса Video")

    def list_videos(self):
        return [str(video) for video in self.videos]

    def get_videos(self, search_title):
        search_videos = [video.title for video in self.videos if search_title.lower() in video.title.lower()]
        return search_videos

    def watch_video(self, name_film):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            video = next((v for v in self.videos if v.title == name_film), None)
            if video is not None:
                if video.adult_mode:
                    # Предположим, что у нас есть способ проверить возраст пользователя
                    if self.current_age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу.")
                    else:
                        # print(f"Начало просмотра видео: {video.title}")
                        for second in range(video.duration):  # Переводим минуты в секунды
                            print(f"{second + 1}")
                            time.sleep(1)  # Пауза в 1 секунду
                        print("Конец видео")




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 20, adult_mode=True)
# Добавление видео
ur.add(v1, v2, v3)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# Дополнительное практическое задание по модулю: "Классы и объекты."
#
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.
#
# Задание "Свой YouTube":
# Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.
#
# Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.
#
# Всего будет 3 класса: UrTube, Video, User.
#
# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.
#
# Подробное ТЗ:
#
# Каждый объект класса User должен обладать следующими атрибутами и методами:
# Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
# Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#  Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
# Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
# Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
# Метод log_out для сброса текущего пользователя на None.
# Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
# Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
# Для метода watch_video так же учитывайте следующие особенности:
# Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
# После воспроизведения нужно выводить: "Конец видео"
#
# Код для проверки:
# ur = UrTube()
# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
# # Добавление видео
# ur.add(v1, v2)
#
# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
#
# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
#
# Примечания:
# Не забывайте для удобства использовать dunder(магические) методы: __str__, __repr__, __contains__, __eq__ и др. (повторить можно здесь)
# Чтобы не запутаться рекомендуется после реализации каждого метода проверять как он работает, тестировать разные вариации.