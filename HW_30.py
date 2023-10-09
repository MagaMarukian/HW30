# 1․ Գրել MyShows class, որը․
#    - __init__ ում կստանա 
#      -- սերիալի անունը (պետք է լինի տեքստ), 
#      -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ), 
#      -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
#      -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 1,
#      -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
#      -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
#    - բոլոր ատրիբուտները կլինեն private,
#    - կունենա getter բոլոր ատրիբուտների համար,
#    - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
#    - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու հնարավորություն լինի,
#    - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
#    - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան։

class MyShows:
    def __init__(self, series_name, platform, release_year, list_of_actors, series_number=1, user_rating=None):
        self.validate_name(series_name)
        self.validate_platform(platform)
        self.validate_release_year(release_year)
        self.validate_actors_list(list_of_actors)
        self.validate_user_rating(user_rating)
        self.validate_series_number(series_number)

        self.__series_name = series_name
        self.__platform = platform
        self.__release_year = release_year
        self.__series_number = series_number
        self.__user_rating = user_rating
        self.__list_of_actors = list_of_actors

    @staticmethod
    def validate_name(n: str):
        if not isinstance(n, str):
            raise ValueError('Wrong Name')

    @staticmethod
    def validate_platform(p: str):
        if not isinstance(p, str):
            raise ValueError('Wrong Platform')
        
    @staticmethod
    def validate_release_year(y: int):
        if not (isinstance(y, int) and y > 0):
            raise ValueError('Wrong Year')

    @staticmethod
    def validate_series_number(sn: int):
        if not (isinstance(sn, int) and sn > 0):
            raise ValueError('Wrong Number')

    @staticmethod
    def validate_user_rating(ur: int):
        if not (isinstance(ur, int) and 1 <= ur <= 10 or ur is None):
            raise ValueError('Wrong Rating')
        
    @staticmethod
    def validate_actors_list(al: list):
        if not isinstance(al, list):
            raise ValueError('Wrong List')

    @property
    def _name(self):
        return self.__series_name

    @property
    def _platform(self):
        return self.__platform

    @property
    def _release(self):
        return self.__release_year

    @property
    def _number(self):
        return self.__series_number

    @property
    def _rating(self):
        return self.__user_rating    

    @property
    def _actors(self):
        return self.__list_of_actors 

    @_number.setter
    def _number(self, new_number):
        self.__series_number = new_number

    @_rating.setter
    def _rating(self, new_rating):
        self.__user_rating = new_rating
    
    @_rating.deleter
    def _rating(self):
        self.__user_rating = None
    
    @_actors.setter
    def _actors(self, adding_actors:list):
        self.__list_of_actors.extend(adding_actors)
    
    @_actors.deleter
    def _actors(self, removing_actors:list):
        [self.__list_of_actors.pop(i) for i in removing_actors]

    def description(self):
        return (self.__series_name, self._platform, self.__release_year, self.__list_of_actors, self.__series_number, self.__user_rating)


Show_1 = MyShows('Game of Thrones', 'HBO', 2012, ['Kit Harington', 'Emilia Clarke'], 1, 1)
print(Show_1.description())




