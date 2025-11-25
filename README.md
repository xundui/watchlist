# Watchlist Application

> 📚 声明：本项目是基于[Flask入门教程](https://helloflask.com/book/3/)的学习实践项目，用于掌握Flask Web开发技能，非原创商业项目。

一个基于 Flask 和 SQLAlchemy 的电影清单应用程序，用于管理用户收藏的电影列表。

## 功能特性

- 用户管理：存储和展示用户信息
- 电影收藏：添加和浏览电影条目
- 数据库管理：通过命令行工具初始化和填充数据
- Web界面：展示用户的电影收藏列表
- 错误处理：自定义404页面

## 技术栈

- **框架**: Flask
- **数据库**: MySQL (通过 SQLAlchemy ORM)
- **模板引擎**: Jinja2
- **命令行工具**: Click

## 数据模型

### User 模型
- [id](file:///home/xun/MyPyCharm/watchlist/app.py#L31-L31): 整数类型主键
- [name](file:///home/xun/MyPyCharm/watchlist/app.py#L28-L28): 字符串类型，最大长度20字符

### Movie 模型
- [id](file:///home/xun/MyPyCharm/watchlist/app.py#L31-L31): 整数类型主键
- [title](file:///home/xun/MyPyCharm/watchlist/app.py#L32-L32): 字符串类型，最大长度60字符
- [year](file:///home/xun/MyPyCharm/watchlist/app.py#L33-L33): 字符串类型，最大长度4字符

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
- 插入默认用户"Xun"和10部预设电影数据

## 路由

- `/` - 首页，显示用户信息和电影列表
- `/movie/edit/<int:movie_id>` - 编辑电影条目页面
- `/movie/delete/<int:movie_id>` - 删除电影条目
- `404错误处理` - 自定义404页面

## 模板文件

- `index.html` - 首页模板，展示用户名称、电影总数和电影列表
- `edit.html` - 编辑电影条目页面模板
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

3. 运行应用：
   ```bash
   export FLASK_APP=app.py
   flask init-db
   flask forge
   flask run
   ```


## 静态资源

- CSS样式文件位于 `static/css/style.css`
- 图片资源位于 `static/images/` 目录下，包括网站图标和装饰图片

## 许权声明

本项目基于采用 MIT 许可证的原项目进行修改学习，遵循相同许可证协议发布。
原项目声明：This project is licensed under the MIT License.