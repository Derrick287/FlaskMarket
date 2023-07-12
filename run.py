from market import app

#  checks if run.py is being run as the main program and being imported as a module. 
# If it's being run as the main program, the code block below will be executed.
if __name__ == '__main__':
    app.run(debug=True)
