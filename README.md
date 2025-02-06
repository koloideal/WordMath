# WordMath

**WordMath** - это скрипт на питоне, возвращающий числовой ответ данного строкого выражения.

## Требования
- **Установленный `Python` версии 3.12+**
- Варианты установки:
- - - - - 
- **Linux:**
- Установка утилиты для установки Python
```bash
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
curl https://pyenv.run | bash
```
- Установка переменных окружения(опционально)
```bash
echo -e 'export PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'eval "$(pyenv init --path)"\neval "$(pyenv init -)"' >> ~/.bashrc
```
- Непосредственная установка и настройка
```bash
pyenv install 3.13.0
pyenv global 3.13.0
```
- - - - -
- **Windows:**
- Установка утилиты для установки Python
- Для установки необходимо включить выполнение сценариев в системе, для этого откройте терминал от имени администратора и введите:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```
Далее установка утилиты
```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```
Непосредственная установка и настройка
```powershell
pyenv install 3.13.0
pyenv global 3.13.0
```
- - - - -
- Установленный пакетный менеджер Poetry
```
pip install poetry
```
  

## Установка и настройка
- Склонируйте репозиторий
```bash
git clone https://github.com/koloideal/WordMath.git
```
- Находясь в директории проекта
```bash
poetry install
```


## Примечания
- Актуальная версия скрипта (v4.0.0) поддерживает выражения с неограниченным количеством операндов.
  
- Скрипт поддерживает такие операции как: сложение(+), вычитание(-), деление(/), умножение(*), возведение в степень(**).
  
- Максимально возможное число каждого операнда - 1 000 000 0000 (один миллиард).
  
- Стандартный строковый вид операторов выглядит так: plus(+), minus(-), multiply(*), divide(/), degree(**).
  
- При желании добавления алиасов добавьте желаемый синоним в json к соответствующему базовому оператору, `src/app/local_data/operator_synonyms.json`
  
- Есть возможность ввода десятичных дробей, в этом случае необходимо разделить целую и десятичную часть словом `point`, пример - `nine point eight`.
  
- Примеры возможных запросов:
  - `seven plus three`
  - `one million eight hundred six times seven`
  - `twenty one stage two`
  - `eight point one separate one point six`


**Ремарка:** Функционал данного скрипта не является исчерпывающим, поэтому всегда рад вашим предложениям и идеям.

