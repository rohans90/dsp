
dflist = df.email.tolist()
my_df = pd.DataFrame(dflist)

my_df.to_csv('email.csv', index=False, header=False)

