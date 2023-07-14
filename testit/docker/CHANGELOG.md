# Changelog

All notable changes to this project will be documented in this file.

## [4.3.0] Gemini - 03.07.2023
​
### Added
​
 - Auto-update of dynamic test suites
 - An option to set auto-update for dynamic test suites on the creation and editing stages
 - Burndown chart
 - **Clear** button in the **Archive** tabs for the following elements:
   - Projects
   - Test plans
   - Test cases
   - Configurations
 - New service in docker-compose: licensedb
 - .env variables:
   - POSTGRES_LICENSE_DB
   - POSTGRES_LICENSE_USER
   - POSTGRES_LICENSE_PASSWORD
   - LICENSE_DB_CONNECTION_STRING
​
### Changed
​
 - Updated auth service
 - Revisited webhooks:
   - Test plan status change
   - Autotest launch
   - Test point assignment
   - Selecting a user in a work item attribute
   - Tagging a user
   - Completing all test points
   - Creating a Jira issue from a test plan
   - Completing all autotests
   - Autotest completion
   - Test run stop
   - Autotest change
   - Changing relation between autotest and work item
   - Project change
   - Work item change
   - Configuration change
   - Work item attribute change
   - Testing the URL availability during webhook setup
 - Enhanced custom test suites functionality 
 - Revisited functionality of auto-updating test plan status when results test results are set
 - Switching from Backoffice to TMS
 - UX/UI improvements:
   - Smaller fonts and intervals in the right navigation bar and filter panel
   - Updated UI of test suites from sections
   - Smaller line spacing in dropdown menus
   - Improved user profile interface
   - Rearranged menu structure (second-level menus are removed from the product)
   - Fixed **Action** and **Selection** columns in tables
   - Smaller **Columns** and **Filter** buttons above table headers
 - Removed service in docker-compose: cleanup-service
 - Renamed service in docker-compose: transfer-service > background-service
 - Updated third-party container images:
   - postgres:14.7-bullseye > postgres:14.8-bookworm
   - minio/minio:RELEASE.2023-04-20T17-56-55Z > minio/minio:RELEASE.2023-05-04T21-44-30Z
   - elasticsearch:8.7.0 > elasticsearch:8.8.1
​
### Fixed
​
 - Bug fixes and performance improvements

## [4.2.4] - 06.06.2023
​
### Fixed
​
 - Bug fixes and performance improvements

## [4.2.3] - 31.05.2023

### Fixed

 - Bug fixes and performance improvements

## [4.2.0] Dorado - 27.04.2023

### Added

 - An updated form for creating a bug in Jira (for Test IT). In the Description field, the following information is available and can be populated:
   - Test case steps
   - Test point step results (if specified)
   - Comments on test point steps (if made)
   - Comments on test point
 - Read-only mode for archived entities: All the archived entities get blocked for the use and available for reading only
 - An option to assign a user to a configuration in the Execution tab
 - An option to modify a test plan via an editable header
 - Upgraded report template with an option to print out a report with attachments and comments on test points and their steps 
 - Migration to PostgreSQL 14 (refer to docs for update guide -  https://docs.testit.software/installation-guide/update-system.html)
 - New image processing library 
 - General UX/UI improvements
 - Integrations
   - Dotnet adapter for MSTest and NUnit (https://github.com/testit-tms/adapters-dotnet)
   - New tags/decorators for Python and .js-adapters: Namespace and Classname
   - A new parameter for TestIT CLI that allows splitting a classname into a namespace and a classname (https://docs.test-gear.io/user-guide/integrations/cli.html)
   - Clients for the TMS version 4.2
 - New service in docker-compose: cleanup-service
 - .env variables:
   - AVATARS_FILE_BUCKET_NAME
   - KIBANA_SERVER_HOST

### Changed

 - Updated third-party container images
  - postgres:10.23-bullseye > postgres:14.7-bullseye (refer to docs for update guide -  https://docs.testit.software/installation-guide/update-system.html)
  - minio/minio:RELEASE.2022-10-24T18-35-07Z > minio/minio:RELEASE.2023-04-20T17-56-55Z (refer to docs for update guide -  https://docs.testit.software/installation-guide/update-system.html)
  - redis:6.2.10-bullseye > redis:6.2.12-bullsey
  - elasticsearch:7.17.9 > elasticsearch:8.7.0

### Fixed

 - Bug fixes and performance improvements

## [4.1.0] Corvus - 28.03.2023

### Added 

 - Dynamic test suites have been added
 - The test suites list is now displayed on the test plan page
 - A new WI display format has been added to the "Manual Tests" page - Breadcrumbs
 - Background tasks mechanism has been added for import and export tasks
 - The archive management
   - The management of archived items has been improved, including tests, configurations, and test plans
   - The management of archived projects now occurs at the system level
   - New permissions in project roles have been added for archive management
 - API improvements
   - PATCH methods are now available for WI
   - Attachments can now be uploaded to WI
 - .env variables
   - POSTGRES_BACKGROUND_DB
   - POSTGRES_BACKGROUND_USER
   - POSTGRES_BACKGROUND_PASSWORD
   - BACKGROUND_CONNECTION_STRING

### Fixed

 - Bug fixes and performance improvements

### Changed

 - Updated third-party container images: rabbitmq:3.9.29-alpine

## [4.0.2] Phoenix - 23.03.2023

### Fixed

 - Bug fixes and performance improvements

## [4.0.1] Phoenix - 13.03.2023

### Added 

 - Yoonion Core Platform
 - Страница выбора продукта
 - Единая страница аутентификации в продукты Yoonion
 - Роль Администратор Core
 - Возможность переключения между продуктами Yoonion
 - Логотип Yoonion на общих страницах
 - В .env добавлены переменные 
    - COMPOSE_NETWORK_NAME
    - POSTGRES_PORT
    - CWM_ENABLED
    - CWM_S3_BUCKET_SECRET_KEY

### Changed

 - Переименованы переменные: 
    - DOCKER_REGISTRY    > TMS_DOCKER_REGISTRY
    - CONTAINER_VERSION  > TMS_CONTAINER_VERSION
    - FILE_BUCKET_NAME   > TMS_FILE_BUCKET_NAME
 - Переименована сеть по умолчанию из testit_network в yoonion_network
 - Сеть по умолчанию указывается как external и должна быть создана перед запуском проекта
 - Версия файла docker-compose обновлена до версии 3.5


## [4.0.0] Phoenix - 27.02.2023

### Redesign

- Меню пользователя
- Меню системы
- Меню проекта
- Профиль пользователя
- Настройки пользователя
- Страница авторизации 
- Страница "Проекты"
- Страница "Запросы"
- Страница "Дашборды"
- Страница "Параметры"
- Страница "Дашбордов"
- Страница "Уведомления"
- Раздел "Проект” и все вложенные разделы
- Проработанный новый лоадер
- Новый дизайн дерева секций
- Логирование Вебхуков
- Переработаны шрифты, иконки и цвета
- Фильтры и сортировка в едином формате
- Кнопки основных действий в едином формате

### Enhancements

- Расширен API v2
- Изменена структура docker-compose.elk.yml  - https://docs.testit.software/installation-guide/log-user-actions.html

### Security

- Все образы контейнеров Test IT теперь запускаются от пользователя testit или nginx. - https://docs.testit.software/installation-guide/update-system.html
- Обновлены сторонние образы контейнеров: postgres:10.23-bullseye, rabbitmq:3.9.22-alpine, minio/minio:RELEASE.2022-10-24T18-35-07Z, redis:6.2.10-bullseye, elasticsearch:7.17.9

### Added 

- Allure-proxy
- Адаптеры
  - Java
    - TestNg https://github.com/testit-tms/adapters-java/tree/main/testit-adapter-testng 
    - Junit4 https://github.com/testit-tms/adapters-java/tree/main/testit-adapter-junit4 
    - Junit5 https://github.com/testit-tms/adapters-java/tree/main/testit-adapter-junit5 
    - Cucumber4 https://github.com/testit-tms/adapters-java/tree/main/testit-adapter-cucumber4 
    - Cucumber5 https://github.com/testit-tms/adapters-java/tree/main/testit-adapter-cucumber5 
    - Cucumber6 https://github.com/testit-tms/adapters-java/tree/main/testit-adapter-cucumber6 
    - Cucumber7 https://github.com/testit-tms/adapters-java/tree/main/testit-adapter-cucumber7 
    - JBehave https://github.com/testit-tms/adapters-java/tree/v1.1.4/testit-adapter-jbehave 
  - Python
    - Pytest https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-pytest 
    - Behave https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-behave 
    - RobotFramework https://github.com/testit-tms/adapters-python/tree/main/testit-adapter-robotframework 
  - JS
    - Cucumber 1-7 https://github.com/testit-tms/adapters-js/tree/main/testit-adapter-cucumber 
    - Jest -https://github.com/testit-tms/adapters-js/tree/main/testit-adapter-jest 
    - Codecept - https://github.com/testit-tms/adapters-js/tree/main/testit-adapter-codecept 
- Клиенты
  - Java https://github.com/testit-tms/api-client-java 
  - Python https://github.com/testit-tms/api-client-python 
  - JS https://github.com/testit-tms/api-client-js 
  - .Net https://github.com/testit-tms/api-client-dotnet