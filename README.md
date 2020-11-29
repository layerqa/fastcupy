# FASTCUPY
Unofficial python fascup module
[![GitHub Issues](https://img.shields.io/github/issues/layerqa/fastcupy)](https://github.com/layerqa/fastcupy/issues)
[![GitHub LICENSE](https://img.shields.io/github/license/layerqa/fastcupy)](https://github.com/layerqa/fastcupy/blob/main/LICENSE)

------------

### **Install**
```
$ pip install git+https://github.com/layerqa/fastcupy
```

------------

### **Usage example**

```python
from fastcupy import fastcupy

api = fastcupy()

# CSGO total statistics
data = api.get_total_statistics(game_id=1)

print(
    f'Matches: {data.matches_count}',
    f'Matches created: {data.matches_created_count}',
    f'Matches live: {data.matches_live_count}',
    f'Users search: {data.users_in_search}',
    f'Users in game: {data.users_ingame_count}',
    f'Users online: {data.users_online_count}',
    f'Users played: {data.users_played_count}',
    sep='\n'
)

# Matches: 391469
# Matches created: 26
# Matches live: 104
# Users search: 32
# Users in game: 746
# Users online: 1197
# Users player: 104148
```