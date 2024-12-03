import logging
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pytest

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Device pixel sizes for reference (update if needed)
DEVICE_PIXEL_SIZES = {
    "iPhone X": "1125x2436",
    "Pixel 2": "1080x1920",
}
USER_AGENTS = {
    "iPhone X": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Pixel 2": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36"
}

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose the browser: chrome, firefox, etc.")
    parser.addoption("--device", action="store", default=None, help="Device name for mobile emulation, e.g., 'iPhone X'")

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    device_name = request.config.getoption("device")
    
    logger.info(f"Setting up browser: {browser_name} with device: {device_name}")

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--disable-gpu")  # Optional: Use this for better compatibility on some systems
    chrome_options.add_argument("--enable-logging")
    chrome_options.add_argument("--v=1")

    # Apply mobile emulation if device is specified
    if device_name:
        pixel_size = DEVICE_PIXEL_SIZES.get(device_name, "375x667")  # Default fallback
        width, height = map(int, pixel_size.split("x"))  # Split and convert to integers
        mobile_emulation = {
            "deviceMetrics": {
                "width": width,
                "height": height,
                "pixelRatio": 3.0  # Adjust as necessary
            },
            "userAgent": USER_AGENTS.get(device_name, "default_user_agent_string")  # Fallback user agent
        }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # Initialize WebDriver based on the browser name
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    request.cls.driver = driver
    yield driver
    driver.quit()
