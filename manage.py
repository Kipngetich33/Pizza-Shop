from app import create_app


#creatin the instance of the app
app = create_app('development')

if __name__ == '__main__':
    app.run()