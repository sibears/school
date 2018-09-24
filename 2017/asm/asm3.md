# Reverse Engineering

## О чём говорили
- Что такое обратная разработка (RE) и с чем её едят
- Почему реверс это как литература :)
- Как реверсить в IDA Pro
- (Внезапно!) Как запускать бинарики в консоли линукс

## Краткий конспект команд

Сочетания клавиш:
- `Ctrl+Alt+t` - открыть терминал
- `Ctrl+c` - прервать выполнение текущего приложения
- `Ctrl+Shift+c` - скопировать из консоли
- `Ctrl+Shift+v` - вставить в консоль

Базовые команды:
- `ls` -- (**L**i**S**t) -- Содержимое текущей директории
- `pwd` -- (**P**resent **W**orking **D**irectory) -- Путь до текущей директории
- `cd` -- (**C**hange **D**irectory) -- Перейти в директорию

Важные сокращения:
- `~` -- (Home directory) - домашняя папка
- `.` -- (Current directory) - текущая папка
- `..` -- (Previous directory) - предыдущая папка

Работа с бинарником:
``` bash
chmod +x ./crackme        # -- Добавить бит исполнения (разрешить исполнение) программы
file ./crackme            # -- Определить тип файла (там можно посмотреть разрядность приложения - х86 или х64)
./crackme                 # -- Запустить приложение
./crackme 'NICE FL!G'     # -- Запустить приложение с экранированным аргументом командной строки
```

## Полезные ссылки
- IDA Pro ([бесплатная версия](https://www.hex-rays.com/products/ida/support/download_freeware.shtml))
- [IDA Pro Book](http://staff.ustc.edu.cn/~sycheng/ssat/books/The.IDA.Pro.Book.2ed.pdf) (на английском)
- [Перевод книги](https://wasm.in/blogs/vvedenie-v-reversing-s-nulja-ispolzuja-ida-pro-spisok-lekcij.585/) по IDA, вдохновлённый IDA Pro Book
- [Лекции](https://vk.com/spbctf?w=wall-114366489_1157%2Fall) по реверсу сообщества [spbctf](https://vk.com/spbctf)
- [DSECи собрали кучу ссылок по RE](https://habrahabr.ru/company/dsec/blog/334832/). Не то, чтобы я думаю, что вам всё это понадобится, но почему бы и не форсануть

## Домашнее задание
### Обязательное

Ждёт вас на [http://training.sibears.ru](http://training.sibears.ru).
Нужно:
- Зарегистрировать команду с префиксом [SSS] (Sibears Security School)
- Решить задания binary1-4

### Повышенной сложности, но важное
- Задание [`b0mb`](http://training.sibears.ru/challenges#B0mB)

### Дополнительное
- [Two arguments](http://training.hackerdom.ru/tasks/open/87/)
- [Don't exit](http://training.hackerdom.ru/tasks/open/88/)
- [Validate password](http://training.hackerdom.ru/tasks/open/93/)
- [How about md5?](http://training.hackerdom.ru/tasks/open/94/)
