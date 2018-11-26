# ProductRestApi
Test django rest framework 

## Настройка и запуск DEV-окружения

    # Сборка всех контейнеров
    docker-compose build
    # Запуск миграций БД
    docker-compose run backend python manage.py migrate
    # Запуск контейнеров
    docker-compose up
    
    
    # Для запуска тестов
    docker-compose run backend pytest