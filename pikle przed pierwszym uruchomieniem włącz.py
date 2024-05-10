import pickle
'DO TWORZENIA PILIKÓW DLA KODU PO RESECIE DANYCH'
'WŁĄCZ TO PRZED PIERWSZYM URUCHOMIENIEM A POTEM  NIC TU NIE TYKAC CHYBA ZE CHCESZ COS ROZPIERDOLIC'
######################################################################################################################################################################################
udict = {}
m = 0
with open('diet', 'wb') as file:
    pickle.dump(udict, file)

with open('m', 'wb') as file:
    pickle.dump(m, file)

 # 'GOAL OF USER'
goal_user = {}
with open('goals', 'wb') as file:
     pickle.dump(goal_user, file)
##########################################################################################################################################################################################

# 'PPM'
##########################################################################################################################################################################################
PPM = 0
with open ('PPPM', 'wb') as file:
    pickle.dump(PPM, file)
##########################################################################################################################################################################################


# 'Calorie_save'
##########################################################################################################################################################################################
calorie_save = {'breakfast_calorie': 0, 'lunch_calorie': 0, 'dinner_calorie': 0,'dessert_calorie': 0, 'snacks_calorie':0, 'protein_menu': 0, 'fats_menu': 0, 'carbohydrates_menu': 0}
with open ('what_you_ate', 'wb') as file:
    pickle.dump(calorie_save, file)
###########################################################################################################################################################################################


# 'Calendar'
##########################################################################################################################################################################################
from datetime import date
niumber= 0
with open ('bignumbers', 'wb') as file:
    pickle.dump(niumber, file)
dates = {}
piwo = date.today()
dates['data0'] = piwo
with open ('dates_file', 'wb') as file:
    pickle.dump(dates, file)
dates_and_data = {}
with open ('dates_and_data_file', 'wb') as file:
    pickle.dump(dates_and_data, file)
###########################################################################################################################################################################################

'Meals_Dict'
##########################################################################################################################################################################################
'Meals'
meals = {}
with open ('meaals', 'wb') as file:
    pickle.dump(meals, file)
##########################################################################################################################################################################################

'Calorie_save_calendar'
##########################################################################################################################################################################################
Calendar_savecal ={}
with open ('Calendar_savecal_file', 'wb')as file:
    pickle.dump(Calendar_savecal, file)
##########################################################################################################################################################################################
'USERNAME AND PASSWORD'
username_and_password = {}
with open ('usernames_and_passwords', 'wb') as file:
    pickle.dump(username_and_password, file)
#############################################################################################################################################################################################
'USERNAME PERSONAL DATA'
User_personal_data = {}
with open ('Users_personal_datas_file', 'wb')as file:
    pickle.dump(User_personal_data, file)
user_personal_data2 ={}
with open ('Users_personal_datas_file2', 'wb') as file:
    pickle.dump(user_personal_data2, file)
####################################################################################################################################################
'LOGOWANIE'
recordarme = []
with open('recordarme_file', 'wb') as file:
    pickle.dump(recordarme, file)
dont_log = False
with open('dont_log_file', 'wb') as file:
    pickle.dump(dont_log, file)
