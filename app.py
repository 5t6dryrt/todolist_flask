from flask import Flask,render_template,request,url_for

app = Flask(__name__)
coffee = []
@app.route('/')
def hello():
   if len(coffee) == 0:
      coffee.append({"name":"tea","price":45})
      coffee.append({"name":"tasdadea","price":452})
      
      
      print(coffee)
      return render_template('index.html',coffeeList = coffee)
   
   else:
      print(coffee)
      return render_template('index.html',coffeeList = coffee)

@app.route('/delete' ,methods = ['POST'])
def delete_item():
    data = request.form
    coffee_name = data.get('listName')  # Assuming 'checkbox' is the name attribute in your HTML form
    print(coffee_name)
    print(coffee)
    # Find the selected coffee item in the list
    res = None
    for sub in coffee:
        if sub['name'] == coffee_name:
            res = sub
            break
    print(res)
    if res:
        # Get the index of the item to delete
        index = coffee.index(res)
        
        # Delete the item from the list
        deleted_item = coffee.pop(index)

        # Print the deleted item (for demonstration purposes)
        print(f"Deleted Coffee: {deleted_item['name']} (Price: ${deleted_item['price']})")
        
        # You can perform additional actions here if needed
        
        
        return render_template('index.html',coffeeList = coffee)
    else:
        return render_template('index.html',coffeeList = coffee)
    
   

@app.route('/',methods = ['POST'])  
def createnew():  
      data = request.form
      coffeeNew = data.get("newItemName")
      priceNew =data.get("newItemPrice")

      coffee.append({"name":coffeeNew,"price":priceNew})
      
      
      
      return render_template('index.html',coffeeList =coffee)

app.run(debug=True)