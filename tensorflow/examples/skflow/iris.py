"""Example of DNNClassifier for Iris plant dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from sklearn import cross_validation
from sklearn import metrics
import tensorflow as tf
from tensorflow.contrib import learn


def main(unused_argv):
  # Load dataset.
  iris = learn.datasets.load_dataset('iris')
  x_train, x_test, y_train, y_test = cross_validation.train_test_split(
      iris.data, iris.target, test_size=0.2, random_state=42)

  # Build 3 layer DNN with 10, 20, 10 units respectively.
  feature_columns = learn.infer_real_valued_columns_from_input(x_train)
  classifier = learn.DNNClassifier(
      feature_columns=feature_columns, hidden_units=[10, 20, 10], n_classes=3)

  # Fit and predict.
  classifier.fit(x_train, y_train, steps=200)
  score = metrics.accuracy_score(y_test, classifier.predict(x_test))
  print('Accuracy: {0:f}'.format(score))


if __name__ == '__main__':
  tf.app.run()
