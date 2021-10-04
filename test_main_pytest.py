import pytest
import unittest
from unittest import mock
from main import check_document_existence, get_doc_owner_name, get_all_doc_owners_names, \
    add_new_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, \
    add_new_doc, documents


class TestCheckPytest:

    @pytest.mark.parametrize('doc_number', [doc['number'] for doc in documents])
    def test_check_document_existence(self, doc_number):
        assert check_document_existence(doc_number) is True

    def test_get_doc_owner_name(self):
        with unittest.mock.patch('builtins.input', return_value='10006'):
            assert get_doc_owner_name() == 'Аристарх Павлов'

    def test_get_all_doc_owners_names(self):
        assert get_all_doc_owners_names() == set([doc['name'] for doc in documents])

    @pytest.mark.parametrize('shelf_number, expected, truth', [('1', '1', False),
                                                               ('2', '2', False),
                                                               ('3', '3', False),
                                                               ('4', '4', True)])
    def test_add_new_shelf(self, shelf_number, expected, truth):
        assert add_new_shelf(shelf_number=shelf_number) == (expected, truth)

    @pytest.mark.parametrize('shelf_number, doc_number',
                             [('1', '2207 876234'),
                              ('1', '5455 028765'),
                              ('1', '11-2'),
                              ('2', '10006')])
    def test_get_doc_shelf(self, shelf_number, doc_number):
        with mock.patch('builtins.input', return_value=doc_number):
            assert get_doc_shelf() == (shelf_number)

    def test_delete_doc(self):
        with mock.patch('builtins.input', return_value='10006'):
            assert delete_doc() == ('10006', True)

    @pytest.mark.parametrize('doc_number, shelf_number',
                             [('2207 876234', '2')])
    def test_move_doc_to_shelf(self, doc_number, shelf_number):
        assert move_doc_to_shelf() == (doc_number, shelf_number)

    @pytest.mark.parametrize('new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number',
                             [('1534', 'invoice', 'Jim Beam', '3')])
    def test_add_new_doc(self, new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number):
        assert add_new_doc() == str(new_doc_shelf_number)
