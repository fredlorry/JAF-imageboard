# JAF-imageboard

Семестровый проект Стрельцова Антона в рамках курса "Технологии программирования".

В результате работы в течение семестра должен получится т.н. "имиджборд": *разновидность веб-форума с возможностью прикреплять к сообщениям графические файлы.*  (аналог [Доброчан](http://dobrochan.ru)).

В работе будут использованы такие инструменты, как Django, Bootstrap 3 и что-нибудь ещё.

Инструкции по установке и запуску на примере консоли Linux:
```
cd && git clone https://github.com/fredlorry/JAF-imageboard.git
cd JAF-imageboard
sudo apt-get install -y python3 pip3
pip3 install virtualenv
python3 virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python source/manage.py runserver
```

Ментор: Кутылёв Сергей Александрович.

###Мокап интерфейса: 
![Image Alt](https://github.com/fredlorry/JAF-imageboard/blob/master/diagrams/SiteMockup.png)

###Диаграмма активности по мотивам UML2:
![Image Alt](https://github.com/fredlorry/JAF-imageboard/blob/master/diagrams/UserActivityDiagram.png)

###Диаграмма последовательности по мотивам UML2:
![Image Alt](https://github.com/fredlorry/JAF-imageboard/blob/master/diagrams/UserSequenceDiagram.png)
