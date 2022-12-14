# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в массиве DEFINITOINS на 11 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='Вставьте свой токен', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'баг': 'баг\nНекорректная работа программы, вызванная ошибкой в программном коде или дизайне продукта',
    'ntp': 'ntp\nNTP=НТП=Новая вкладка в браузере',
    'ptr': 'ptr\nPull To Refresh, потянуть экран вниз для рефреша страницы',
    'startrek': 'startrek\nТрекер задач, который используется и разрабатывается в Яндексе',
    'бп': 'бп\nБольшая почта. Обычная почта  https://mail.yandex.ru',
    'днд': 'днд\nДраг-н-дроп. Метод перемещения файлов путем перетаскивания',
    'пдд': 'пдд\nПочта для доменов',
    'прод': 'про\nОфициальная версия приложения (НЕ тестовая), доступная для общего пользования. При тестировании прод. версий веб-сервисов хосты прописывать не нужно. Продакшн версии мобильных приложений можно найти в App Store и Google Play',
    'синк': 'синк\nСинхронизация',
    'тап': 'тап\nКлик пальцем по экрану/кнопке/строке и т.д',
    'crash': 'crash, краш\nОстановка приложения в результате какой-либо ошибки (падение приложения)',
    'phonish': 'phonish, фониши\nЭто аккаунты, живущие на мобильном, связанные только с номером телефона и использующие в качестве метода авторизации смс',
    'testflight': 'TestFlight\nTest Flight — это сервис, упрощающий тестирование приложений для iOS-устройств путем облегчения процесса сбора кодов тестовых устройств (UDID-ов), а также путем более легкого распространения подписанных для тестеров билдов',
    'алиас': 'алиас\nАдрес, с которого будет отправлено письмо',
    'балансер': 'балансер\nРаспределитель нагрузки между серверами - балансировщик нагрузки',
    'бургер': 'бургер\nМеню',
    'дропзона': 'дропзона\nОбласть ДНД, куда перетаскивается файл',
    'заглушка': 'заглушка\nСтраница, показываемая вместо некоторого контента. Например, в случае, если нет сети или доступ к запрашиваемому содержимому по каким-то причинам запрещен',
    'инбокс': 'инбокс, inbox\nПапка "Входящие" в почте',
    'карусель': 'карусель, аккаунт свитчер\nЭкран выбора одного из зарегистрированных в системе аккаунтов',
    'корень диска': 'корень диска\nРаздел "Все файлы" в Я.Диске',
    'кукуц': 'кукуц\nПри добавлении или удалении пользователя из переписки в чате рисуется серая полоса с +/- имя пользователя',
    'лонгтап': 'лонгтап, long tap\nДлительное нажатие',
    'мейлиши': 'мейлиши\nАккаунты, которые авторизуются в приложениях Яндекса, используя логин и пароль внешнего почтового сервиса (Google, Mail, Rambler, Microsoft (Outlook))',
    'морда': 'морда\nГлавная страница сайта',
    'омнибокс': 'омнибокс\nПоисковая строка',
    'паранджа': 'паранджа\nЗатемнение заднего фона',
    'плейсхолдер': 'плейсхолдер, placeholder\nИспользуются в качестве заглушки полях и в формах ввода',
    'поделяшка': 'поделяшка\nБлок/попап импорта в соцсети.',
    'пошарить': 'пошарить, поделиться\nОпубликовать публичную ссылку на файл или папку кнопкой шаринга',
    'редирект': 'редирект, redirect\nПеренаправление пользователя на другой адрес',
    'саджест': 'саджест, саггест\nВыпадающее меню с вариантами значения для выбора',
    'серп': 'серп, serp\nSERP - Search Engine Results Page, Морда яндекса, страница с результатами поиска',
    'слайдер': 'слайдер, slider\nПревью картинок и видеофайлов с кнопками',
    'смоук тест': 'смоук тест, дымовой тест, дымовое тестирование\nМинимальный набор тестов на явные ошибки. Smoke-тестирование предназначено для проверки самых простых и очевидных кейсов, без которой любой другой вид тестирования будет неоправданно излишним',
    'снэк бар': 'снэк бар, snack bar\nУзкая панель, появляющаяся на несколько секунд внизу экрана, с краткой информацией для пользователя',
    'социальщик': 'социальщик\nПользователь, зарегистрированный в Яндексе с помощью профиля из социальной сети. Это не полноценный пользователь, у него ограниченный набор прав и нету даже логина с паролем',
    'сплешскрин': 'сплешскрин, splash screen\nЭкран загрузки, заставка',
    'старт визард': 'старт визард, СВ\nЭкран, который отображается у запущенного приложения в первый раз после добавления аккаунта',
    'статус бар': 'статус бар, status bar\nМаленькая информативная панель в верхней части дисплея смартфона, где можно узнать время, заряд аккумулятора и т.д',
    'тестран': 'тестран, ран, run\nНабор кейсов, запущенный в оценку',
    'тестсьют': 'тестсьют, сьют, suite\nНабор тест кейсов, объединенных по каким-то критериям (относятся к одному тестируемому модулю, функциональности, приоритету или одному типу тестирования)',
    'тикет': 'тикет, задача\nОпределенная задача или багрепорт в сервисе Стартрек',
    'тред': 'тред\nЦепочка писем с одной темой',
    'троббер': 'троббер, спиннер\nИндикатор, что программа выполняет какое-то действие, выглядит как круговая стрелка',
    'фавиконка': 'фавиконка\nЗначок веб-сайта или веб-страницы, а также изображение лого или типа файла,рядом с именем вкладки',
    'фотосрез': 'фотосрез, ФС\nРаздел "Все фото" на мобильном диске',
    'футер': 'футер, подвал, footer\nНижняя часть веб-страницы с полезным содержанием (ссылками, формой обратной связи и т.д.)',
    'хедер': 'хедер, шапка, header\nВерхняя часть веб-страницы с полезным содержанием (ссылками, строкой поиска и т.д.)',
    'хострут': 'хострут\nНезалогиненная страница почты',
    'ябл': 'ябл\nСформированный адрес в поле Почты',
    'янг': 'янг, yang\nСервис по сбору оценок',
    'пальма': 'testpalm\nСистема управления тестовой документацией и тестированием',
    'мок': 'mock\nОбъекты, которые заменяют реальный объект в условиях теста. Объект-заглушка, реализующий заданный аспект моделируемого ПО',
    'репозиторий': 'репозиторий\nЭто хранилище кода и истории его изменений',
    'git': 'git\nЭто консольная утилита, для отслеживания и ведения истории изменения файлов, в проекте, система управления версиями',
    'черный ящик': 'черный ящик, Black box\nТестировщику не известно как устроена тестируемая система',
    'белый ящик': 'белый ящик, White box\nТестировщику известно все детали реализации тестируемой системы',
    'серый ящик': 'серый ящик, Grey box\nТестировщику известно только некоторые особенности устройства тестируемой системы',
    'спецификация': 'спецификация\nДетальное описание того, как должно работать ПО.',
    'приоритет багов': 'приоритет баговприоритет багов\nВажность той или иной ошибки в ПО: \nTrivial — косметическая малозаметная проблема.\nMinor — очевидная, незначительная проблема.\nMajor — значительная проблема.\nCritical — проблема, нарушающая работу c ключевыми функциями ПО.\nBlocker — проблема, нарушающая функционирование ПО',
    'баг репорт': 'баг репорт\nДокумент, описывающий ситуацию или последовательность действий приведшую к некорректной работе объекта тестирования, с указанием причин и ожидаемого результата',
    'валидация': 'валидация\nОпределение соответствия разрабатываемого ПО ожиданиям и потребностям пользователя, требованиям к системе',
    'верификация': 'верификация\nПроцесс оценки системы или её компонентов с целью определения удовлетворяют ли результаты текущего этапа разработки условиям, сформированным в начале этого этапа',
    'тестирование': 'тестирование\nПроцесс проверки соответствия заявленных к продукту требований и реально реализованной функциональности, осуществляемый путем наблюдения за его работой в искусственно созданных ситуациях и на ограниченном наборе тестов, выбранных определенным образом',
    'qa': 'qa\nСовокупность мероприятий, охватывающих все технологические этапы разработки, выпуска и эксплуатации программного обеспечения',
    'ошибка': 'ошибка\nДействие, которое порождает неправильный результат',
    'ux': 'ux\nОщущение, испытываемое пользователем во время использования цифрового продукта',
    'ui': 'ui\nЭто инструмент, позволяющий осуществлять взаимодействие «пользователь — приложение»',
    'тест-дизайн': 'тест-дизайн\nЭто этап процесса тестирования ПО, на котором проектируются и создаются тестовые случаи (тест кейсы)',
    'тест-план': 'тест-план\nЭто документ, описывающий весь объем работ по тестированию, а также оценки рисков с вариантами их разрешения',
    'чек-лист': 'чек-лист\nЭто документ, описывающий что должно быть протестировано',
    'тест-кейс': 'test case\nто артефакт, описывающий совокупность шагов, конкретных условий и параметров, необходимых для проверки реализации тестируемой функции или её части',
    'регресс': 'регресс\nПроверка на наличие багов, вызванных изменениями в приложении',
}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет, друг! Только начал работать младшим специалистом ручного тестирования в компании Яндекс? Я помогу тебе запомнить и повторить сложные аббревиатуры и термины 🤓\nПросто введи интересующий термин, например, морда!', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='🤯 Я пока не знаю такого определения',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Давай еще!',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
