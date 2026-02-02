from playwright.sync_api import sync_playwright
import yaml

with open("framework/config.yaml", "r") as f:
    config = yaml.safe_load(f)

def launch_browser():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    return p, browser, page

def login(page):
    page.goto(f"{config['base_url']}/login")
    page.fill(config['selectors']['login']['username'], config['credentials']['username'])
    page.fill(config['selectors']['login']['password'], config['credentials']['password'])
    page.click(config['selectors']['login']['submit'])