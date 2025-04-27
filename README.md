# Student Growth Backend

## 快速启动指南

### 前置条件:

#### Docker & Docker Compose

#### Python 3.11.x

#### Poetry (Python 依赖和虚拟环境管理工具)

```bash
pip install poetry
```

### 1. 克隆仓库

```bash
git clone https://github.com/你的用户名/student-growth-backend.git
cd student-growth-backend
```

### 2. 启动数据库

```bash
docker compose up -d
```

### 3. 安装 Python 依赖

```bash
poetry install --no-root
```

### 4. 配置环境变量

```bash
cp .env.example .env
```

### 5. 启动 FastAPI 服务

```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 6. 验证

```bash
curl http://localhost:8000/health
```
