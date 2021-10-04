from yandex import create_dir

Y_DISK_PATH = 'f9'


class TestYandex:
    def test_create_dir(self):
        expected = f'201 Dir created'
        assert create_dir(Y_DISK_PATH) == expected

    def test_create_dir_exist(self):
        expected = f'409 Dir exists'
        assert create_dir(Y_DISK_PATH) == expected
