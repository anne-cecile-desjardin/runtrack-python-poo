class Student:
    def __init__(self, nom, prenom, num_etudiant, nb_credit):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__nb_credit = 0
        self.__level = self.__studentEval()

    def get_nom(self):
        return self.__nom
    
    def set_nom(self, nom):
        self.__nom = nom

    def get_prenom(self):
        return self.__prenom
    
    def set_prenom(self, prenom):
        self.__prenom = prenom
    
    def get_num_etudiant(self):
        return self.__num_etudiant
    
    def set_num_etudiant(self, num_etudiant):
        self.__num_etudiant = num_etudiant

    def get_nb_credit(self):
        return self.__nb_credit
    
    def set_nb_credit(self, nb_credit):
        self.__nb_credit = nb_credit

    def add_credits(self, credit_adding):
        if credit_adding > 0:
            self.__nb_credit += credit_adding
            self.__level = self.__studentEval() 
            return self.__nb_credit
        else :
            print("Le nombre rentré doit être supérieur à 0")

    def __studentEval(self):
        if self.__nb_credit >= 90:
            return "Excellent"
        elif self.__nb_credit >= 80:
            return "Trés bien"
        elif self.__nb_credit >= 70:
            return "Bien"
        elif self.__nb_credit > 60:
            return "Passable"
        else :
            return "Insuffisant"
        
    def get_level(self):
        return self.__studentEval()
    
    def set_level(self, level):
        self.__level = level

    
    def studentInfo(self):
        print(f"Nom = {self.__prenom} \nPrenom = {self.__nom} \nID: {self.__num_etudiant}")
        print(f"Nombre de crédits : {self.__nb_credit}")
        print(f"Niveau : {self.__level}")


        
etudiant1 = Student("Doe", "John", 145, 0)

# print(etudiant1.get_nom())
# print(etudiant1.get_prenom())
# print(etudiant1.get_num_etudiant())
# print(etudiant1.get_nb_credit())

etudiant1.add_credits(10)

# print(f"Le nombre de crédit de {etudiant1.get_prenom()} {etudiant1.get_nom()} est de {etudiant1.get_nb_credit()} points")

etudiant1.add_credits(41)

# print(f"Le nombre de crédit de {etudiant1.get_prenom()}{etudiant1.get_nom()} est de {etudiant1.get_nb_credit()} points")

etudiant1.add_credits(10)

# print(f"Le nombre de crédit de {etudiant1.get_prenom()}{etudiant1.get_nom()} est de {etudiant1.get_nb_credit()} points")
etudiant1.add_credits(10)
# print(f"Le nombre de crédit de {etudiant1.get_prenom()}{etudiant1.get_nom()} est de {etudiant1.get_nb_credit()} points")

etudiant1.studentInfo()
