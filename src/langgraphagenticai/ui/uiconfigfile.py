from configparser import ConfigParser
# This class is used to parse and manage configuration files, typically in the INI format. 
# These files are structured with sections (enclosed in square brackets []) 
# and key-value pairs within those sections.


class Config:
    def __init__(self,config_file = "./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    #We get the all Info from the uiconfigfile.ini file
    def get_llm_options(self):
        #it will retunr all the LLLM OPtions in the Deafult one
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ") #Split by comma and space
    
    def get_use_case_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        #it will retun all the LLLM OPtions in the Deafult one
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ") #Split by comma and space
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    