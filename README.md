# Космический защитник (Space Defender)
2D аркадный космический шутер с видом сверху.
Защитите космическую базу (позади игрока, не поместилась в экран ;-) ) от вторжения космических пришельцев.

Если пришелец дойдет до конца экрана или врежется в игрока, игрок теряет жизнь, уровень начинается сначала.
Игра завершится, когда у игрока не останется жизней.
За пораженных пришельцев начисляются очки, лучший результат игра сохраняет и отображает вверху экрана HI_SCORE.
Текущее количество очков SCORE и количество жизней игрока LIVES также отображаются вверху экрана.
В центре экрана объявляется текущий уровень LEVEL.

#### Управление:

Стрелки "Влево" и "Вправо" для перемещения игрока, "Пробел" - выстрел.


## Установка и запуск

Программа написана на [Python v.3.10](https://www.python.org) с использованием библиотеки [pygame v.2.1.2](https://github.com/pygame/pygame).
1. Скачайте SpaceDefender на Ваше устройство любым удобным способом (например Code -> Download ZIP, распакуйте архив).
2. Установите [Python](https://www.python.org), если он у Вас еще не установлен.
3. Установите библиотеку Pygame. Для этого откройте терминал, перейдите в каталог с игрой (cd <путь к игре>/SpaceDefender),
выполните команду `pip3 install -r requirements.txt`. Если Вы пользователь Microsoft Windows, то вместо `pip3 install ...` следует использовать  `pip install ...`
4. Запустите игру командой `python3 main.py` (Для Microsoft Windows `python main.py`).


#### Настройка
Если игра покажется слишком сложной или простой, поэкспериментируйте с настройками в разделе "начальные настройки" файла settings.py.

#### Приятной игры!


