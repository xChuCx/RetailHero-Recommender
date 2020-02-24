import pickle

import numpy as np
import scipy


class Predictor:
    def __init__(self, model_pickled_path, dict_pickled_path):
        self.model = pickle.load(open(model_pickled_path, "rb"))
        with open(dict_pickled_path, "rb") as f:
            (
                self.client_dict,
                self.reverse_client_dict,
                self.product_dict,
                self.reverse_product_dict,
            ) = pickle.load(f)
        self.matrix_shape = (1, max(self.reverse_product_dict.keys()) + 1)

    def predict(self, products):
        enum_clients = np.zeros(
            len([product for product in products if product in self.product_dict])
        )
        enum_products = np.array(
            [self.product_dict[product] for product in products if product in self.product_dict]
        )

        sparse_matrix = scipy.sparse.csr_matrix(
            (np.ones(shape=(len(enum_clients))), (enum_clients, enum_products)),
            shape=self.matrix_shape,
        )

        raw_recs = self.model.recommend(
            0, sparse_matrix, N=30, filter_already_liked_items=False, recalculate_user=True
        )
        return [self.reverse_product_dict[r[0]] for r in raw_recs]

