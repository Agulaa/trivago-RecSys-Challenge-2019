from  score_submission import functions as f

def main(gt_csv, subm_csv ):

    mrr = f.score_submissions(subm_csv, gt_csv, f.get_reciprocal_ranks)

    print(f'Mean reciprocal rank: {mrr}')


if __name__ == '__main__':
    main()
