from llama_index.core import PromptTemplate

instruction_str = """
1. Convert the query into executable Python code using panadas
2. The final line of code should be a python expression that can be called with the 'eval()' function
3. The code should represent a solution to the query
4. PRINT ONLY THE EXPRESSION
5. Do not quote the expression
 """

    
new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}
  
    Follow the instructions:
    {instruction_str}
    Query: {query}

    Expression:
    """,
    
)

