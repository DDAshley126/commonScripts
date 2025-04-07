from plyer import notification


def notice():
    # 设置通知的内容
    title = "标题"
    message = "这是一个来自桌面通知！"

    # 发送通知
    notification.notify(
        title=title,
        message=message,
        app_name="我的应用",  # 应用名称，会显示在通知中
        timeout=10,  # 通知持续时间（秒），0表示直到用户手动关闭
        ticker="提醒",  # 在某些系统上，这是状态栏的短暂文本提示
    )

    # 等待一段时间，以便能看到通知
    time.sleep(60)
    return True