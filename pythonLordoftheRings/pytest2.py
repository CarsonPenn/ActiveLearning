from question_class import question
from LOTRquiz_final import *
# test_water_flow.py



def easy():
    assert easy(question)
#     =



# def test_pressure_gain_from_water_height():
#     assert pressure_gain_from_water_height(0) == pytest.approx(0, abs=0.001)
#     assert pressure_gain_from_water_height(30.2) == pytest.approx(295.628, abs=0.001)
#     assert pressure_gain_from_water_height(50) == pytest.approx(489.450, abs=0.001)
    


# def test_pressure_loss_from_pipe():
#     assert pressure_loss_from_pipe(0.048692,0,0.018,1.75) == pytest.approx(0, abs=0.001)
#     assert pressure_loss_from_pipe(0.048692,200,0,1.75) == pytest.approx(0, abs=0.001)
#     assert pressure_loss_from_pipe(0.048692,200,0.018,0) == pytest.approx(0, abs=0.001)
#     assert pressure_loss_from_pipe(0.048692,200,0.018,1.75) == pytest.approx(-113.008, abs=0.001)
#     assert pressure_loss_from_pipe(0.048692,200,0.018,1.65) == pytest.approx(-100.462, abs=0.001)
#     assert pressure_loss_from_pipe(0.28687,1000,0.013,1.65) == pytest.approx(-61.576, abs=0.001)
#     assert pressure_loss_from_pipe(0.28687,1800.75,0.013,1.65) == pytest.approx(-110.884, abs=0.001)





# def test_pressure_loss_from_fittings():
#     assert pressure_loss_from_fittings(0, 3) == pytest.approx(0, abs=0.001)
#     assert pressure_loss_from_fittings(1.65, 0) == pytest.approx(0, abs=0.001)
#     assert pressure_loss_from_fittings(1.65, 2) == pytest.approx(-0.109, abs=0.001)
#     assert pressure_loss_from_fittings(1.75, 2) == pytest.approx(-0.122, abs=0.001)
#     assert pressure_loss_from_fittings(1.75, 5) == pytest.approx(-0.306, abs=0.001)


# def test_reynolds_number():
#     assert reynolds_number(0.048692, 0) == pytest.approx(0, abs=1)
#     assert reynolds_number(0.048692, 1.65) == pytest.approx(80069, abs=1)
#     assert reynolds_number(0.048692, 1.75) == pytest.approx(84922, abs=1)
#     assert reynolds_number(0.28687, 1.65) == pytest.approx(471729, abs=1)
#     assert reynolds_number(0.28687, 1.75) == pytest.approx(500318, abs=1)


# def test_pressure_loss_from_pipe_reduction():
#     assert pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) == pytest.approx(0, abs=0.001)
#     assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == pytest.approx(-163.744, abs=0.001)
#     assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == pytest.approx(-184.182, abs=0.001)


# pytest.main(["-v", "--tb=line", "-rN", __file__])
# # used chatgpt to help me find numbers like the pressure and fitting loss to test the water_flow program against.
