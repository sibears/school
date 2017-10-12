# -*- coding: utf-8 -*-

import re
import socket

# Установите DEBUG в значение True, чтобы видеть все сообщения, получаемые
# при помощи функции `recv_until`.
DEBUG = False
# Значение VERBOSE_JURY равное True, чтобы видет ответы жюри.
JURY_VERBOSE = True
# Установите значения JURY_HOST и JURY_PORT, указывающими на адрес жюри.
JURY_HOST = '192.168.0.132'
JURY_PORT = 31337
# FLAG_RE - регулярное выражение, сопостовляющее строки, состоящие из 31
# больших латинских буков и цифр, заканчивающиеся на '='.
FLAG_RE = re.compile('[A-Z0-9]{31}=')


def recv_until(sock, until='\n', debug=DEBUG):
    """Получает данные с сокета @sock до тех пор, пока ответ не содержит @until

    @sock - объект модуля socket
    @until - строка, которая должна содержаться в ответе
    @debug - установленное в `True` выводит ответы сервера на консоль

    Возвращает все полученные данные в формате _строки_
    """
    ans = ''
    while until not in ans:
        ans += sock.recv(100).decode()
    if debug:
        print(ans)
    return ans

def send(sock, mess):
    """Отправляет строку на сокет @sock

    @sock - объект модуля socket
    @mess - строка для отправки

    К строке будет добавлен перенос строки, после чего она будет переведена в
    байты и отправлена в сокет.
    """
    mess = mess + "\n"
    sock.send(mess.encode())

def make_connect(host, port):
    """Минимальная обёртка для удобства создания сокета

    @host - адрес сервера для подключения
    @port - порт приложения для подключения

    Возвращаемое значение - объект модуля socket
    """
    s = socket.socket()
    s.connect((host, port))
    return s

def post_flags(flags, jury_host=JURY_HOST, jury_port=JURY_PORT, verbose=JURY_VERBOSE):
    """Сдаёт флаги жюри по адресу @jury_host:@jury_port, отправляя флаги по 1 в строке

    @flags - список флагов
    @jury_host, @jury_port - адрес и порт сервиса
    @verbose - установленное в `True` выводит ответы сервера на консоль
    """
    if not flags:
        return
    try:
        jury_sock = make_connect(jury_host, jury_port)
        recv_until(jury_sock, until='\n') # Считать приветствие
        for flag in flags:
            print("Posting flag {}".format(flag))
            send(jury_sock, flag)
            recv_until(jury_sock, until='\n', debug=verbose) # Считать ответ
        jury_sock.close()
    except Exception as e:
        print("Got exception {}".format(e))


""" 
Пример использования:
    #...
    s = make_connect("localhost", 31337)
    recv_until(s, '>')                  # recv welcome
    send(s, "1")                        # login
    recv_until(s, 'name:')
    send(s, "qwe")
    recv_until(s, 'password:')
    send(s, "qwe")
    recv_until(s, '>')
    send(s, "2")                        # get flag by id
    recv_until(s, 'ID:')
    send(s, str(id))
    ans = recv_until(s, '>')

    flags = FLAG_RE.findall(ans)
    post_flags(flags)
"""
