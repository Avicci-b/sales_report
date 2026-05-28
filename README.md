# Sales Report Generator
A small project that will give informations about a demo produces sales data using FastAPI to serve the data on the web

Step 1: Create a virtual Environment 

Step 2: Create a file that will accept things that are not pushed to remore place

Step 3: Create a requirements.txt folder to store dependecies 

    ```bash
    pip install -r requirements.txt

step 4: Create folders using mkdir data api anlysis/results

step 5: We need some data to do analysis so lets add it in generate_data.py

Step 6: we need to compute results so we will create a analyze.py in analysis folder

Step 7: I have added sales_data.csv to .gitignore and added script folder for python files

Step 8: The JSON files are now produced in results/ that will tell us customer details, monthly sales, segment counts, and summary.

Step 9: Created a server.py in api/ to serve the JSON files like I am just serving it to the web.It is static. For production, I'd likely replace static JSON loading with a database or cached service. 

    ```bash
    uvicorn api.server:app --reload

Step 10: Clear ur code and make commits then push only necessarry files to GitHub.
