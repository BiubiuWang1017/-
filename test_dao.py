# test_dao.py
import unittest
from dao import DisciplineDao
from models import Discipline
from database_config import connection_string


class TestDisciplineDao(unittest.TestCase):
    def setUp(self):
        self.discipline_dao = DisciplineDao(connection_string)

    def test_add_discipline(self):
        # 创建一个新的一级学科实例
        new_discipline = Discipline('D011', 'A010', '土木工程', '研究土木工程')

        # 使用DisciplineDao的add_discipline方法将一级学科添加到数据库中
        self.discipline_dao.add_discipline(new_discipline)

        # 获取并打印增加后的数据
        retrieved_discipline = self.discipline_dao.get_discipline_by_id('D011')
        self.assertIsNotNone(retrieved_discipline)
        print(
            f"增加后的数据: 学院ID: {retrieved_discipline[1]}, 学科名称: {retrieved_discipline[2]}, 学科概述: {retrieved_discipline[3]}")

    def tearDown(self):
        self.discipline_dao.delete_discipline('D011')  # 清理测试数据
        self.discipline_dao.close()


if __name__ == '__main__':
    unittest.main()
