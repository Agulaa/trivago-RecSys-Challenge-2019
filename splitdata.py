import numpy as np
import pandas as pd


def split_dataset(df, stamp):
    # Get all session id
    all_session_ids = df.session_id.unique()
    num_of_session = len(all_session_ids)
    # Last number of train session
    num_train_session = int(stamp * num_of_session)
    # Get session_id for last item
    dftrain_end_session_id = all_session_ids[num_train_session]
    # Get last index
    dftrain_last_index = int(df[df.session_id==dftrain_end_session_id][-1:].index[0])
    # Split data to train and test and ground Truth
    df_train = df[:dftrain_last_index+1]
    groundTruth = df[dftrain_last_index+1:]
    # Change test set -> in last step put NaN
    # get first step
    idx_step_1 = np.array(groundTruth[groundTruth.step == 1].index)
    # get last step
    idx_last_step = [x-1 for x in idx_step_1[1:] ]
    # Prepare test set
    df_test = groundTruth.copy()
    df_test_label = df_test[(df_test.index.isin(idx_last_step)) & (df_test.action_type == 'clickout item')]['reference']
    # Change reference to Nan if action_type is clickout item and is last step
    df_test.loc[(df_test.index.isin(idx_last_step)) & (df_test.action_type == 'clickout item'), 'reference'] = np.nan
    # Saving sets
    df_train.to_csv('../data/train.csv')
    groundTruth.to_csv('../data/groundTruth.csv')
    df_test.to_csv('../data/test.csv')
    df_test_label.to_csv('../data/reference.csv')
    return df_train, df_test, groundTruth

if __name__ == '__main__':
    df = pd.read_csv('../data/Rectrain.csv')
    df_train, df_test, groundTruth = split_dataset(df, 0.8)
