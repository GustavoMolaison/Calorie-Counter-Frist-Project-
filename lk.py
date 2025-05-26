import pickle
global nus
global nus
# This code is responsible for setting profile for new users
# From their calorie to protein goal based on info they provide


class Ugoal:
 def __init__(self, calorieconsumption, goal, gcalorie, gprotein, gfats, gcarbohydrates):
          self.calorieconsumption =  int(calorieconsumption)
          self.goal =  goal
          self.gcalorie = int(gcalorie)
          self.gprotein = int(gprotein)
          self.gfats = int(gfats)
          self.gcarbohydrates = int(gcarbohydrates)


 def Goal_information(self):
         print('your calorie consumption is ' + str(self.calorieconsumption))
         print('Your calorie goal to ' + str(self.goal) + ' weight is ' + str(self.gcalorie))
         print('macroelements list')
         print('protein: ' + str(self.gprotein) + ' grams')
         print('fats: ' + str(self.gfats) + ' grams')
         print('carbohydrates: ' + str(self.gcarbohydrates) + ' grams')




class User:
    def __init__(self, name, weight, height, BMI, gender, age, activity):
     self.weight_of_user = weight
     self.height_of_user = height
     self.BMI_of_user = BMI
     self.gender = gender
     self.age = age
     self.activity = activity

    def Body_information(self):
      print ('your weight is ' + str(self.weight_of_user))
      print ('your height is ' + str(self.height_of_user))
      print ('your BMI is ' + str(self.BMI_of_user))



class rmeals:
    def __init__(self, mcalorie, mprotein, mfats, mcarbohydrates  ):
        self.mcalorie = mcalorie
        self.mprotein = mprotein
        self.mfats = mfats
        self.mcarbohydrates = mcarbohydrates

    def meal_prop(self):
        print(self)
        print('calories', str(self.mcalorie))
        print('proteins', str(self.mprotein))
        print('fats', str(self.mfats))
        print('carbohydrates', str(self.mcarbohydrates))

def errorhandle(thetype, thestring):
    global thevalue
    try:
        thevalue = thetype(input(f'Please insert your {thestring}'))
    except ValueError:
        errorhandle(thetype, thestring)

def new_user(nus):
  print('Welcome to the calorie counting program')
  print('From what we can see you are new up there huh?')
  print('We hope you dont mind few questions!')
  global udict
  with open('../../.venv/diet', 'rb') as file:
      udict = pickle.load(file)
  udict[nus] = nus
  gendergiv = input('are you female or male?')
  while gendergiv != 'male' and gendergiv != 'female':
      print('Please chosse one of the two genders available')
      gendergiv = input('are you female or male?')
  errorhandle( float, 'weight' )
  weightgiv = thevalue
  errorhandle( float, 'height(in meters)')
  heightgiv = thevalue
  errorhandle( int, 'age')
  agegiv = thevalue
  activgiv = (input('What is your level of sport activity? (none, small(1 - 3 trainings a week), medium( 3 - 4 trainings), high( 6 - 7), very high( hard workout everyday)'))
  while activgiv != 'none' and activgiv != 'small' and activgiv != 'medium' and activgiv != 'high' and activgiv != 'very high':
       print('please choose one from the given options')
       activgiv = (input( 'What is your level of sport activity? (none, small(1 - 3 trainings a week), medium( 3 - 4 trainings), high( 6 - 7)'))
  BMIgiv = int(weightgiv / (heightgiv * heightgiv))
  udict[nus] = User(name = nus, weight = weightgiv, height = heightgiv, BMI = BMIgiv, gender = gendergiv, age = agegiv, activity = activgiv)
  with open('diet', 'wb') as file:
      pickle.dump(udict, file)




def Calorie_consumption(nus):
     if udict[nus].gender == 'male':
         PPM = 66.473 + (13.752 * udict[nus].weight_of_user) + (5.003 * (udict[nus].height_of_user * 100)) - (6.775 * udict[nus].age)
         if udict[nus].activity == 'none':
             CPM = PPM * 1.2
         if udict[nus].activity == 'small':
             CPM = PPM * 1.4
         if udict[nus].activity == 'medium':
             CPM = PPM * 1.6
         if udict[nus].activity == 'high':
             CPM = PPM * 1.8
         if udict[nus].activity == 'very high':
             CPM = PPM * 2.1
         print( 'your base calorie consumption is')
         print(int(CPM))
     if udict[nus].gender == 'female':
         PPM = 655.1 + (9.563 * udict[nus].weight_of_user) + (1.85 * (udict[nus].height_of_user * 100)) - (4.676 * udict[
             nus].age)
         if udict[nus].activity == 'none':
             CPM = PPM * 1.2
         if udict[nus].activity == 'small':
             CPM = PPM * 1.4
         if udict[nus].activity == 'medium':
             CPM = PPM * 1.6
         if udict[nus].activity == 'high':
             CPM = PPM * 1.8
         if udict[nus].activity == 'very high':
             CPM = PPM * 2.1
         print('your base calorie consumption is')
         print(int(CPM))
     with open ('PPPM', 'wb') as file:
         pickle.dump(CPM, file)

def goal_of_user(nus):
 global goal_user
 with open('PPPM', 'rb') as file:
  CPM = pickle.load(file)
 with open('goals', 'rb') as file:
  goal_user = pickle.load(file)
 goal_user[str(nus)] = nus
 print('What is your calorie goal?(lose, maintain, gain')
 print('Lose weight')
 print('Maintain weight')
 print('Gain weight')
 pgoal = input()
 while pgoal != 'lose' and  pgoal != 'maintain' and  pgoal != 'gain':
     print('insert "lose" or "maintain" or "gain"')
     pgoal = input()
 if pgoal == 'lose':
  Weightincrease = int(CPM) * 0.85
  print( 'Your calorie goal is ')
  print(str(int(Weightincrease)))
 if pgoal == 'maintain':
  Weightincrease = int(CPM)
  print( 'Your calorie goal is ')
  print(str(int(Weightincrease)))
 if pgoal == 'gain':
  Weightincrease = int(CPM) * 1.15
  print( 'Your calorie goal is ')
  print(str(int(Weightincrease)))
 if udict[nus].activity == 'none' or 'small':
    protein = (Weightincrease * 0.15) / 4
    carbohydrates = (Weightincrease * 0.55) / 4
    fats = (Weightincrease * 0.30) / 9
 if udict[nus].activity == 'medium':
    protein = (Weightincrease * 0.25) / 4
    carbohydrates = (Weightincrease * 0.50) / 4
    fats = (Weightincrease * 0.25) / 9
 if udict[nus].activity == 'high':
    protein =(Weightincrease * 0.25) / 4
    carbohydrates = (Weightincrease * 0.55) / 4
    fats = (Weightincrease * 0.20) / 9
 if udict[nus].activity == ('very high'):
    protein = (Weightincrease * 0.25) / 4
    carbohydrates = (Weightincrease * 0.60) / 4
    fats = (Weightincrease * 0.15) / 9

 goal_user[nus] = Ugoal(calorieconsumption = CPM, goal = pgoal, gcalorie = Weightincrease, gprotein = protein, gfats = fats, gcarbohydrates = carbohydrates)
 with open('goals', 'wb') as file:
      pickle.dump(goal_user, file)

def new_user_package(nuss):
    new_user(nuss)
    Calorie_consumption(nuss)
    goal_of_user(nuss)

