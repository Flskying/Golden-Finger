
# Golden-Finger

## 项目简介
**Golden-Finger** 是一个基于 Python 开发的自动化工具，专注于为游戏《金铲铲之战》提供辅助功能（如自动点击、循环操作等），通过图像识别和模拟键鼠操作实现简单高效的自动化流程。项目结构轻量，易于扩展，适合需要重复操作的游戏场景。


## 核心功能
- **自动任务执行**：支持自定义循环逻辑，简化重复操作（如刷副本、领取奖励等）。  
- **图像识别点击**：通过模板匹配技术定位游戏界面元素，实现精准点击（依赖 `zan.png`、`like.png` 等图片模板）。  
- **热键控制**：支持通过快捷键启动/暂停程序，灵活控制自动化流程。  


## 安装与运行
### 环境要求
- Python 3.7+  
- 依赖库：`pyautogui`、`keyboard`、`Pillow`  
  ```bash
  pip install pyautogui keyboard Pillow
  ```

### 使用步骤
1. 克隆项目到本地：  
   ```bash
   git clone https://github.com/Flskying/Golden-Finger.git
   ```
2. 打开 `金铲铲.py`，根据需求修改配置（如循环次数、点击坐标、图片模板路径等）。  
3. 运行脚本：  
   ```bash
   python 金铲铲.py
   ```
4. 通过预设热键（默认为 `F1` 启动，`F2` 暂停）控制程序运行。  


## 文件结构
```
Golden-Finger/
├─ 3.png          # 界面截图或模板图片（示例文件）
├─ like.png       # 点赞/确认按钮模板
├─ like2.png      # 备用按钮模板
├─ zan.png        # 点赞按钮模板（中文）
├─ 金铲铲.py      # 核心脚本文件
└─ README.md      # 项目说明文档
```


## 自定义配置
- **图像模板**：将需要识别的游戏界面元素截图保存为 `.png` 文件（如 `zan.png`），放置在项目根目录，通过 `pyautogui.locateOnScreen()` 方法调用。  
- **操作逻辑**：在 `金铲铲.py` 中修改 `main()` 函数内的循环逻辑，添加点击坐标、等待时间、条件判断等自定义功能。  
- **热键设置**：通过 `keyboard.add_hotkey()` 方法调整启动/暂停快捷键（需注意避免与系统热键冲突）。  


## 注意事项
1. 请在合法合规范围内使用本工具，避免违反游戏用户协议。  
2. 不同分辨率或界面版本可能导致图像识别失败，建议根据实际界面调整模板图片或坐标参数。  
3. 运行时请确保游戏窗口处于前台且分辨率一致。  


## 贡献与反馈
欢迎提交代码改进、BUG 反馈或新功能建议：  
1. 提交 Issues：在 [GitHub 仓库](https://github.com/Flskying/Golden-Finger/issues) 中描述问题或需求。  
2. 提交 Pull Request： fork 项目后修改代码并提交合并请求。  


## 许可证
本项目采用 **MIT 许可证**，详见 [LICENSE](https://github.com/Flskying/Golden-Finger/LICENSE)（如需添加，请自行创建）。


## 联系作者
如有问题或合作意向，可通过 GitHub 仓库私信或邮箱联系（暂未提供，建议补充）。

---
**Enjoy automating!** 🚀