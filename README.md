<h2 style="color:green"> This project has been created as part
of the 42 curriculum by <spam style= "color:#FFC0CB">khnoman </spam></h4>

<h1 style> 🕹️ CALL ME MAYBE</h1>
</br>
<h3>📋 Table of Contents </h3>

<ul>
<li><a href="#overview"> Overview </a></li>
<li><a href="#Installation">Installation</a></li>
<li><a href="#Project_Description"> Project Description </a></li>
<li><a href="#Rules"> Rules </a></li>
<li><a href="#algo"> Algorithm Explanation</a> </li>
<li><a href="#Project_Structure"> Project Structure </a></li>
<li><a href="#Resources"> Resources </a></li>
<li><a href="#AI_Usage"> AI Usage </a></li>
</ul>

<h4 id="overview"> 🎯OVERVIEW</h4>
<p style="font_size: 70px;">
**Call Me Maybe** is a Python project that implements an LLM-based function calling system. It takes a user's natural language request, identifies the most appropriate function from a predefined list, extracts the required parameters, converts them to the correct data types, and generates a structured JSON output describing the function call. The project uses prompt engineering, tokenization, a small language model, Pydantic models for validation, and a state machine to produce consistently formatted results, while also handling cases where no matching function is found.

</P>

<h4 id ="Installation" > 🛠️ INSTALLATION </h4>

<h6> clone the repository </h6>
<p> git clone <my_repo_link> call_me_maybe </p>
<h6> install the packages </h6>
<p style="color:aqua"> make install</p>

<h6> run the program </h6>
<p style="color:aqua"> make run</p>
<h7> output</h7>
<code>
data/output/function_calls.json

<h2 id="Project_Description"> 📖 Project Description</h2>

<p> 

Call Me Maybe is a Python-based function calling system that uses a Small Language Model (LLM) to understand natural language requests. It identifies the most appropriate function from a predefined set, extracts the required parameters, converts them to their expected data types, and generates a structured JSON representation of the function call. The project focuses on accurate function selection, parameter extraction, and reliable JSON generation without executing the selected function.

</p>

<h2 style="font-size: 27px;" id="algo">Algorithm Explanation </h2>
<p> The project uses a constrained decoding approach to perform function calling with a Small Language Model (LLM). First, the model predicts the most suitable function for a user's natural language request from a predefined list of available functions. Once the function is identified, each parameter is extracted individually using dedicated prompts tailored to its expected type (e.g., number, integer, or string). The extracted values are then converted to the appropriate Python data types and combined into a structured JSON object. Finally, a state machine generates the output token by token, ensuring the JSON format is always syntactically correct.</p>
<h2 style="font_size: 27px;" id="design_decions"> Design Decions </h2>
<p>The implementation separates the task into two stages: function selection and parameter extraction. This modular design simplifies debugging and improves maintainability. Pydantic models are used to validate function definitions and parameter schemas, while a state machine is responsible for producing valid JSON output. Different prompt templates are used for numeric and string parameters to improve extraction accuracy, and an fn_unknown function is included to handle requests that do not match any available function.</p>

<h2 style="font_size: 27px;" id="performance_analysis"> performance_analysis </h2>
<p>The system performs efficiently because it only requires one LLM call to identify the function and one additional call for each parameter. The constrained decoding strategy significantly improves reliability by limiting the model's output to the expected format. Accuracy is high for well-defined prompts, although ambiguous or poorly phrased requests may still lead to incorrect function selection or parameter extraction.</p>


<h2 style="font_size: 27px;" id="Testing_Strategy">Testing Strategy</h2>
<p>The implementation was tested using the provided Moulinette test suite as well as additional custom test cases. Tests covered numeric, string, integer, and regular expression parameters, functions with multiple parameters, functions without parameters, invalid user requests, and JSON formatting. The generated output was compared against the expected results to verify correctness and robustness.</p>
<h4> EXAMPLE:</h4>
<pre>
<h7 style="color:yellow">make run </h7>
<br/>
<h8 style="color:red"> input prompt:</h8>
    What is the product of 3 and 5?
<br/>
<h8 style="color:green"> Output:</h8>
<code>
    {
  "prompt": "What is the product of 3 and 5?",
  "name": "fn_multiply_numbers",
  "parameters": {
    "a": 3,
    "b": 5
  }
}
</code>

</pre>
<h2 style="font-size: 27px;" id="Project_Structure">📁 Project Structure </h2>

<pre style="font-family: 'Courier New', monospace; background: #7c817875; padding: 20px; border-radius: 5px;">
call_me_maybe/
├── data/
|   └──input/
|        ├── function_calling_tests.json
|        └── functions_definition.json
├── llm_sdk/
├── algo_class.py
├── src/
|   ├── __init__.py
|   ├── __main__.py
|   ├── found_parameters.py
|   ├── models.py
|   ├── parser.py
|   ├── read_vocab.py
|   ├── start.py
|   ├── state_prompt.py
|   └── write_output.py
├── Makefile
├── README.md
└── pyproject.toml
</pre>
e.>

<div////>
    <h2  style="font-size: 27px;" id="Resources"> 📚 Resources </h2>
    <h4 style="font-size: 20px;"> Useful Links:</h4>
    <ul>
    <li> <a href="https://www.pygame.org/docs/"> pygame </a> </li>
    <li> <a href="https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/"> Dijkstra's Algorithm</a></li>
   <li><a href="https://www.youtube.com/watch?v=rvxt42na8Ss"> Explanation and solution of a Dijkstra algorithm example </a> </li>
    </ul>
    

</div>