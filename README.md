# Watchlist 应用程序

> 📚 声明：本项目是基于[Flask入门教程](https://helloflask.com/book/3/)的学习实践项目，用于掌握Flask Web开发技能，非原创商业项目。

一个基于 Flask 和 SQLAlchemy 的电影清单应用程序，用于管理用户收藏的电影列表，支持用户认证、数据增删改查等完整功能。

![License](https://img.shields.io/github/license/greyli/watchlist)
![Python Version](https://img.shields.io/badge/python-3.7+-blue)
![Flask Version](https://img.shields.io/badge/flask-3.1.2-green)

## 目录

- [功能特性](#功能特性)
- [技术栈](#技术栈)
- [数据模型](#数据模型)
- [安装与配置](#安装与配置)
- [使用说明](#使用说明)
- [命令行工具](#命令行工具)
- [测试](#测试)
- [许可证](#许可证)

## 功能特性

- 用户认证：登录、登出功能
- 电影管理：添加、编辑、删除电影条目
- 数据展示：首页展示所有电影列表
- 权限控制：仅认证用户可执行增删改操作
- 数据库管理：通过命令行工具初始化和填充数据
- 错误处理：自定义404页面
- 用户设置：修改用户名称

## 技术栈

- **框架**: Flask 3.1.2
- **数据库**: MySQL (通过 SQLAlchemy 2.0.44 ORM)
- **模板引擎**: Jinja2
- **命令行工具**: Click 8.1.8
- **用户认证**: Flask-Login 0.6.3
- **安全**: Werkzeug 3.1.4 (密码哈希)
- **前端**: HTML, CSS

## 数据模型

### User 模型
- [id](file:///home/xun/MyPyCharm/watchlist/watchlist/models.py#L26-L26): 整数类型主键
- [name](file:///home/xun/MyPyCharm/watchlist/watchlist/models.py#L13-L13): 字符串类型，最大长度20字符
- [username](file:///home/xun/MyPyCharm/watchlist/watchlist/models.py#L14-L14): 字符串类型，最大长度20字符
- [password_hash](file:///home/xun/MyPyCharm/watchlist/watchlist/models.py#L15-L15): 字符串类型，存储密码哈希值

### Movie 模型
- [id](file:///home/xun/MyPyCharm/watchlist/watchlist/models.py#L26-L26): 整数类型主键
- [title](file:///home/xun/MyPyCharm/watchlist/watchlist/models.py#L27-L27): 字符串类型，最大长度60字符
- [year](file:///home/xun/MyPyCharm/watchlist/watchlist/models.py#L28-L28): 字符串类型，最大长度4字符

## 安装与配置

1. 克隆项目到本地：
```bash
git clone https://github.com/xundui/watchlist.git
cd watchlist
```
2. 创建并激活虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. 安装依赖：
```bash
pip install -r requirements.txt
```
4. 配置环境变量：
   在项目根目录创建 `.env` 文件，并添加以下内容：
```
SECRET_KEY=your-secret-key
DATABASE_URL=mysql://username:password@host:port/database
```
5. 初始化数据库：
```bash
flask init-db
```
## 使用说明

1. 启动开发服务器：
```bash
flask run
```
2. 访问应用：
   打开浏览器访问 http://127.0.0.1:5000

3. 创建管理员账户：
```bash
flask admin
```
## 命令行工具

### 初始化数据库
```bash
flask init-db [--drop]
```
选项：
- `--drop`: 删除现有数据后再重新创建

### 生成测试数据
```bash
flask forge
```
### 创建/更新管理员账户
```bash
flask admin [--username USERNAME] [--password PASSWORD]
```
选项：
- `--username`: 设置用户名
- `--password`: 设置密码

## 测试

运行测试套件：
```bash
python -m unittest
```
测试覆盖了以下功能：
- 应用存在性和配置测试
- 404页面处理
- 首页显示
- 登录保护机制
- 用户登录/登出功能
- 设置页面功能
- 电影条目的增删改查操作
- 命令行工具功能

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情