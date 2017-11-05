from setuptools import setup, find_packages  
  
setup(  
    name = "HLMAnalysis",  
    version = "2.7182",  
    keywords = ("hlm", "nlp"),  
    description = "nlp for Hong Lou Meng",  
    license = "MIT Licence",  
  
    url = "https://github.com/yangminz/HLMAnalysis",  
    author = "yangminz",  
    author_email = "yangminzhao14@gmail.com",  
  
    # required dependencies
    install_requires = [
        'suffix-trees>=0.2.4.4',
    ],

    # for uninstall on Windows
    zip_safe=False
    }  
)