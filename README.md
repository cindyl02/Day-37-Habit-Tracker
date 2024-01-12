## Habit Tracker (Day 37)
### About
This project uses Pixela API to keep track of daily habits. To create a new graph, update graph_params with a new GRAPH_ID, name, unit, and type. 

### How to setup project
Go to pixela website and create a new account. Update USERNAME and TOKEN from your account in `main.py`. 
Create a new user if not already which will use the USERNAME and TOKEN in user_params. 

### How to run the project
1. Run main.py to create new graph.
2. Go to your Pixela account and look for your graph under the link `https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}`.
3. To post a new pixel, use post_pixel_endpoint. It will use the current date and post a pixel under today.  
4. To update a pixel with new data, use update_pixel_endpoint. 
5. To delete a pixel, use the delete_endpoint. 

