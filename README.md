# Parser_Kinopoisk
Поставлена задача разработать "Парсер" сайта Киноафиша, который позволяет просматривать данные онлайн контента по их видам (кино, сериалы, мультфильмы). 
Программа реализована в виде функции. Функция имеет 2 аргумента. Тип контента (movies, series, animation) и номер страницы. Контент всех страниц выводить оказалось проблемой, 
так как страниц оказалось очень много. По этому есть возможность ввести номер страницы. Если при вызове функции выходит пустая строка значит страницы закончились. Так же 
программа всю информацию собирает в exel файл, который тоже можно менять и каждую страницу выводить в отдельном файле.
Чтобы программа корректно работала должен быть установлен интерпретатор Python и бибилиотеки request, BeautifulSoup, openpyxl, lxml. Установить их можно через терминал редактора 
кода PyCharm или в командной строки операционной системы. Нужно ввести следующую команду: pip install beautifulsoup4 lxml, pip install requests, pip install pandas openpyxl.
После открывается файл Tsarkov_Boris_Project_23.2.1 (HW).py через редактор (PyCharm) передаются нужные параметры при вызове функции и запускается код на выполднение. 
Результатом будет exel файл с данными выборки. 
