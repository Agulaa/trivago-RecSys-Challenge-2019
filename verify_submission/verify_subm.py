import pandas as pd
from verify_submission import functions as f


def main( subm_csv, test_csv):


    print('Reading files...')
    df_subm = pd.read_csv(subm_csv)
    df_test = pd.read_csv(test_csv)
    #df_subm.drop_duplicates(subset=['session_id'], inplace=True)

    print('Checking for required columns in the submission file...')
    check_cols = f.check_columns(df_subm)
    f.check_passed(check_cols)

    print('Checking for duplicate sessions in the submission file...')
    check_dupl = f.check_duplicates(df_subm)
    f.check_passed(check_dupl)

    print('Checking that all the required sessions are present in submission...')
    check_sess = f.check_sessions(df_subm, df_test)
    f.check_passed(check_sess)

    if all([check_cols, check_dupl, check_sess]):
        df_subm.to_csv(subm_csv)
        print('All checks passed')
    else:
        print('One or more checks failed')


if __name__ == '__main__':
    main()
