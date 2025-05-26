import pickle
from lk import *
from datetime import datetime
from time import sleep, time
# Im commenting this one year after making this and yes its tragic
# I wont comment it as a whole cause its pointless its a mess i used more global var in this code than i will use for  the rest of my life probably 
# I was new in python so you have to understand. Theoriticly is shoudnt make it public but its sentimental for me so just dont judge me on this one code please.
# Still code works and its pretty comfy to use
# We can choose between adding foods we ate or checking our goal for current day or even history of out diet.
# One thing that is most cool is how program saves properties of meals if they are being mentioned for frist time if we add properties of apple one time next time...
# code will remeber it and skip the procces of filling properies i could try including so outisde food data but well it was frsit project after all.
# Data manegment is pretty tuff though kinda suprised i did it back then with this whole pickle dicts stuff.
global backer
global nie_ma_to_kurwa_sensu
def calorie_shedule(uzer):
    # mostly unnecessary globals
    global backer
    global uchoice
    global Calorie_savedhelp
    global trycpf
    global cal_calculator
    global dates
    global csc
    global cal_calculator2
    global trry
    global trry2
    global shedule
    global ate
    global meals
    global breakfast_calorie
    global lunch_calorie
    global dinner_calorie
    global dessert_calorie
    global snacks_calorie
    global protein_menu
    global fats_menu
    global carbohydrates_menu
    global fake_gcalorie
    global fake_gcarbohydrates
    global fake_fatsmenu
    global fake_proteinmenu
    global fake_gcarbohydratesmenu
    global fake_gfats
    global fake_gprotein
    global fakebreakfast_calorie
    global current_gcalorie
    global current_gprotein
    global current_gfats
    global stoch
    global current_gcarbohydrates
    global nutreins
    global calorie_save
    global time
    global calorie_save
    global breakfun
    global calendar
    global calendar2
    
    # Setting up datetime and other data
    
    calendar2 = datetime.today()
    calendar = calendar2.strftime('%Y-%m-%d')
    breakfun = 0
    calorie_save = {'breakfast_calorie': 0, 'lunch_calorie': 0, 'dinner_calorie': 0, 'dessert_calorie': 0,'snacks_calorie':0,
                    'protein_menu': 0, 'fats_menu': 0, 'carbohydrates_menu': 0}
    # Loading saved data of user
    with open('what_you_ate', 'rb') as file:
        calorie_save = pickle.load(file)
    with open('Users_personal_datas_file', 'rb') as file:
        User_personal_data = pickle.load(file)
        
    nutreins = {'gfats':None, 'gprotein':None, 'gcarbohydrates':None, 'gcalorie':None}
    meals = {}
    with open('goals', 'rb') as file:
     goal_user = pickle.load(file)
    with open('diet', 'rb') as file:
      udict = pickle.load(file)


    # defying functions 

    
    def trry():
     try:
        pol = True
        while True:
            print(f'How many grams of {ate} did you ate?')
            amount = float(input()) / 100
            break
     except ValueError:
        print('Please insert number')
        trry2()
    def trry2():
        try:
            pol = True
            while True:
                global amount
                amount = float(input()) / 100
                break
        except ValueError:
            print('Please insert number')
            trry2()
    def trycpf(nu):
        try:
         lop = True
         while True:
            nutreins[(nu)] = float(input())
            break
        except ValueError:
            print('Please insert number')
            trycpf(nu)
    def cal_calculator2():
        nutreins[('gcalorie')] = float(meals[ate].mcalorie) * amount
        nutreins[('gprotein')] = float(meals[ate].mprotein) * amount
        nutreins[('gfats')] = float(meals[ate].mfats) * amount
        nutreins[('gcarbohydrates')] = float(meals[ate].mcarbohydrates) * amount
        global fake_gcalorie
        global fake_gcarbohydrates
        global fake_fatsmenu
        global fake_proteinmenu
        global fake_gcarbohydratesmenu
        global fake_gfats
        global fake_gprotein
        global fakebreakfast_calorie
        fake_gcalorie = current_gcalorie
        fake_gprotein = current_gprotein
        fake_gfats = current_gfats
        fake_proteinmenu = protein_menu
        fake_fatsmenu = protein_menu
        fakebreakfast_calorie = breakfast_calorie
        fake_gcarbohydrates = current_gcarbohydrates
        fake_gcarbohydratesmenu = carbohydrates_menu
        fakebreakfast_calorie = int(breakfast_calorie) + int(nutreins[('gcalorie')])
        fake_gcalorie = int(fake_gcalorie) - int(nutreins[('gcalorie')])
        fake_gprotein = int(fake_gprotein) - int(nutreins[('gprotein')])
        fake_proteinmenu = int(fake_proteinmenu) + int(nutreins[('gprotein')])
        fake_gfats = int(fake_gfats) - int(nutreins[('gfats')])
        fake_fatsmenu = int(fake_fatsmenu) + int(nutreins[('gfats')])
        fake_gcarbohydrates = int(fake_gcarbohydrates) - int(nutreins[('gcarbohydrates')])
        fake_gcarbohydratesmenu = int(fake_gcarbohydratesmenu) + int(nutreins[('gcarbohydrates')])
    def cal_calculator():
     global meals
     try:
         pol = True
         while pol == True:
          print(f'How many grams of {ate} did you ate?')
          print('Go back')
          global gołbak
          global amount
          gołbak = input()
          if gołbak.lower() == 'go back':
              return
          amount = int(gołbak)
          amount = amount/100
          if amount == str:
              print('Please insert number')
              trry2()
          break

     except ValueError:
       print('Please insert number')
       trry2()
     nutreins[('gcalorie')] = float(meals[ate].mcalorie) * amount
     nutreins[('gprotein')] = float(meals[ate].mprotein) * amount
     nutreins[('gfats')] = float(meals[ate].mfats) * amount
     nutreins[('gcarbohydrates')] = float(meals[ate].mcarbohydrates) * amount
     global fake_gcalorie
     global fake_gcarbohydrates
     global fake_fatsmenu
     global fake_proteinmenu
     global fake_gcarbohydratesmenu
     global fake_gfats
     global fake_gprotein
     global fakebreakfast_calorie
     fake_gcalorie = current_gcalorie
     fake_gprotein = current_gprotein
     fake_gfats = current_gfats
     fake_gcarbohydrates = current_gcarbohydrates
     fake_proteinmenu = protein_menu
     fake_fatsmenu = fats_menu
     fakebreakfast_calorie = breakfast_calorie
     fake_gcarbohydratesmenu = carbohydrates_menu
     fakebreakfast_calorie = int(breakfast_calorie) + int(nutreins[('gcalorie')])
     fake_gcalorie = int(fake_gcalorie) - int(nutreins[('gcalorie')])
     fake_gprotein = int(fake_gprotein) - int(nutreins[('gprotein')])
     fake_proteinmenu = int(fake_proteinmenu) + int(nutreins[('gprotein')])
     fake_gfats = int( fake_gfats) - int(nutreins[('gfats')])
     fake_fatsmenu = int(fake_fatsmenu) + int(nutreins[('gfats')])
     fake_gcarbohydrates = int(fake_gcarbohydrates) - int(nutreins[('gcarbohydrates')])
     fake_gcarbohydratesmenu = int(fake_gcarbohydratesmenu) + int(nutreins[('gcarbohydrates')])

    def shedule():

        print(f'         {uzer} calorie counter menu                   ')
        print(f'Breakfast   {breakfast_calorie}  calorie                       proteins  {protein_menu}  grams')
        print(f'Lunch       {lunch_calorie}  calorie                           fats  {fats_menu}  grams')
        print(f'Dinner      {dinner_calorie}  calorie                 carbohydrates   {carbohydrates_menu}  grams')
        print(f'Dessert     {dessert_calorie}  calorie')
        print(f'Snacks      {snacks_calorie}  calorie')
        print(f'calories left:      {current_gcalorie}  grams ')
        print(f'protein left:       {current_gprotein}  grams ')
        print(f'fats left:          {current_gfats}  grams ')
        print(f'carbohydrates left: {current_gcarbohydrates}  grams ')
        print(                                                                        'Show my history'                          )


    with open('dates_file', 'rb') as file:
        dates = pickle.load(file)
    current_date = calendar
    with open('bignumbers', 'rb') as file:
        niumber = pickle.load(file)
    if current_date != dates['data' + str(niumber)]:
        calorie_save = {'breakfast_calorie': 0, 'lunch_calorie': 0, 'dinner_calorie': 0, 'dessert_calorie': 0,
                        'snacks_calorie': 0, 'protein_menu': 0, 'fats_menu': 0, 'carbohydrates_menu': 0}
        with open('what_you_ate', 'wb') as file:
            pickle.dump(calorie_save, file)
        with open('what_you_ate', 'rb') as file:
            calorie_save = pickle.load(file)

        niumber = niumber + 1
        dates['data' + str(niumber)] = current_date
        with open('bignumbers', 'wb') as file:
            pickle.dump(niumber, file)
        dates['data' + str(niumber)] = current_date
        with open('dates_file', 'wb') as file:
           pickle.dump(dates, file)
    with open('Users_personal_datas_file', 'wb') as file:
        pickle.dump(User_personal_data, file)
    if not  uzer + str(calendar) + 'breakfast_calorie' in User_personal_data.keys():
        User_personal_data[uzer + str(calendar) + 'breakfast_calorie'] = 0
        User_personal_data[uzer + str(calendar) + 'lunch_calorie'] = 0
        User_personal_data[uzer + str(calendar) + 'dinner_calorie'] = 0
        User_personal_data[uzer + str(calendar) + 'dessert_calorie'] = 0
        User_personal_data[uzer + str(calendar) + 'snacks_calorie'] = 0
        User_personal_data[uzer + str(calendar) + 'protein_menu'] = 0
        User_personal_data[uzer + str(calendar) + 'fats_menu'] = 0
        User_personal_data[uzer + str(calendar) + 'carbohydrates_menu'] = 0




    with open('Users_personal_datas_file', 'wb') as file:
        pickle.dump(User_personal_data, file)



    breakfast_calorie = User_personal_data[uzer + str(calendar) + 'breakfast_calorie']
    lunch_calorie = User_personal_data[uzer + str(calendar) + 'lunch_calorie']
    dinner_calorie = User_personal_data[uzer + str(calendar) + 'dinner_calorie']
    dessert_calorie = User_personal_data[uzer + str(calendar) + 'dessert_calorie']
    snacks_calorie = User_personal_data[uzer + str(calendar) + 'snacks_calorie']
    protein_menu = User_personal_data[uzer + str(calendar) + 'protein_menu']
    fats_menu = User_personal_data[uzer + str(calendar) + 'fats_menu']
    carbohydrates_menu = User_personal_data[uzer + str(calendar) + 'carbohydrates_menu']
    current_gcalorie = goal_user[uzer].gcalorie
    current_gprotein = (goal_user[uzer].gprotein)
    current_gfats =  (goal_user[uzer].gfats)
    current_gcarbohydrates = (goal_user[uzer].gcarbohydrates)
    tak = True
    while tak == True:
     shedule()
     global uchoice
     print('                                  quit/logout\n')
     print('Insert for example dinner, or another of the commends from below the calorie counter, like "quit" or "show my history"(shorcut show)')
     uchoice= input().lower()
     if  uchoice == 'quit':
         quit()
     if uchoice.lower() == 'show' or uchoice == 'show my history':
         def try_time():
              print('incorrect input')
              print('Please insert the date(month/day/year)')
              try:

                 dejt = input()
                 format = '%d/%m/%Y'
                 date_to_read = calendar2.strptime(dejt, '%d/%m/%Y')
                 date_to_read = date_to_read.strftime('%d/%m/%Y')
              except ValueError:
                 try_time()

         print('Please insert the date(day/month/year)')
         try:
             dejt = input()
             format = '%d/%m/%Y'
             date_to_read = calendar2.strptime(dejt, '%d/%m/%Y')
             date_to_read = date_to_read.strftime('%d/%m/%Y')
         except ValueError:
             try_time()
         with open('Users_personal_datas_file2', 'rb') as file:
                 user_personal_data2 = pickle.load(file)
         try:
          calorie_save_to_read = user_personal_data2[uzer + str(date_to_read)]
          breakfast_calorie = calorie_save_to_read['breakfast_calorie']
          lunch_calorie = calorie_save_to_read['lunch_calorie']
          dinner_calorie = calorie_save_to_read['dinner_calorie']
          dessert_calorie = calorie_save_to_read['dessert_calorie']
          snacks_calorie = calorie_save_to_read['snacks_calorie']
          protein_menu = calorie_save_to_read['protein_menu']
          fats_menu = calorie_save_to_read['fats_menu']
          carbohydrates_menu = calorie_save_to_read['carbohydrates_menu']
          print(f'         {uzer} calorie counter menu  {date_to_read}                 ')
          print(f'Breakfast   {breakfast_calorie}  calorie                       proteins  {protein_menu}  grams')
          print(f'Lunch       {lunch_calorie}  calorie                           fats  {fats_menu}  grams')
          print(f'Dinner      {dinner_calorie}  calorie                 carbohydrates   {carbohydrates_menu}  grams')
          print(f'Dessert     {dessert_calorie}  calorie')
          print(f'Snacks      {snacks_calorie}  calorie\n\n\n\n\n')
          sleep(10)
         except KeyError:
             print(f'         {uzer} calorie counter menu  {date_to_read}                 ')
             print(f'Breakfast   0  calorie                       proteins  0  grams')
             print(f'Lunch       0  calorie                           fats  0  grams')
             print(f'Dinner      0  calorie                 carbohydrates   0  grams')
             print(f'Dessert     0  calorie')
             print(f'Snacks      0  calorie\n\n\n\n\n')
             sleep(10)
     if uchoice.lower() == 'log out' or uchoice == 'logout':
         return


         # 07/05/2024

     if uchoice == 'breakfast':
         eating('breakfast', uzer)
     if uchoice == 'lunch':
         eating('lunch', uzer)
     if uchoice == 'dinner':
         eating('dinner', uzer)
     if uchoice == 'dessert':
         eating('dessert', uzer)
     if uchoice == 'snacks':
         eating('snacks', uzer)


def eating(time, udzer2):
    global Calorie_savedhelp
    Calorie_savedhelp = time
    global uchoice
    global trycpf
    global cal_calculator
    global cal_calculator2
    global csc
    global trry
    global trry2
    global shedule
    global ate
    global calorie_save
    global meals
    global breakfast_calorie
    global dates
    global lunch_calorie
    global dinner_calorie
    global dessert_calorie
    global snacks_calorie
    global protein_menu
    global calendar
    global fats_menu
    global carbohydrates_menu
    global fake_gcalorie
    global gołbak
    global fake_gcarbohydrates
    global fake_fatsmenu
    global fake_proteinmenu
    global fake_gcarbohydratesmenu
    global fake_gcarbohydrates
    global fake_gfats
    global fake_gprotein
    global fakebreakfast_calorie
    global current_gcalorie
    global current_gprotein
    global current_gfats
    global current_gcarbohydrates
    global nutreins
    global calorie_save_func

    def calorie_save_func():
        global breakfun
        breakfun = 0
        global breakfast_calorie
        global lunch_calorie
        global dinner_calorie
        global dessert_calorie
        global snacks_calorie
        global protein_menu
        global fats_menu
        global carbohydrates_menu
        global current_gcalorie
        global current_gprotein
        global current_gfats
        global fake_gcarbohydratesmenu
        global fake_gfats
        global fake_gprotein
        global fake_gcarbohydrates
        global current_gcarbohydrates
        global csc
        global dates
        with open('what_you_ate', 'rb') as file:
            calorie_save = pickle.load(file)

        current_gcalorie = fake_gcalorie
        current_gprotein = fake_gprotein
        current_gfats = fake_gfats
        current_gcarbohydrates = fake_gcarbohydrates
        protein_menu = fake_proteinmenu
        fats_menu = fake_fatsmenu
        carbohydrates_menu = fake_gcarbohydratesmenu
        if time == 'breakfast':
            breakfast_calorie = fakebreakfast_calorie
            calorie_save['breakfast_calorie'] = breakfast_calorie
        if time == 'lunch':
            lunch_calorie = fakebreakfast_calorie + lunch_calorie
            calorie_save['lunch_calorie'] = lunch_calorie
        if time == 'dinner':
            dinner_calorie = fakebreakfast_calorie + dinner_calorie
            calorie_save['dinner_calorie'] = dinner_calorie
        if time == 'dessert':
            dessert_calorie = fakebreakfast_calorie + dessert_calorie
            calorie_save['dessert_calorie'] =  dessert_calorie
        if time == 'snacks':
            snacks_calorie = fakebreakfast_calorie + snacks_calorie
            calorie_save['snacks_calorie'] = snacks_calorie
        calorie_save['protein_menu'] = protein_menu
        calorie_save['fats_menu'] = fats_menu
        calorie_save['carbohydrates_menu'] = carbohydrates_menu

        with open('what_you_ate', 'wb') as file:
           pickle.dump(calorie_save, file)
        with open('what_you_ate', 'rb') as file:
           calorie_save = pickle.load(file)
        with open('Calendar_savecal_file', 'rb') as file:
               Calendar_savecal = pickle.load(file)
        with open('Users_personal_datas_file', 'rb') as file:
            User_personal_data = pickle.load(file)
        Calendar_savecal[calendar] = calorie_save
        # [Calendar_savecal[calendar]]
        User_personal_data[udzer2 + str(calendar) + 'breakfast_calorie']  = calorie_save['breakfast_calorie']
        User_personal_data[udzer2 + str(calendar) + 'lunch_calorie'] = calorie_save['lunch_calorie']
        User_personal_data[udzer2 + str(calendar) + 'dinner_calorie'] = calorie_save['dinner_calorie']
        User_personal_data[udzer2 + str(calendar) + 'dessert_calorie'] = calorie_save['dessert_calorie']
        User_personal_data[udzer2 + str(calendar) + 'snacks_calorie'] = calorie_save['snacks_calorie']
        User_personal_data[udzer2 + str(calendar) + 'protein_menu'] = calorie_save['protein_menu']
        User_personal_data[udzer2 + str(calendar) + 'fats_menu'] = calorie_save['fats_menu']
        User_personal_data[udzer2 + str(calendar) + 'carbohydrates_menu'] = calorie_save['carbohydrates_menu']
        with open('Users_personal_datas_file', 'wb') as file:
            pickle.dump(User_personal_data, file)
        with open('Users_personal_datas_file2', 'rb') as file:
            user_personal_data2 = pickle.load(file)
        now_date = calendar2.strftime('%d/%m/%Y')
        calorie_save_well = {}
        calorie_save_well['right_now'] = calorie_save
        calorie_save_well2 = {}
        calorie_save_well2[now_date] = calorie_save_well['right_now']
        user_personal_data2[udzer2 + str(now_date)] =  calorie_save_well2[now_date]
        with open('Users_personal_datas_file2', 'wb') as file:
            pickle.dump(user_personal_data2, file)





        shedule()
        prop = None
        mist = None
        ate = None
        iks = False
        gate = False
        mop = False
        gate1 = False


    while uchoice == time:
        global breakfun
        with open('meaals', 'rb') as file:
            meals = pickle.load(file)
        gate1 = True

        print(f'What did you ate for {time} today?')
        print('go back')
        print('Quit')
        if breakfun == 1:
            ate = None
        breakfun = 0
        ate = None
        ate = input()
        if ate.lower() == 'quit':
            quit()


        if ate in meals.keys():
            gate1 = False
        typee22 = None
        mist = None
        prop = None
        gate = True
        if ate == 'go back' or ate == 'gb':
            break
        if ate in meals.keys():
            if mist == 'go back' or mist == 'Go back':
                mist = None
                break
            if prop == 'go back' or prop == 'Go back':
                prop = None
                break
            if typee22 == 'go back' or typee22 == 'Go back':
                typee22 = None
                break
            cal_calculator()
            if  gołbak == 'go back':
                return
            calorie_save_func()

        while gate1 == True:
               if breakfun == 1:
                break
               print('Sadly we dont have this meal on our list.')
               print(' Please insert values of your meal so we can save it for next time (:')
               meals[ate] = ate
               print('Will it be easier for you to give properties for 100g or for the portion you ate?')
               print('100 grams')
               print('Portion i ate')
               print('go back')
               typee = input()
               mop = True
               if typee == 'go back' or typee == 'Go back' or typee == 'goback' or typee == 'Goback' or typee == 'gb':
                   typee22 = None
                   break
               while mop == True:
                if breakfun == 1:
                       break
                if typee == 'Portion i ate' or typee == 'portion i ate' or typee == 'portion' or typee == 'p':
                   if typee22 == 'go back' or typee22 == 'Go back':
                        typee22 = None
                        break
                   print('how many grams did you eat?')
                   trry2()
                   print('Amount of fats')
                   trycpf('gfats')
                   print('Amount of protein')
                   trycpf('gprotein')
                   print('Amount of carbohydrates ')
                   trycpf('gcarbohydrates')
                   print('grams: ' + str(amount * 100))
                   print('fats: ' + str(nutreins['gfats']))
                   print('protein: ' + str(nutreins['gprotein']))
                   print('carbohydrates: ' + str(nutreins['gcarbohydrates']))
                   gate = True
                   while gate == True:
                     if breakfun == 1:
                         break
                     print('Correct mistake')
                     print('Go on')
                     print('Go back')
                     mist = None
                     typee22 = input()
                     prop = typee22
                     if typee22 == 'go back' or  typee22 == 'Go back' or  typee22 == 'gb':
                        break
                     while prop == 'correct mistake' or prop == 'Correct mistake' or prop == 'cm':
                      if breakfun == 1:
                             break
                      print('What do you wont to correct?')
                      print('Go on')
                      print('go back')
                      again = 'xd'
                      typee22 = input()
                      mist =  typee22
                      if  typee22 == 'go back' or  typee22 == 'Go back' or  typee22 == 'gb':
                        typee22 = None
                        break
                      iks = True
                      while iks == True:
                       if breakfun == 1:
                              break
                       if mist == ('amount') or mist == ('Amount') or mist == ('am') or mist ==('grams') or mist ==('gram'):
                              print('insert correct value')
                              trry2()
                              again = 'xd'
                              mist = again


                       if mist == ('fats') or mist == ('fat') or mist == 'f':
                               print('insert correct value')
                               trycpf('gfats')
                               again = 'xd'
                               mist = again
                       if mist == ('proteins') or mist == ('protein') or mist == 'p':
                               print('insert correct value')
                               trycpf('gprotein')
                               again = 'xd'
                               mist = again
                       if mist == ('carbohydrates') or mist == ('carbohydrate') or mist == 'c':
                               print('insert correct value')
                               trycpf('gcarbohydrates')
                               again = 'xd'
                               mist = again
                       if mist == 'Go back' or mist == 'go back' or mist == 'gb':
                               iks = False
                       if again == mist:
                               print('Go on or you wont correct something else?(fats, carbohydrates, proteins, amount(grams))')
                               print('Go on')
                               print('Go back')
                               typee22 = input()
                               mist = typee22
                               if typee22 == 'Go back' or typee22 == 'go back' or typee22 == 'gb':
                                   typee22 = None
                                   break
                               typee22 = None
                       if mist != ('fats') and mist != ('fat') and mist != ('proteins') and mist != ('protein') and mist != ('carbohydrates') and mist != ('carbohydrate') and mist != 'Go back' and mist != 'go back' and mist != 'Go on' and mist != 'go on' and mist != 'Goon' and mist != 'goon' and mist != 'gb' and mist != 'c'  and mist != ('am')  and mist != 'f'  and mist != 'p':
                         print('Incorrect coment')
                         typee22 = input()
                         mist = typee22
                         if typee22 == 'go back' or typee22 == 'Go back':
                             typee22 = None
                             break
                       if mist == 'go on' or mist == ' Go on' or mist == 'Goon' or mist == 'goon':
                        nutreins[('gfats')] = float(nutreins['gfats']) / amount
                        nutreins[('gprotein')] = float(nutreins["gprotein"]) / amount
                        nutreins[('gcarbohydrates')] = float(nutreins[('gcarbohydrates')]) / amount
                        nutreins[('gcalorie')] = float(nutreins['gfats'] * 9) + float(
                            nutreins['gprotein'] * 4) + float(nutreins['gcarbohydrates'] * 4)
                        meals[ate] = rmeals(mcalorie=nutreins[('gcalorie')], mprotein=nutreins[('gprotein')],
                                            mfats=nutreins[('gfats')],
                                            mcarbohydrates=nutreins[('gcarbohydrates')])
                        with open('meaals', 'wb') as file:
                            pickle.dump(meals, file)
                        print('Meal successfuly saved! Thank you!')
                        cal_calculator2()
                        calorie_save_func()
                        breakfun = 1
                        break


                     if prop == 'go on' or prop == 'Go on':
                       nutreins[('gfats')] = float(nutreins[('gfats')]) / amount
                       nutreins[('gprotein')] = float(nutreins[("gprotein")]) / amount
                       nutreins[('gcarbohydrates')] = float(nutreins[('gcarbohydrates')]) / amount
                       nutreins[('gcalorie')] = float(nutreins[('gfats')] * 9) + float(
                           nutreins[('gprotein')] * 4) + float(nutreins[('gcarbohydrates')] * 4)
                       meals[ate] = rmeals(mcalorie=nutreins[('gcalorie')], mprotein=nutreins[('gprotein')],
                                           mfats=nutreins[('gfats')],
                                           mcarbohydrates=nutreins[('gcarbohydrates')])
                       with open('meaals', 'wb') as file:
                           pickle.dump(meals, file)
                       print('Meal successfuly saved! Thank you!')

                       cal_calculator2()
                       calorie_save_func()
                       breakfun = 1
                       break

                if typee == '100 grams':
                   if typee22 == 'go back' or typee22 == 'Go back':
                       typee = None
                       break
                   print('Amount of fats')
                   trycpf('gfats')
                   print('Amount of protein')
                   trycpf('gprotein')
                   print('Amount of carbohydrates ')
                   trycpf('gcarbohydrates')
                   print('fats' + str(nutreins[('gfats')]))
                   print('protein' + str(nutreins[('gprotein')]))
                   print('carbohydrates' + str(nutreins[('gcarbohydrates')]))
                   gate = True
                   while gate == True:
                       if breakfun == 1:
                           break
                       print('Correct mistake')
                       print('Go on')
                       print('Go back')
                       typee22 = input()
                       if typee22 == 'go back' or typee22 == 'Go back' or typee22 == 'goback' or typee22 == 'Goback':
                           break
                       prop = typee22
                       while prop == 'correct mistake' or prop == 'Correct mistake' or prop == 'cm':
                           if breakfun == 1:
                               break

                           print('What do you wont to correct?')
                           print('Go back')
                           mist = input()
                           iks = True
                           again = 'xd'
                           if mist == 'go back' or mist == 'Go back':
                               break
                           while iks == True:
                               if breakfun == 1:
                                   break
                               if mist == ('fats') or mist == ('fat') or mist == 'f':
                                   print('insert correct value')
                                   trycpf('gfats')
                                   again = 'xd'
                                   mist = again
                               if mist == ('proteins') or mist == ('protein') or mist == 'p':
                                   print('insert correct value')
                                   trycpf('gprotein')
                                   again = 'xd'
                                   mist = again
                               if mist == ('carbohydrates') or mist == ('carbohydrate') or mist == 'c':
                                   print('insert correct value')
                                   trycpf('gcarbohydrates')
                                   again = 'xd'
                                   mist = again
                               if mist == 'Go back' or mist == 'go back':
                                   prop = 'go on'
                               if again == mist:
                                   print('Do you wont correct something else? (fats, carbohydrates, proteins)')
                                   print('Go on')
                                   print('Go back')
                                   mist = input()
                                   if mist == 'go back' or mist == 'Go back':
                                       break


                               if mist != ('fats') and mist != ('fat') and mist != ('proteins') and mist != ('protein') and mist != ('carbohydrates') and mist != ('carbohydrate') and mist != 'Go back' and mist != 'go back' and mist != 'Go on' and mist != 'go on' and mist != 'Goon' and mist != 'goon':
                                print('Incorrect coment')
                                mist = input()
                                if mist == 'go back' or mist == 'Go back':
                                    break
                               if mist == 'Go on' or mist == 'go on' or mist == 'Goon' or mist == 'goon':
                                   print('Meal successfuly saved! Thank you!')
                                   nutreins[('gcalorie')] = float(nutreins[('gfats')] * 9) + float(
                                   nutreins[('gprotein')] * 4) + float(nutreins[('gcarbohydrates')] * 4)
                                   meals[ate] = rmeals(mcalorie=nutreins[('gcalorie')], mprotein=nutreins[('gprotein')],
                                               mfats=nutreins[('gfats')], mcarbohydrates=nutreins[('gcarbohydrates')])
                                   with open('meaals', 'wb') as file:
                                     pickle.dump(meals, file)
                                   cal_calculator()
                                   calorie_save_func()
                                   breakfun = 1
                                   break

                       if typee22 == 'go on' or typee22 == 'Go on' or typee22 == 'Goon' or typee22 =='goon':
                           print('Meal successfuly saved! Thank you!')
                           nutreins[('gcalorie')] = float(nutreins[('gfats')] * 9) + float(
                               nutreins[('gprotein')] * 4) + float(nutreins[('gcarbohydrates')] * 4)
                           meals[ate] = rmeals(mcalorie=nutreins[('gcalorie')], mprotein=nutreins[('gprotein')],
                                               mfats=nutreins[('gfats')], mcarbohydrates=nutreins[('gcarbohydrates')])
                           with open('meaals', 'wb') as file:
                               pickle.dump(meals, file)
                           cal_calculator()
                           calorie_save_func()
                           breakfun = 1
                           break


                       if typee22 != 'Go on' and typee22 != 'go on' and typee22 != 'Goon' and typee22 != 'goon' and  typee22 != 'correct mistake' and typee22 != 'Correct mistake' and typee22 != 'go back' and typee22 != 'Go back' and typee22 != 'Goback' and typee22 !='goback' and typee22 !='p' and typee22 !='c' and typee22 !='f':
                           print('Incorrect comend')
                           typee22 = input()
                if typee != '100 grams' and typee != 'portion' and typee != 'portion i ate' and typee != 'go on' and typee != 'Goon' and typee != 'goon'  and typee != 'Go on' and typee != 'go back' and typee!= 'Go back' and typee!= 'Goback' and typee!='goback' and typee!= 'p' and typee!= 'c' and typee!='f':
                   print('Incorrect comend')
                   typee = input()
