def fun_in_the_sun():
    global age
    if holiday_programme == 1:
        age = input("What is your child's age: ")
        fun_in_the_sun_.append(age)


def active_kidz():
    global age
    global holiday_programme
    if holiday_programme == 2:
        age = input("What is your child's age: ")
        active_kidz_.append(age)
    holiday_programme = 0


def details():
    global active_kidz_
    global fun_in_the_sun_
    print(sum(fun_in_the_sun_) / len(fun_in_the_sun_))
    print(sum(active_kidz_) / len(active_kidz_))


active_kidz_ = []
fun_in_the_sun_ = []
holiday_programme = 0
while holiday_programme == 0:
    holiday_programme = int(input(
        "What holiday program is your child attending, 1 for Fun in the sun, 2 for Active kidz,\nand 3 for details about each holiday programme: "))

if holiday_programme == 1:
    fun_in_the_sun()
    holiday_programme = 0
if holiday_programme == 2:
    active_kidz()
    holiday_programme = 0
if holiday_programme == 3:
    details()
