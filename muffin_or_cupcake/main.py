from flask import Flask, request, render_template
from py_muffins_cupcakes import muffin_or_cupcake #predictionfucn name


# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/') #When someone come to my home pack, show the table 
def entry_page():
    return render_template('index.html')

# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/predict_recipe/', methods=['GET', 'POST'])
def render_message():

    # user-entered ingredients (17)
    ingredients = ['loan_amnt','funded_amnt','int_rate','installment','emp_length','annual_inc','dti','delinq_2yrs','inq_last_6mths','open_acc','pub_rec','revol_bal','revol_util','total_acc','tot_coll_amt','tot_cur_bal','total_rev_hi_lim']

    # error messages to ensure correct units of measure
    messages = ["The loan_amnt must be valid.",
                "The funded_amnt must be valid.",
                "The int_rate must be valid.",
                "The installment must be valid.",
                "The emp_length must be valid.",
                "The annual_inc must be valid.",
                "The dti of vanilla must be valid.",
                "The delinq_2yrs of salt must be valid.",
                "The inq_last_6mths of salt must be valid.",
                "The open_acc of salt must be valid.",
                "The pub_rec of salt must be valid.",
                "The revol_bal of salt must be valid.",
                "The revol_util of salt must be valid.",
                "The total_acc of salt must be valid.",
                "The tot_coll_amt of salt must be valid.",
                "The tot_cur_bal of salt must be valid.",
                "The total_rev_hi_lim of salt must be valid."
                ]

    # hold all amounts as floats
    amounts = []

    # names of the dictionary
    letter_grade = {'A':1 , 'B':1 , 'C':1 , 'D':1 , 'E':1 , 'F':1 ,'G':1}
    term_time = {'36':1, '60':1}
    plan = {'No':1,'Yes':1}
    home = {'Any': 1, 'Mortgage': 1, 'None': 1,'Other': 1, 'Own': 1,'Rent': 1}
    purpose = {'Car': 1, 'Credit Card': 1, 'Debt Consolation': 1,'Educational': 1,'Home Improvement': 1, 'House':1, 'Major Purchase': 1,'Medical':1, 'Moving': 1,'Other': 1, 'Renewable Energy': 1,'Small Business': 1,'Vacation': 1, 'Wedding': 1}
    recover = {'No':1,'Yes': 1}
    intial_listing = {'Full':1, 'Partial':1}
    verification_type = {'Not Verified':1 ,'Source Verified':1, 'Verified':1}
    #55

    # takes user input and ensures it can be turned into a floats
    for i, name in enumerate(ingredients):
        print(name) #is the name the variable name
        user_input = request.form[name] #This will get the user's response to the name
        try:
            float_ingredient = float(user_input)
        except: #if someone entered a text, then return one of the error mesg
            return render_template('index.html', message=messages[i])
        amounts.append(float_ingredient)

    grade = request.form['grade']
    term = request.form['term']
    payment_plan = request.form['payment_plan']
    home_ownership = request.form['home_ownership']
    purpose_of_loan = request.form['purpose_of_loan']
    recovery = request.form['recovery']
    listing = request.form['initial_List_Status']
    verification = request.form['verification']
    
    for key in letter_grade:
            if key == grade: #home[key]: #request.form[name] 
                amounts.append(1)
                # print('hello mister')
                # print (amounts)
            else:
                amounts.append(0)
                # print('noooo')
                # print (amounts)
    for key in term_time:
            if key == term: #home[key]: #request.form[name] 
                amounts.append(1)
                # print('hello mister')
                # print (amounts)
            else:
                amounts.append(0)
                # print('noooo')
                # print (amounts) 

    for key in plan:
            if key == payment_plan: #home[key]: #request.form[name] 
                amounts.append(1)
                # print('hello mister')
                # print (amounts)
            else:
                amounts.append(0)
                # print('noooo')
                # print (amounts)  

    for key in home:
            if key == home_ownership: #home[key]: #request.form[name] 
                amounts.append(1)
                # print('hello mister')
                # print (amounts)
            else:
                amounts.append(0)
                # print('noooo')
                # print (amounts)
    
    for key in purpose:
            if key == purpose_of_loan: #home[key]: #request.form[name] 
                amounts.append(1)
                # print('hello mister')
                # print (amounts)
            else:
                amounts.append(0)
                # print('noooo')
                # print (amounts)

    for key in recover:
            if key == recovery: #home[key]: #request.form[name] 
                amounts.append(1)
                # print('hello mister')
                # print (amounts)
            else:
                amounts.append(0)
                # print('noooo')
                # print (amounts)

    for key in intial_listing:
            if key == listing: #home[key]: #request.form[name] 
                amounts.append(1)
                # print('hello mister')
                # print (amounts)
            else:
                amounts.append(0)
                # print('noooo')
                # print (amounts)

    for key in verification_type:
            if key == verification: #home[key]: #request.form[name] 
                amounts.append(1)
                # print('hello mister')
                # print (amounts)
            else:
                amounts.append(0)
                # print('noooo')
                # print (amounts)   
    print (amounts)
    final_message = muffin_or_cupcake(amounts)
    return render_template('index.html', message=final_message)


if __name__ == '__main__':
    app.run(debug=True)


#52

    # for name in ingredients:
    #     print(name) #is the name the name of the
    #     user_input = request.form[name] #This will get the user's response to the name
    #     print('USER INPUT:' + user_input) #print input user
        



    # for i, ing in enumerate(ingredients):
    #     user_input = request.form[ing]
    #     print('HELLO PEEPS' + user_input)
    #     try:
    #         float_ingredient = float(user_input)
    #     except: #if someone entered a text, then return one of the error mesg
    #         return render_template('index.html', message=messages[i])
    #     amounts.append(float_ingredient)

    # show user final message
    #function that you call from the other python file. (muffin_or_cupcake)
    # actually use a



# for i, ing in enumerate(ingredients):
#         user_input = request.form[ing]
#         if (ingredients < 25):
#             try:
#                 float_ingredient = float(user_input)
#             except: #if someone entered a text, then return one of the error mesg
#                 return render_template('index.html', message=messages[i])
#             amounts.append(float_ingredient)
#         if (ingredients == (0 or 1)):
#             if i == 0:
#                 loan_asked = float(user_input)
#             if loan_asked < funded_amnt :
#                 return render_template('index.html', message=messages[i])
#         if 
 
#  #       if (ingredients > 24):
#  #           if 



