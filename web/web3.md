# Cross-Site Scripting (XSS)

## О чем говорили
+ Что такое DOM и откуда "растёт" HTML
+ Как из JavaScript можно взаимодействовать с DOM и что нам это даёт
+ Что такое контекст атаки и почему он важен при эксплуатации XSS
+ Какие бывают контексты:
  - HTML context
  - JavaScript context
    1. В коде
    2. В строке
    1. В другом месте внутри JS
  - Attribute context
    1. В значении атрибута
    2. Среди других атрибутов
  - Менее распространённые контексты
+ О том что такое BugBounty и почему это хорошо

## Что почитать
1. [XSS для новичков](https://forum.antichat.ru/threads/20140/).
2. [В поисках лазеек: гид по DOM Based XSS](https://habrahabr.ru/company/xakep/blog/189210/)
3. [Вся правда об XSS или Почему межсайтовое выполнение сценариев не является уязвимостью?](https://habrahabr.ru/company/pt/blog/149152/).
4. [Коротко о BugBounty](https://habrahabr.ru/company/pentestit/blog/335676/)

## Что порешать
1. [SiBears XSS Game](http://xss.school.sibears.ru/).

## Справочные материалы
1. [OWASP XSS Filter Evasion Cheat Sheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet).
2. [XSS Cheat Sheet](http://brutelogic.com.br/blog/cheat-sheet/).
3. [OWASP Cross-site Scripting (XSS) Attack](https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)).
4. Списки BugBounty программ:
    - [BugCrowd](https://www.bugcrowd.com/bug-bounty-list/)
    - [Hackerone](https://hackerone.com/directory?query=type%3Ahackerone&sort=published_at%3Adescending&page=1)
