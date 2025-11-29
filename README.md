# Watchlist 应用程序

> 📚 声明：本项目是基于[Flask入门教程](https://helloflask.com/book/3/)的学习实践项目，用于掌握Flask Web开发技能，非原创商业项目。

一个基于 Flask 和 SQLAlchemy 的电影清单应用程序，用于管理用户收藏的电影列表，支持用户认证、数据增删改查等完整功能。

## 功能特性

- 用户认证：注册、登录、登出功能
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

## 数据模型

### User 模型
- [id](file:///home/xun/MyPyCharm/watchlist/app.py#L34-L34): 整数类型主键
- [name](file:///home/xun/MyPyCharm/watchlist/app.py#L22-L22): 字符串类型，最大长度20字符
- [username](file:///home/xun/MyPyCharm/watchlist/app.py#L23-L23): 字符串类型，最大长度20字符
- [password_hash](file:///home/xun/MyPyCharm/watchlist/app.py#L24-L24): 字符串类型，存储密码哈希值

### Movie 模型
- [id](file:///home/xun/MyPyCharm/watchlist/app.py#L34-L34): 整数类型主键
- [title](file:///home/xun/MyPyCharm/watchlist/app.py#L35-L35): 字符串类型，最大长度60字符
- [year](file:///home/xun/MyPyCharm/watchlist/app.py#L36-L36): 字符串类型，最大长度4字符

## 命令行工具

### 初始化数据库
```bash
flask init-db [--drop]
```


- `--drop` 选项：在创建新表之前删除现有表

### 生成测试数据
```bash
flask forge
```


- 清空并重新创建数据库表
- 插入默认用户和预设电影数据

### 创建管理员账户
```bash
flask admin
```


- 交互式创建或更新管理员账户

## 路由

- `/` - 首页，显示用户信息和电影列表（GET/POST）
- `/login` - 用户登录页面（GET/POST）
- `/logout` - 用户登出（需认证）
- `/movie/edit/<int:movie_id>` - 编辑电影条目页面（GET/POST，需认证）
- `/movie/delete/<int:movie_id>` - 删除电影条目（POST，需认证）
- `/settings` - 用户设置页面（GET/POST，需认证）
- `404错误处理` - 自定义404页面

## 模板文件

- `base.html` - 基础模板，包含页面结构和导航
- `index.html` - 首页模板，展示用户名称、电影总数和电影列表
- `edit.html` - 编辑电影条目页面模板
- `login.html` - 用户登录页面模板
- `settings.html` - 用户设置页面模板
- `404.html` - 404错误页面模板

## 配置

数据库连接配置在 `app.py` 中设置：
```
mysql://xun:_Aa7835381@localhost:3306/data
```


## 安装和运行

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```


2. 确保MySQL服务运行并创建数据库 `data`

3. 初始化数据库并创建管理员账户：
   ```bash
   export FLASK_APP=app.py
   flask init-db
   flask admin
   ```


4. （可选）生成测试数据：
   ```bash
   flask forge
   ```


5. 运行应用：
   ```bash
   flask run
   ```


## 静态资源

- CSS样式文件位于 `static/css/style.css`
- 图片资源位于 `static/images/` 目录下，包括网站图标和装饰图片

## 许可声明

本项目基于采用 MIT 许可证的原项目进行修改学习，遵循相同许可证协议发布。