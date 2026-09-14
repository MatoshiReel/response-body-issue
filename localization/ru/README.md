## response-body-issue: Python библиотека стандартизированных HTTP ответов.
***
[![license](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE)

## Описание
***

Библиотека response-body-issue содержит DTO-классы для HTTP-ответов с кодами 4xx.
Библиотека предоставляет единый формат тела ответа 
для серверных архитектур на основе микросервисов.
Она позволяет сервисам использовать единообразный контракт ошибок, 
не раскрывая детали внутренней реализации, такие как 
классы сервисов, исключения, внутренняя архитектура или используемые фреймворки.

## Содержание
***

- [Начало работы](#начало-работы)
- [Использование](#использование)
- [Внутренняя структура](#внутренняя-структура)
- [Лицензия](#лицензия)

## Начало работы
***

Чтобы собрать проект, выполните следующие команды в корневом каталоге проекта:

1. Создайте виртуальное окружение:
```bash
python -m venv .venv
```
2. Активируйте виртуальное окружение:

* Linux и macOS:
```bash
source .venv/bin/activate
```
* Windows (в cmd):
```bash
.venv\Scripts\activate
```
3. Проверьте, что `pip` работает внутри этой среды:
```bash
python -m pip --version
```
4. Сборка проекта:
```bash
python -m pip install build && python -m build
```
Файл .whl библиотеки будет сгенерирован в /dist каталоге проекта.

Чтобы установить response-body-issue в качестве зависимости в другом проекте,
создайте /dist каталог в корневом каталоге проекта, который будет использовать библиотеку.
Скопируйте сгенерированный файл .whl в только что созданный /dist каталог
и выполните следующую команду в корневом каталоге проекта:
```bash
pip install ./dist/response_body_issue-0.1.0-py3-none-any.whl
```

## Использование
***

1. Простой пример создания сущности `RequestError` без параметров для сообщения:
```python
from resbo.error import RequestError
from resbo.reason import ErrorReason

RequestError(errorReason=ErrorReason.JSON_FORMAT.name).system_message()
```

Результат в формате JSON:

```json
{
  "errorReason" : "JSON_FORMAT",
  "message" : "Invalid JSON format."
}
```

2. Пример создания сущности `RequestError` с одним параметром 
для стандартизированного сообщения, сгенерированного с помощью `ErrorMessageFactory`:
```python
from resbo.error import RequestError
from resbo.reason import ErrorReason

RequestError(errorReason=ErrorReason.EMPTY.name).system_message("field_name") # {} is empty or null.
```

Результат в формате JSON:

```json
{
  "errorReason" : "EMPTY",
  "message" : "field_name is empty or null."
}
```

3. Пример создания сущности `RequestFieldError` с несколькими параметрами 
для стандартизированного сообщения, сгенерированного с помощью `ErrorMessageFactory`:
```python
from resbo.error import RequestFieldError
from resbo.reason import ErrorReason

RequestFieldError(errorReason=ErrorReason.LESS_SIZE.name, field="password").system_message("password", "6") # {} cannot be less than {}.
```

Результат в формате JSON:

```json
{
  "field" : "password",
  "errorReason" : "LESS_SIZE",
  "message" : "password cannot be less than 6."
}
```

4. Пример создания сущности `RequestFieldError` с кастомным сообщением:
```python
from resbo.error import RequestFieldError
from resbo.reason import ErrorReason

RequestFieldError(errorReason=ErrorReason.LESS_SIZE.name, field="password").custom_message("Password cannot be less than 6 characters!")
```

Результат в формате JSON:

```json
{
  "field" : "password",
  "errorReason" : "LESS_SIZE",
  "message" : "Password cannot be less than 6 characters!"
}
```

Чтобы определить количество параметров, 
необходимых для стандартизированного сообщения, 
обратитесь к docstring документации класса ErrorMessageFactory.

## Внутренняя структура
***

- **Issue** - содержит базовый DTO-класс для описания проблемы запроса.
- **Error** - содержит DTO-классы для HTTP-ответов с кодом 4xx.
- **Reason** - содержит перечисление, определяющее причины ответов с кодом 4xx.
- **Message** - содержит класс-фабрику для создания стандартизированных сообщений об ошибках.

## Лицензия
***

Этот проект распространяется на условиях лицензии MIT.