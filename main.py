from dotenv import load_dotenv
import os
import pandas as pd
# from llama_index.query_engine import PandasQueryEngine
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str


load_dotenv()

population_path = os.path.join(os.path.dirname(__file__), "data", "WorldPopulation2023.csv")
population_df = pd.read_csv(population_path)

population_qury_engine = PandasQueryEngine(df=population_df, verbose=True, instruction_str=instruction_str)
population_qury_engine.update_prompts({"panadas_prompt": new_prompt})

population_qury_engine.query("What is the population of India in 2023?")

# query = "What is the population of India in 2023?"
# response = population_qury_engine.query(query)
# print(response)

# print(population_df.head())
