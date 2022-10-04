from website import create_app

app = create_app()

#only if main.py is run, wile app.run be executed 
#debug=True  -> any change will automatically rerun the server
if __name__ ==  '__main__':
    app.run(debug=True)