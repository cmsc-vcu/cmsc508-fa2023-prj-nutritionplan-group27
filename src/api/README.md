# API Folder

## server.py
This is the file that contains the base server code. It links to several routes in the routes folder using flask's blueprint functionality. Instructions on running it are below
1. To run the server look at the includes in server.py and ensure everything there is installed
2. Then you can just run the file which will open the server on port 5000 of localhost/127.0.0.1

## send.py
This is the file that was used to send data to the API
1. To send data to the API first tweak the headers based on the API's definition to ensure you get the responses you desire
2. Then use the command 'python send.py <endpoint>' where <endpoint> is the endpoint you want to reach, for example /users/mealplans
3. send.py will print the returned json to the console for you
