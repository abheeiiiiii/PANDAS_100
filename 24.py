import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    df1 = request_accepted[['requester_id']].rename(columns={'requester_id': 'id'})
    df2 = request_accepted[['accepter_id']].rename(columns={'accepter_id': 'id'})

    all_friends = pd.concat([df1, df2])

    counts = all_friends.value_counts().reset_index()
    counts.columns = ['id', 'num']

    max_friends = counts['num'].max()

    return counts[counts['num'] == max_friends]
