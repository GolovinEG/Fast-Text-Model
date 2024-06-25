# Fast-Text-Model
Allows for a quick creation of a text neural network model, as well as for creation of graphs describing it.

---
# build_model():
    (function) def build_model(
        df: DataFrame,
        x_column: str | list,
        y_column: str,
        v_type: Literal['CountVectorizer', 'HashingVectorizer', 'TfidfTransformer', 'TfidfVectorizer'],
        c_type: Literal['LogisticRegression', 'LogisticRegressionCV', 'PassiveAggressiveClassifier', 'Perceptron', 'RidgeClassifier', 'RidgeClassifierCV', 'SGDClassifier', 'SGDOneClassSVM'],
        v_params: dict | None = None,
        c_params: dict | None = None,
        file_name: str = "model.pickle",
        random_state: int | None = None,
        verbose: bool = False
    ) -> tuple
Builds a text model with a the chosen vecotorizer and classifier and returns the training and test sets.
Also creates a pickle file. Loading the file will return a tupple: (vectorizer, classifier, labels, feature_names)
# Parameters
    df - pandas DataFrame containing the dataset
    x_column - the label (or list of labels) of the input data
    y_column - the label of the target data
    v_type - text vectorizer type to build
    c_type - classifier type to build
    v_params - a dictionary of vectorizer parameter
    c_params - a dictionary of classifier parameter
    file_name - the name of the pickle file to save the model to
    random_state - random state to use in train_test_split for testing
    verbose - enables debugging output
---
# set_vectorizer():
    (function) def set_vectorizer(
        v_type: Literal['CountVectorizer', 'HashingVectorizer', 'TfidfTransformer', 'TfidfVectorizer'],
        v_params: dict | None = None
    ) -> Any
Returns given text vectorizer with given parameters

---
# set_classifier():
    (function) def set_classifier(
        c_type: Literal['LogisticRegression', 'LogisticRegressionCV', 'PassiveAggressiveClassifier', 'Perceptron', 'RidgeClassifier', 'RidgeClassifierCV', 'SGDClassifier', 'SGDOneClassSVM'],
        c_params: dict | None = None
    ) -> Any
Returns given classifier with given parameters

---
# output_graphs_generic():
    (function) def output_graphs_generic(
        classifier: Any,
        X_train: csc_matrix,
        X_test: csc_matrix,
        y_test: Series,
        labels: ndarray,
        feature_names: ndarray
    ) -> None
Outputs plotly graphs for given model and data. Doesn't output graphs for binary classification
# Parameters
    classifier - model's classifier, [1] member of the model.pickle file data
    X_train - training input
    X_test - test input
    y_test - test target
    labels - labels array [2] member of the model.pickle file data
    feature_names - feature names array, [3] member of the model.pickle file data
---
# output_graphs_binary_selection():
    (function) def output_graphs_binary_selection(
        classifier: Any,
        X_test: csc_matrix,
        y_test: Series,
        labels: ndarray
    ) -> None
Outputs plotly graphs for given binary classification model and data.
# Parameters
    classifier - model's classifier, [1] member of the model.pickle file data
    X_test - test input
    y_test - test target
    labels - labels array [2] member of the model.pickle file data
