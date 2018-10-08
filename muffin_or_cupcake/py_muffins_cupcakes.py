import pickle
import pandas as pd
import numpy as np

# read in the model
mc_model = pickle.load(open("logRegCredit.p","rb"))

#list of all values the users inputed
# create a function to take in user-entered amounts and apply the model
def muffin_or_cupcake(amounts_float, model=mc_model):
    
    # # put everything in terms of tablespoons
    # # flour, milk, sugar, butter, eggs, baking powder, vanilla, salt
    # multipliers = [16, 16, 16, 16, 3, .33, .33, .33]
    
    # # sum up the total values to get the total number of tablespoons in the batter
    # total = np.dot(multipliers, amounts_float)

    # # note the proportion of flour and sugar
    # flour_cups_prop = multipliers[0] * amounts_float[0] * 100.0 / total
    # sugar_cups_prop = multipliers[2] * amounts_float[2] * 100.0 / total

    # # inputs into the model
    # input_df = [[flour_cups_prop, sugar_cups_prop]]
    
    input_df = [amounts_float] #Assumes everything is clean, or go through amountfloats[0], amountfloats[3]...
    print (input_df)
    # make a prediction
    prediction = mc_model.predict(input_df)[0] #array[0] then number

    # return a message
    message_array = ["You have a bad loan!",
                     "You have a good loan!"]

    return message_array[prediction]
