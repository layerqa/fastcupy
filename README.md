# FASTCUPY
Unofficial python fascup module

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
```