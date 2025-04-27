# 1. Clone the repo

git clone https://github.com/你的用户名/student-growth-backend.git
cd student-growth-backend

# 2. 启动数据库（在 Docker 容器里跑 MySQL）

docker compose up -d

# Docker 会拉取 mysql:8.0 镜像，并在容器内监听 3306，

# 宿主机映射到 3307

# 3. 安装 Python 依赖

poetry install --no-root

# 这一步会根据 pyproject.toml & poetry.lock 安装 fastapi、uvicorn、pymysql 等。

# 4. 配置环境变量

# 在项目根目录建立 .env 文件，写入：

echo DATABASE_URL="mysql+pymysql://growth:growth@localhost:3307/growth" > .env

# 5. 启动 FastAPI 服务

poetry run uvicorn app.main:app --reload

# 6. 验证

curl http://localhost:8000/health

# 应看到 {"status":"ok"}
