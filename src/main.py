# Import the libraries needed to find elements and manipulate the browser
from selenium import webdriver
from selenium.webdriver.common.by import By

# Import exceptions
from selenium.common.exceptions import *

# Import custom log function
from utils.custom_log import *

# Import data functions
from utils.data_utils import *

# Import xlsx data
data_path = r"data\challenge.xlsx"
df = load_excel(data_path)

def main():
    
    # Tries to create the log, open the web browser and start the RPA Challenge
    try:

        # Get the name of the python file that is being executed to create the log folder
        nome_arquivo_py = os.path.basename(__file__).replace('.py', '')

        # Creates the log
        log_create(nome_arquivo_py)
        log_append("Início do RPA Challenge")

        # Initializes the driver (in this case, Edge)
        driver = webdriver.Edge()

        # Opens the desired page and maximizes the window
        driver.get("https://rpachallenge.com/")
        driver.maximize_window()
        log_append("Navegador inicializado na página do RPA Challenge")

        # Click the START button
        start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
        start_button.click()
        log_append("Realizado click no botão START")
    
    except Exception as e:
        log_append(f"Ocorreu um erro - {e.__class__.__name__}")

    # Counter of the rounds (loop) of the RPA Challenge
    round = 1

    # Loop to fill the fields and submit for the data of each line of the XLSX file
    for index, row in df.iterrows():

        try:
            # Filling in the First Name input field
            first_name_field = driver.find_element(By.XPATH, "//div[label[text()='First Name']]/input")
            first_name_field.send_keys(row['First Name'])

            # Filling in the Last Name input field
            last_name_field = driver.find_element(By.XPATH, "//div[label[text()='Last Name']]/input")
            last_name_field.send_keys(row['Last Name '])

            # Filling in the Company Name input field
            company_name_field = driver.find_element(By.XPATH, "//div[label[text()='Company Name']]/input")
            company_name_field.send_keys(row['Company Name'])

            # Filling in the Role in Company input field
            role_field = driver.find_element(By.XPATH, "//div[label[text()='Role in Company']]/input")
            role_field.send_keys(row['Role in Company'])

            # Filling in the Address input field
            adress_field = driver.find_element(By.XPATH, "//div[label[text()='Address']]/input")
            adress_field.send_keys(row['Address'])

            # Filling in the Email input field
            email_field = driver.find_element(By.XPATH, "//div[label[text()='Email']]/input")
            email_field.send_keys(row['Email'])

            # Filling in the Phone Number input field
            phone_field = driver.find_element(By.XPATH, "//div[label[text()='Phone Number']]/input")
            phone_field.send_keys(row['Phone Number'])

            # Click the SUBMIT button
            submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
            submit_button.click()
            log_append(f"Realizado click no botão SUBMIT para os dados da linha {round}")

            round += 1

        except Exception as e:
            log_append(f"Ocorreu um erro no round {round} - {e.__class__.__name__}")
            break
    
    # Condition that verifies if the bot ran successfully for 10 rounds
    if round == 11:
        log_append("Realização do RPA Challenge concluída com sucesso")
        success_message = driver.find_element(By.XPATH, "//div[@class='message2']").text
        log_append(f'Resultado: {success_message}')

    log_append("Finalizando automação do RPA Challenge")

# Performs the main function
main()