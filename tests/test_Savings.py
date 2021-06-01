from datetime import datetime
from exercise_41_1.Saving import Saving
from exercise_41_1.Savings import Savings


def test_add_saving():
    # given
    now1 = datetime(2021, 5, 21, 12, 50)
    saving1 = Saving(30.5, now1)
    now2 = datetime(2021, 5, 21, 13, 50)
    saving2 = Saving(300.0, now2)
    savings1 = Savings()
    # when
    savings1.add_saving(saving1)
    savings1.add_saving(saving2)
    # then
    assert savings1.get_sum_of_all_savings() == 330.5
    # assert savings1.print_savings_as_dict_list() == [
    #                                                        {
    #                                                         'date': '21.05.2021 12:50:00',
    #                                                         'amount': 35.0
    #                                                        },
    #                                                        {
    #                                                         'date': '21.05.2021 13:50:00',
    #                                                         'amount': 300.0
    #                                                        }
    #                                                    ]
