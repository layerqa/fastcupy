from gql import Client
from gql.transport.requests import RequestsHTTPTransport

from .exceptions import GameIdError
from .models import TotalStatistics
from .querys import get_total_statistics_query


class fastcupy:
    '''
    Unofficial fascup api wrapper for python3
    '''
    def __init__(self):
        self._url = 'https://hasura.fastcup.net/v1/graphql'
        self._transport = RequestsHTTPTransport(url=self._url)
        self._client = Client(transport=self._transport)
    
    def _check_game_id(self, game_id: int) -> [GameIdError, int]:
        if game_id <= 2:
            return game_id
        else:
            raise GameIdError('Game id is not 1 or 2')

    def _send_request(self, query: str, variables: dict) -> dict:
        '''
        Send request https://hasura.fastcup.net/v1/graphql
        :query: str
        :variables: dict
        '''
        response = self._client.execute(query, variable_values=variables)
        return response

    def get_total_statistics(self, game_id: int) -> TotalStatistics:
        '''
        Get total statistics
        :game_id: int
        1 = CSGO, 2 = CS 1.6
        '''
        variables = {"gameID": self._check_game_id(game_id)}
        return TotalStatistics(self._send_request(
            query=get_total_statistics_query, variables=variables
        ))
