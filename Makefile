.DEFAULT_GOAL := help

.PHONY: help
help:
ifeq ($(OS),Windows_NT)
	@powershell -Command "[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; $$OutputEncoding = [System.Text.Encoding]::UTF8; Write-Host ''; Write-Host '==================== Доступные команды ===================='; Write-Host ''; Get-Content '$(MAKEFILE_LIST)' -Encoding UTF8 | Select-String -Pattern '^[a-zA-Z0-9_-]+:.*##' | Sort-Object | ForEach-Object { if ($$_ -match '^([^:]+):.*?##\s*(.*)$$') { Write-Host ('  {0,-28} {1}' -f $$matches[1], $$matches[2]) } }; Write-Host ''; Write-Host '==========================================================='; Write-Host ''"
else
	@echo
	@echo ==================== Доступные команды ====================
	@echo
	@grep -E '^[a-zA-Z0-9_-]+:.*##' $(MAKEFILE_LIST) 2>/dev/null | sort | awk -F ':.*## ' '{printf "  \033[36m%-28s\033[0m %s\n", $$1, $$2}'
	@echo
	@echo ===========================================================
	@echo
endif

.PHONY: install
install: ## Установка зависимостей
	poetry install --no-root

.PHONY: add
add: ## Добавление зависимостей в pyproject.toml (передавать зависимости через пробелы с помощью deps=...)
	poetry add "$(deps)"

.PHONY: remove
remove: ## Удаление зависимостей из pyproject.toml (передавать зависимости через пробелы с помощью deps=...)
	poetry remove "$(deps)"

.PHONY: migrations
migrations: ## Создание миграции (передавать комментарий через comm="...")
	alembic -c src/database/alembic.ini revision --autogenerate -m "$(comm)"

.PHONY: upgrade
upgrade: ## Применение миграций (передавать шаг/revision_id с помощью targ=...)
	alembic -c src/database/alembic.ini upgrade $(targ)

.PHONY: downgrade
downgrade: ## Откат миграций (передавать шаг/revision_id с помощью targ=...)
	alembic -c src/database/alembic.ini downgrade $(targ)

.PHONY: up
up: ## Сборка и запуск контейнеров
	docker-compose -p shadow-chat -f ./devops/docker-compose.yaml up -d --build

.PHONY: down
down: ## Остановка и удаление контейнеров
	docker-compose -p shadow-chat down
