import typing

class TotalStatistics:
    def __init__(self, data: dict) -> None:
        '''
        Total statistics details
        Attributes
        ----------
        matches_live_count: int
        matches_created_count: int
        matches_count: int
        users_played_count: int
        users_online_count: int
        users_in_search: int
        users_ingame_count: int
        '''
        self.matches_live_count: int = int(data['statisticsTotal']['matchesLiveCount'])
        self.matches_created_count: int = int(data['statisticsTotal']['matchesCreatedCount'])
        self.matches_count: int = int(data['statisticsTotal']['matchesCount'])
        self.users_played_count: int = int(data['statisticsTotal']['usersPlayedCount'])
        self.users_online_count: int = int(data['statisticsTotal']['usersOnlineCount'])
        self.users_in_search: int = int(data['statisticsTotal']['usersInSearch'])
        self.users_ingame_count: int = int(data['statisticsTotal']['usersIngameCount'])

class GetUser:
    def __init__(self, data: dict) -> None:
        '''
        User details
        :user_id: int
        :nick_name: str
        :avatar: str
        :online: bool
        :is_mobile: bool
        :link: [str, None]
        :stats: list
        :bans: list
        :city: City model
        :country: Country model
        :steam_id: int
        :first_name: str
        :last_name: str
        :last_ctivity: str
        :created_at: str
        :friends_count: int
        '''
        data = data['users'][0]
        self.user_id: int = int(data['id'])
        self.nick_name: str = str(data['nickName'])
        self.avatar: str = str(data['avatar'])
        self.online: bool = bool(data['online'])
        self.is_mobile: bool = bool(data['isMobile'])
        self.link = data['link']
        self.stats: typing.List[int, str] = list(data['stats'])
        self.bans: typing.List[int, str] = list(data['bans'])
        self.city = City(data['city'])
        self.country = Country(data['country'])
        self.steam_id: int = int(data['steamID'])
        self.first_name = data['firstName']
        self.last_name = data['lastName']
        self.last_ctivity: str = str(data['lastActivity'])
        self.created_at: str = str(data['createdAt'])
        self.friends_count: int = int(data['friendsCount'])

class City:
    def __init__(self, city: dict) -> None:
        self.city_id: int = int(city['id'])
        self.region_id: int = int(city['regionID'])
        self.name_ru: str = str(city['name_ru'])
        self.name_en: str = str(city['name_en'])

class Country:
    def __init__(self, country: dict) -> None:
        self.country_id: int = int(country['id'])
        self.iso2: str = str(country['iso2'])
        self.name_ru: str = str(country['name_ru'])
        self.name_en: str = str(country['name_en'])

class Stats:
    def __init__(self, stats: dict) -> None:
        '''
        User stats details
        :game_mode_id: int
        :rating: [int, float]
        :place: int
        '''
        for i in stats:
            self.game_mode_id: int = i['gameModeID']
            self.rating: [int, float] = i['rating']
            self.place: int = i['place']