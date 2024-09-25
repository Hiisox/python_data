import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def categorize_age(age : float) -> int:
    age_cat = [12, 19, 30, 50, 70, 100]
    for i in range(len(age_cat)):
        if age <= age_cat[i]:
            return i

def categorize_price(price : float) -> int:
    price_cat = [7.91, 14.45, 31.0, 80.0, 150.0, 1000000]
    for i in range(len(price_cat)):
        if price <= price_cat[i]:
            return i

def replace_name(name_str: str) -> int:
    attribut_tab = ["Miss.", "Mrs.", "Mr.", "Master."]
    for i in range(len(attribut_tab)):
        if name_str.find(attribut_tab[i]) != -1:
            return i
    return 4


def get_final_file(name : str) -> object:
    
    my_file = pd.read_csv(name)
    if name == "train.csv":
        print(my_file.Fare.describe())
    my_file.Embarked = my_file.Embarked.fillna("Z")
    my_file.Embarked = my_file.Embarked.map(lambda y: ord(y))
    my_file.Age = my_file.Age.fillna(round(my_file.Age.mean(), 1))
    my_file.Age = my_file.Age.map(categorize_age)
    my_file.Age = my_file.Age.astype(int)
    my_file.Cabin = my_file.Cabin.map(lambda y: y if pd.isna(y) else 1)
    my_file.Cabin = my_file.Cabin.fillna(0)
    my_file.Fare = my_file.Fare.fillna(my_file.Fare.mean())
    my_file.Fare = my_file.Fare.map(categorize_price)
    my_file.Name = my_file.Name.map(replace_name)
    columns = ['Name', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    try:
        result = my_file['Survived']
    except:
        result = None
    my_file["Sex"] = my_file.Sex.map(lambda y: 0 if y == "male" else 1)
    my_file = my_file[columns]
    # my_file.to_csv("final_csv.csv")
    return my_file, result


def main():
    train_file, result = get_final_file("train.csv")
    titanic_model = RandomForestClassifier(max_leaf_nodes=75 ,random_state=0)
    titanic_model.fit(train_file, result)
    test_file, result_test = get_final_file("test.csv")
    predictions = titanic_model.predict(test_file)
    returned_file = pd.DataFrame(columns=['PassengerId', 'Survived'])
    for i in range(len(test_file)):
        returned_file = returned_file._append({'PassengerId': f'{i + 892}', 'Survived': f'{predictions[i]}'}, ignore_index=True)
    returned_file = returned_file.set_index("PassengerId")
    returned_file.to_csv("submission.csv")



if __name__ == "__main__":
    main()