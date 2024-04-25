from flask import abort,render_template,redirect,url_for
from flask import jsonify
from flask import request,session
from flask import make_response 

from werkzeug.security import generate_password_hash, check_password_hash

from Api import app
from .models import User_Details, User_DetailsSchema,User_Complains,User_Complains_Schema, db
print("ssss")

app.secret_key = "asdsadsdvbvsdgvcgjsdvvsdcvg"

user_details_schema = User_DetailsSchema()
user_details_List_schema = User_DetailsSchema(many=True)

user_complains_schema = User_Complains_Schema()
user_complainsLst_schema = User_Complains_Schema(many=True)


@app.route("/")
def index():
    print("Hekli")
  
    return render_template('index.html')


@app.route("/signup", methods=["POST","GET"])
def signup():
    """endpoint to create new todo_item"""
    if request.method =="POST":
        print("IN POST")
        try:
            email =request.form['email']
                
            password = request.form['password']
            cpassword = request.form['cpassword']
            print(email,password)
            if password == cpassword:
                user_details_item  = User_Details(email,password)
                db.session.add(user_details_item)
                db.session.commit()
                return {"status":"OK"}
            else:
                return {"status":"Password and Confirm password Not same"}
        except:
            return {"status":"Email already exists"}
    return render_template('signup.html')

@app.route("/login", methods=["GET","POST"])
def login():
    """endpoint to show all todo items"""
    if request.method =="POST":
        if request.form['email'] =='admin@gmail' and request.form['password'] =='admin123':
            return {'user':'admin'}

        user = User_Details.query.filter_by(email=request.form['email']).first()
        try:
            email = user.email
            session['loggedin'] = True
            session['email'] = email
        
            password= user.password
            # print(email,password)
            if password == request.form['password'] :
                # print(password)
                # result = user_details_List_schema.dump(result)
        
                
        
                return {"status": "OK"}
            else:

                return  {"status" :"Invalid  Password"}
        except:
            return {'status':"Invalid Email or Password"}

    return render_template('login.html')

@app.route("/dashboard", methods=["GET","POST"])




def dashboard():
    """endpoint to show all todo items"""
    # print(session['email'],'in session dash oard')
    print(session)
    if request.method =="POST":
        email = session['email']
        text = request.form['text'] 
        category = request.form['category']
        
        user_complain_item = User_Complains(email,text,category)
        db.session.add(user_complain_item)
        db.session.commit()
        return {"email":email,'text':text, 'category':category}
    #     result = User_Details.query.all()
    #     result = user_details_List_schema.dump(result)
    #     return redirect(url_for('dashboard'))
        # return {}
    return render_template('dashboard.html')

@app.route('/dashboard/view',methods=['GET'])
def view_dashboard():
    print("in view dashboard")
    user = User_Complains.query.filter_by(email=session['email']).all()
    user = user_complainsLst_schema.dump(user)
    return jsonify(user)

@app.route('/admin', methods=['GET'])
def admin():

    return render_template('admin_dashboard.html')


@app.route('/admin/view',methods=['GET'])

def get_admin():
    user = User_Complains.query.all()
    user = user_complainsLst_schema.dump(user)
    return jsonify(user)

@app.route("/admin/<id>",methods=["DELETE"])
def delete_todo_item(id):
    if id:
        User_Complains.query.filter(User_Complains.id==id).delete()
        db.session.commit()
        return id
    abort(400)


@app.before_request
def make_session_permanent():
    session.permanent = True
# @app.route("/todo/api/<id>", methods=["GET"])
# def get_todo_item(id):
#     if id:
        
#         data = TodoList.query.get(id)
#         data  =  todo_item_schema.dump(data)
#         return jsonify(data)
#     """endpoint to get todo_item detail by id"""
   
#     return abort(400)

# @app.route("/todo/api/<id>",methods=["DELETE"])
# def delete_todo_item(id):
#     if id:
#         TodoList.query.filter(TodoList.id==id).delete()
#         # db.session.delete(user)
#         db.session.commit()
#         return id
#     abort(400)

# # @app.route("todo/api/<id>",methods=[PUT])
# # def update_todo_item(id):
# #     if id:

