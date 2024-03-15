# WordMath

**WordMath** - это скрипт на питоне, возвращающий числовой ответ данного строкого выражения.

## Требования
- Установленная библиотека word2number
```
pip install word2number
```

## Установка и настройка
- Склонируйте репозиторий
```
git clone https://github.com/koloideal/WordMath.git
```


## Примечания
- Актуальная версия скрипта (v1.0) поддерживает выражения только с двумя операндами.
  
- Выражения должны иметь вид: first_operand operator second_operand.
  
- В актуальной версии скрипта (v1.0) реализована поддержка только английского языка.
  
- Скрипт поддерживает такие операции как: сложение(+), вычитание(-), деление(/), умножение(*), возведение в степень(**).
  
- Максимально возможное число каждого операнда - 1 000 000 0000 (один миллиард).
  
- Стандартный строковый вид операторов выглядит так: plus(+), minus(-), multiply(*), divide(/), degree(**).
  
- Также реализована поддержка алиасов(синонимов) для каждого оператора, подробнее с синонимами каждого оператора можно ознакомиться в словаре `act` в функции `main` в файле `main.py.
  
- При желании добавления алиасов добавьте желаемый синоним в кортеж, являющийся ключом соответствующего оператора в словаре `act` в функции `main` в файле `main.py`
  
- Есть возможность ввода десятичных дробей, в этом случае необходимо разделить целую и десятичную часть словом `point`, пример - `nine point eight`.
  
- Примеры возможных запросов:
  - `seven plus three`
  - `one million eight hundred six times seven`
  - `twenty one stage two`
  - `eight point one separate one point six`


**Ремарка:** Данный скрипт не является исчерпывающим, есть много способов улучшить и модернизировать, поэтому всегда рад вашим предложениям и идеям.

