"""dexycb_dataset dataset."""

import tensorflow_datasets as tfds
from . import dexycb_dataset_dataset_builder


class DexycbDatasetTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for dexycb_dataset dataset."""
  # TODO(dexycb_dataset):
  DATASET_CLASS = dexycb_dataset_dataset_builder.Builder
  SPLITS = {
      'train': 3,  # Number of fake train example
      'test': 1,  # Number of fake test example
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == '__main__':
  tfds.testing.test_main()
