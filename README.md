# daily_push
日常推送

## 目录结构
```text
│  base.py          基础配置，公共组件
│  fish_job.py      任务
│  weibo_job.py     任务
│  main.py          程序入口
│  README.md        说明
```

## 搭建
```bash
# 下载
git clone https://github.com/AkaneMurakawa/daily_push.git
# 安装依赖
pip install schedule
pip install requests
```

## 配置
见`base.py`

## 运行
```bash
python main.py &
```

## 测试
```bash
python main.py test
```