from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Si usas chromedriver local, pon la ruta aquí y usa la OPCIÓN B:
# CHROME_DRIVER_PATH = r"C:\RUTA\A\chromedriver.exe"

# Función para ejecutar código como si se pegara en la consola del navegador
def run_console(driver, js):
    return driver.execute_script(js)


def login_automatico(url_login, usuario_texto, password_texto, url_destino,url_destino2):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--windows-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    # OPCIÓN A: webdriver-manager (requiere internet)
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    print("🌐 Abriendo navegador...")
    driver.get(url_login)
    time.sleep(1)

    # -------- Usuario --------
    try:
        campo_usuario = driver.find_element(
            By.CSS_SELECTOR,
            "input[type='email'], input[type='text']"
        )
        print("✔ Usuario detectado.")
        time.sleep(1)
        campo_usuario.send_keys(usuario_texto)
        print("⌨ Usuario escrito.")
    except Exception as e:
        print("❌ Usuario NO detectado:", e)

    # -------- Password --------
    try:
        campo_password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        print("✔ Password detectado.")
        time.sleep(1)
        campo_password.send_keys(password_texto)
        print("🔐 Password escrita.")
    except Exception as e:
        print("❌ Password NO detectado:", e)

    # -------- Botón de login --------
    try:
        boton_login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        print("✔ Botón de login detectado.")
        time.sleep(1)
        boton_login.click()
        print("🚪 Clic en 'Iniciar sesión' ejecutado.")
    except Exception as e:
        print("❌ Botón de login NO detectado:", e)

    print("\n⏳ Esperando validación de login (3s)...")
    time.sleep(3)

    # -------- Ir a la URL interna --------
    print(f"🌐 Navegando a la sección interna: {url_destino}")
    driver.get(url_destino)

    # 🔎 Ejecutar los comandos JS equivalentes a la consola
    # Hacer click en el botón 4 y 40 como pediste
    time.sleep(25)  # Ajusta si la página tarda más en cargar
    run_console(driver, """
    const botones = document.querySelectorAll("button");
    if (botones[4]) botones[4].dispatchEvent(new MouseEvent('click', { bubbles: true }));
    """)

    time.sleep(2)  # Ajusta si la página tarda más en cargar
    run_console(driver, """
    const botones = document.querySelectorAll("button");
    if (botones[38]) botones[38].dispatchEvent(new MouseEvent('click', { bubbles: true }));
    """)

    print("🔥 JS ejecutado: clicks en button[4] y button[38]")

    # Mantener ventana abierta (si lo necesitas)
    time.sleep(180)

    


    print(f"🌐 Navegando a la sección interna: {url_destino2}")
    driver.get(url_destino2)

    # 🔎 Ejecutar los comandos JS equivalentes a la consola
    # Hacer click en el botón 4 y 40 como pediste
    time.sleep(25)  # Ajusta si la página tarda más en cargar
    run_console(driver, """
    const botones = document.querySelectorAll("button");
    if (botones[4]) botones[4].dispatchEvent(new MouseEvent('click', { bubbles: true }));
    """)

    time.sleep(2)  # Ajusta si la página tarda más en cargar
    run_console(driver, """
    const botones = document.querySelectorAll("button");
    if (botones[38]) botones[38].dispatchEvent(new MouseEvent('click', { bubbles: true }));
    """)

    print("🔥 JS ejecutado: clicks en button[4] y button[38]")

    # Mantener ventana abierta (si lo necesitas)
    time.sleep(180)



# ---------------- USO ----------------

