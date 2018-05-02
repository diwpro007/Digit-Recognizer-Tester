from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Index Route'

@app.route('/hello')
def hello():
    return 'Route Hello'

# above can also be written as
# def hello_world():
#    return 'hello world'
# app.add_url_rule('/', 'hello', hello_world)

# parameterized routing
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

# use of url for for dynamic url building

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin')) #hello admin function is called
   else:
      return redirect(url_for('hello_guest',guest = name)) #hello guest function is called and for the guest argument name values is passed

# with fixed datatype

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

# for post method
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   # if request.method == 'POST':
   #    user = request.form['nm']
   #    return redirect(url_for('success',name = user))
   # else:
      user = request.args.get('nm')
      # return redirect(url_for('success',name = user))
      return '{ "name":"'+user +'" }'

if __name__ == '__main__':
   app.run(debug = True)