import pickle
# DO SPRAWDZANIA CO JEST W PICKLE
with open('m', 'rb') as file:
    m = pickle.load(file)


with open('diet', 'rb') as file:
    udict = pickle.load(file)
with open('goals', 'rb') as file:
        goal_user = pickle.load(file)
with open('PPPM', 'rb') as file:
    PPM = pickle.load(file)
with open('meaals', 'rb') as file:
    meals = pickle.load(file)
with open('what_you_ate', 'rb') as file:
    calorie_save = pickle.load(file)
with open('bignumbers', 'rb') as file:
    niumber = pickle.load(file)
with open('dates_file', 'rb') as file:
    dates = pickle.load(file)
with open('dates_and_data_file', 'rb') as file:
        dates_and_data = pickle.load(file)
with open('usernames_and_passwords', 'rb') as file:
    username_and_password = pickle.load(file)
with open('Calendar_savecal_file', 'rb') as file:
    Calendar_savecal = pickle.load(file)
with open('Users_personal_datas_file', 'rb') as file:
    User_personal_data = pickle.load(file)
with open('Users_personal_datas_file2', 'rb') as file:
        user_personal_data2 = pickle.load(file)

print('user_def' + str(m))
print('calendar_def' + str(niumber))
print(udict.keys())
print('Number of users: ' + (str(len(udict))))
print(goal_user)
print(PPM)
print('List of meals in registered')
print(meals.keys())

print(calorie_save)

print(dates)

print(username_and_password)

print(Calendar_savecal)

print(User_personal_data)

print(user_personal_data2)



