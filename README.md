# 物业管理系统

一个基于 Django 和 Django REST Framework 开发的现代化物业管理系统。

## 功能特点

### 1. 物业管理
- 房产信息管理（添加、修改、删除）
- 业主信息管理
- 房产状态跟踪（已占用/空置）
- 基于权限的访问控制

### 2. 收费管理
- 支持多种收费类别（水费、电费、物业费等）
- 收费记录管理
- 费用状态追踪（待缴费、已缴费、已逾期）
- 自动计算欠费和逾期

### 3. 报表系统
- 综合报表
- 物业统计（总数、占用率等）
- 收费统计（总额、已收、待收等）
- 支持 Excel 导出

### 4. 用户管理
- 基于角色的权限控制
- 用户认证和授权
- 管理员和普通用户分离

## 技术栈

- Python 3.8+
- Django 4.2.7
- Django REST Framework 3.14.0
- PostgreSQL（可选，默认使用 SQLite）
- Bootstrap 5
- Celery 5.3.4（异步任务）
- Redis 5.0.1（缓存和消息队列）

## 快速开始

1. 克隆项目
```bash
git clone [项目地址]
cd WYSFXT-windsuf
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 初始化数据库
```bash
python manage.py migrate
```

4. 创建管理员用户（如果尚未创建）
```bash
python manage.py createsuperuser
```

5. 收集静态文件
```bash
python manage.py collectstatic
```

6. 启动开发服务器
```bash
python manage.py runserver
```

7. 访问系统
- 主页：http://127.0.0.1:8000/
- 管理后台：http://127.0.0.1:8000/admin/
- API文档：http://127.0.0.1:8000/api/

## API 端点

### 物业管理
- GET /api/properties/ - 获取物业列表
- POST /api/properties/ - 创建新物业
- GET /api/properties/{id}/ - 获取特定物业详情
- PUT /api/properties/{id}/ - 更新物业信息
- DELETE /api/properties/{id}/ - 删除物业

### 收费管理
- GET /api/charges/ - 获取收费记录列表
- POST /api/charges/ - 创建新收费记录
- GET /api/charges/{id}/ - 获取特定收费记录
- PUT /api/charges/{id}/ - 更新收费记录
- DELETE /api/charges/{id}/ - 删除收费记录

### 报表
- GET /api/reports/comprehensive/ - 获取综合报表
- GET /api/reports/property-stats/ - 获取物业统计
- GET /api/reports/charge-stats/ - 获取收费统计
- GET /api/reports/export/excel/ - 导出Excel报表

## 后续更新计划

### 近期计划（v1.1）
1. 用户界面优化
   - [ ] 添加响应式数据表格
   - [ ] 改进表单验证和错误提示
   - [ ] 添加数据可视化图表

2. 功能增强
   - [ ] 添加批量导入导出功能
   - [ ] 实现费用自动计算
   - [ ] 添加消息通知系统

3. 报表功能扩展
   - [ ] 添加更多报表模板
   - [ ] 支持自定义报表
   - [ ] 添加报表定时发送功能

### 中期计划（v1.2）
1. 移动端适配
   - [ ] 开发移动端API
   - [ ] 优化移动端界面
   - [ ] 添加微信小程序支持

2. 系统集成
   - [ ] 集成支付系统
   - [ ] 添加短信通知功能
   - [ ] 集成物联网设备数据

3. 性能优化
   - [ ] 添加缓存机制
   - [ ] 优化数据库查询
   - [ ] 实现异步任务处理

### 长期计划（v2.0）
1. 智能化功能
   - [ ] 添加数据分析功能
   - [ ] 实现智能报警系统
   - [ ] 添加预测分析功能

2. 平台化发展
   - [ ] 支持多物业公司
   - [ ] 添加云端部署支持
   - [ ] 实现多租户架构

3. 生态系统建设
   - [ ] 开发插件系统
   - [ ] 提供API市场
   - [ ] 建立开发者社区

## 贡献指南

欢迎提交 Issue 和 Pull Request。在提交之前，请确保：

1. Issue 未被重复提交
2. Pull Request 包含完整的测试
3. 代码符合项目规范
4. 更新相关文档

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。
