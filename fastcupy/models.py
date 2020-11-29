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
        self.matches_live_count = data['statisticsTotal']['matchesLiveCount']
        self.matches_created_count = data['statisticsTotal']['matchesCreatedCount']
        self.matches_count = data['statisticsTotal']['matchesCount']
        self.users_played_count = data['statisticsTotal']['usersPlayedCount']
        self.users_online_count = data['statisticsTotal']['usersOnlineCount']
        self.users_in_search = data['statisticsTotal']['usersInSearch']
        self.users_ingame_count = data['statisticsTotal']['usersIngameCount']