from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd


def main():
    data = pd.read_csv('../input/okcupid-profiles/okcupid_profiles.csv')

    # print(len(data.columns))
    data = data.iloc[:, 0:21]
    data = data.drop(['smokes','orientation','status','drinks','body_type','diet','drugs','education','ethnicity','last_online','location','offspring','pets','job','religion','sign','speaks'], axis=1)
    print(data.columns)
    print(data.info())
    # data.head()

    for c in data.columns:
        vc = data[str(c)].value_counts()
        print(vc)
        print('######################')

    data['sex'] = data['sex'].replace('m', 1.0)
    data['sex'] = data['sex'].replace('f', -1.0)

    # data['income'] = data['income'].replace(-1, int(np.mean(data['income'])))
    data = data[data['income']!=-1]

    # data['smokes'] = data['smokes'].replace('no', 0.0)
    # data['smokes'] = data['smokes'].fillna(0.0)
    # data['smokes'] = data['smokes'].replace(['sometimes','when drinking','trying to quit'], 1.0)
    # data['smokes'] = data['smokes'].replace('yes', 2.0)
    data.head(20)

    y = data['income']
    x = data.drop(['income'], axis=1)
    # 正規化
    xss_pd = (x - x.mean()) / x.std()
    yss_pd = (y - y.mean()) / y.std()

    model_lr = LinearRegression()
    model_lr.fit(xss_pd, yss_pd)

    from mpl_toolkits.mplot3d import Axes3D  #3Dplot
    import matplotlib.pyplot as plt

    fig=plt.figure()
    ax=Axes3D(fig)
    x1 = x['height']
    x2 = x['sex']
    ax.scatter3D(x1, x2, y)
    ax.set_xlabel("age")
    ax.set_ylabel("sex")
    ax.set_zlabel("income")
    plt.show()

    print(model_lr.score(xss_pd, yss_pd))

    s_all = ((yss_pd - yss_pd.mean())**2).sum()
    s_reg = ((model_lr.predict(xss_pd) - yss_pd.mean())**2).sum()
    s_res = ((yss_pd - model_lr.predict(xss_pd))**2).sum()

    R = 1 - (s_res / (yss_pd.size - 2 - 1)) / (s_all / (yss_pd.size -1))
    print(R)

if __name__== '__main__':
    main()