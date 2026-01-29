import allure
from allure_commons.types import AttachmentType
import os


# Скриншоты
def add_screenshot(browser):
    png = browser.get_screenshot_as_png()
    allure.attach(
        body=png,
        name='screenshot',
        attachment_type=AttachmentType.PNG
    )

# логи
def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.get_log(log_type='browser'))
    allure.attach(
        log,
        name='browser_logs',
        attachment_type=AttachmentType.TEXT
    )

# html-код страницы
def add_html(browser):
    html = browser.page_source
    allure.attach(
        html,
        name='page_source',
        attachment_type=AttachmentType.HTML
    )

# скринкаст
def add_video(browser):
    selenoid_url = os.getenv("SELENOID_URL")
    if not selenoid_url:
        return  # Не прикреплять видео, если URL не настроен

    video_url = f"https://{selenoid_url}/video/{browser.session_id}.mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(
        html,
        name='video_' + browser.session_id,
        attachment_type=AttachmentType.HTML
    )