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

get_user = gql('''
query GetUser($gameID: smallint!, $id: Int, $link: String, $steamID: Int) {
  users(
    where: {id: {_eq: $id}, link: {_eq: $link}, steam_id: {_eq: $steamID}}
    limit: 1
  ) {
    id
    ...UserCommon
    ...UserStats
    ...UserBan
    ...UserGeo
    steamID: steam_id
    blacklisted {
      targetUserID: target_user_id
      userID: user_id
    }
    isMeBlacklisted {
      targetUserID: target_user_id
      userID: user_id
      private {
        reason
      }
    }
    firstName: first_name
    lastName: last_name
    gender
    birthday
    lastActivity: last_activity
    createdAt: created_at
    friendsCount: friends_count
    friends(where: {state: {_eq: "ACCEPTED"}}, order_by: {date: desc}, limit: 5) {
      ...Friend
    }
    streams(where: {game_id: {_eq: $gameID}}, limit: 1) {
      id
      name
      followers
      views
      viewers
      online
      service {
        id
        name
        rawName: raw_name
      }
      source
      chatID: chat_id
    }
    matchMemberships(
      where: {finished: {_eq: false}, game_id: {_eq: $gameID}}
      limit: 1
    ) {
      kills
      deaths
      assists
      finished
      matchID: match_id
      match {
        status
        type
        readinessPassed: readiness_passed
        gameStatus: game_status
        teams(order_by: {id: asc}) {
          size
          score
        }
        createdAt: created_at
        startedAt: started_at
        bestOf: best_of
        maps(order_by: {number: asc}) {
          map {
            id
            name
            rawName: raw_name
          }
          gameStatus: game_status
        }
        serverInstance {
          ip
          tvPort: tv_port
        }
        gameMode {
          id
          name: name_en
        }
        tvAddressHidden: tv_address_hidden
      }
    }
    verified
    vkID: vk_id
    fbID: fb_id
    twitchID: twitch_id
    instagramID: instagram_id
    privacyFeedWrite: privacy_feed_write
  }
}

fragment UserCommon on users {
  id
  nickName: nick_name
  avatar
  online
  isMobile: is_mobile
  link
}

fragment UserStats on users {
  stats(
    where: {game_id: {_eq: $gameID}, map_id: {_is_null: true}, game_mode_id: {_is_null: false}}
  ) {
    gameModeID: game_mode_id
    rating
    place
  }
}

fragment UserBan on users {
  bans(
    where: {active: {_eq: true}, game_id: {_eq: $gameID}}
    order_by: {until: desc}
  ) {
    id
    since
    until
    reason {
      id
      name_ru
      name_uk
      name_en
      name_de
      name_pl
      name_pt
      name_es
      name_hbs
      name_tr
      description_ru
      description_uk
      description_en
      description_de
      description_pl
      description_pt
      description_es
      description_hbs
      description_tr
      restrictions
      __typename
    }
    comment
  }
}

fragment Friend on friends {
  userID: user_id
  friendID: friend_id
  date
  state
  friend_id
  user {
    ...UserCommon
    ...UserStats
    ...UserLastActiveBan
  }
}

fragment UserLastActiveBan on users {
  bans(
    where: {active: {_eq: true}, game_id: {_eq: $gameID}}
    order_by: {length_minutes: desc}
    limit: 1
  ) {
    id
    since
    until
  }
}

fragment UserGeo on users {
  city {
    id
    regionID: region_id
    name_ru
    name_uk
    name_en
    name_de
    name_pl
    name_pt
    name_es
    name_hbs
    name_tr
  }
  country {
    id
    name_ru
    name_uk
    name_en
    name_de
    name_pl
    name_pt
    name_es
    name_hbs
    name_tr
    iso2
  }
}
''')