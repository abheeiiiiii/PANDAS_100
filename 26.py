import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    parents = set(tree['p_id'].dropna())

    def node_type(row):
        if pd.isna(row['p_id']):
            return 'Root'
        elif row['id'] not in parents:
            return 'Leaf'
        else:
            return 'Inner'

    tree['type'] = tree.apply(node_type, axis=1)
    return tree[['id', 'type']]