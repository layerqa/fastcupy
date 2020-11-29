from gql import gql

get_total_statistics_query = gql('''
query GetStatisticsTotal($gameID: smallint!) {
  statisticsTotal: statistics_total_by_pk(game_id: $gameID) {
    matchesLiveCount: matches_live
    matchesCreatedCount: matches_created
    matchesCount: matches
    usersPlayedCount: users_played
    usersOnlineCount: users_online
    usersInSearch: users_insearch
    usersIngameCount: users_ingame
  }
}
''')