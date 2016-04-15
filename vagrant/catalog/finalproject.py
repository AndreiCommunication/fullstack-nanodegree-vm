# Flask web framework
from flask import Flask, url_for, render_template, redirect
# The name of the running application is the argument we pass to the instance
# of Flask
app = Flask(__name__)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
# makes the connection between our class definitions and corresponding tables in
# the database
Base.metadata.bind = engine
# A link of communication between our code executions and the engine created above
DBSession = sessionmaker(bind = engine)
# In order to create, read, update, or delete information on our database,
# SQLAlchemy uses sessions. These are basically just transactions. We can write
# a bunch of commands and only send them when necessary.
#
# You can call methods from within session (below) to make changes to the
# database. This provides a staging zone for all objects loaded into the
# database session object. Until we call session.commit(), no changes will be
# persisted into the database.
session = DBSession()



#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]

#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree', 'id':'1'}



# List all the restaurants
@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants )

# Add a new restaurant
@app.route('/restaurant/new')
def newRestaurant():
    return render_template('newrestaurant.html')

# Edit existing restaurant
@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    # TODO: Get the restaurant that is actually being asked for, not placeholder
    return render_template('editrestaurant.html', r=restaurant)

# Delete existing restaurant
@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    # TODO: Get the restaurant that is actually being asked for, not placeholder
    return render_template('deleterestaurant.html', r=restaurant)

# List all menu items in a particular restaurant
@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    # TODO: Replace placeholders with an actual restaurant and items
    return render_template('menu.html', r=restaurant, items=items)

# Add a new menu item for a restaurant
@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    # TODO: Replace placeholder
    return render_template('newmenuitem.html', r=restaurant)

# Edit existing menu item in a restaurant
@app.route('/restaurant/<int:restaurant_id>/menu/<int:item_id>/edit')
def editMenuItem(restaurant_id, item_id):
    # TODO: Replace placeholders
    return render_template('editmenuitem.html', r=restaurant, i=item)

# Delete existing menu item in a restaurant
@app.route('/restaurant/<int:restaurant_id>/menu/<int:item_id>/delete')
def deleteMenuItem(restaurant_id, item_id):
    # TODO: Replace placeholders
    return render_template('deletemenuitem.html', r = restaurant, i = item)

# The application run by the Python interpretor gets the name __main__
# Only run when this script is directly run, not imported.
if __name__ == '__main__':
    # Flask will use this to create sessions for our users. Make sure it is
    # secure in a production environment
    app.secret_key = 'super_secret_key'
    # Reload server each time there is a code change
    app.debug = True
    # By default the server is only accessible from the host machine and not
    # from any other computer. This is the default because a user running
    # debugging mode on my application can execute arbitrary python code on my
    # computer. So its a safety thing. Here, we make the server publically
    # available due to this being run on a vagrant environment
    app.run(host = '0.0.0.0', port = 8000)